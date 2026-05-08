#!/usr/bin/env python3
"""Export SVG to PNG.

Uses (in priority order):
1. rsvg-convert (best quality, handles CSS/animations correctly)
2. cairosvg Python package (pip install cairosvg)
3. Inkscape CLI

Exit 0 = success, Exit 1 = failure.
"""

import subprocess
import shutil
import sys
from pathlib import Path


def export_with_rsvg(svg_path: Path, png_path: Path, width: int) -> tuple[bool, str]:
    result = subprocess.run(
        ["rsvg-convert", "-w", str(width), str(svg_path), "-o", str(png_path)],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr.strip()


def export_with_cairosvg(svg_path: Path, png_path: Path, width: int) -> tuple[bool, str]:
    try:
        import cairosvg
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
        return True, ""
    except ImportError:
        return False, "cairosvg not installed"
    except OSError:
        return False, "cairosvg installed but cairo library not found"
    except Exception as e:
        return False, str(e)


def export_with_inkscape(svg_path: Path, png_path: Path, width: int) -> tuple[bool, str]:
    inkscape = shutil.which("inkscape")
    if not inkscape:
        return False, "inkscape not found"
    result = subprocess.run(
        [inkscape, str(svg_path), "--export-type=png",
         f"--export-filename={png_path}", f"--export-width={width}"],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr.strip()


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python export_png.py <file.svg> [width]")
        print("  width: output width in pixels (default: 1920)")
        return 1

    svg_path = Path(sys.argv[1])
    try:
        width = int(sys.argv[2]) if len(sys.argv) > 2 else 1920
        if width <= 0:
            raise ValueError("must be positive")
    except ValueError:
        print("ERROR: width must be a positive integer")
        return 1

    if not svg_path.exists():
        print(f"ERROR: File not found: {svg_path}")
        return 1

    png_path = svg_path.with_suffix(".png")

    # Try exporters in priority order
    exporters = [
        ("rsvg-convert", export_with_rsvg),
        ("cairosvg", export_with_cairosvg),
        ("inkscape", export_with_inkscape),
    ]

    for name, exporter in exporters:
        if name == "rsvg-convert" and not shutil.which("rsvg-convert"):
            continue
        if name == "inkscape" and not shutil.which("inkscape"):
            continue

        success, msg = exporter(svg_path, png_path, width)
        if success:
            print(f"✓ Exported ({name}): {png_path} ({width}px wide)")
            return 0
        # If tool is genuinely unavailable, try next
        if "not installed" in msg or "not found" in msg:
            continue
        # Real failure from an available tool
        print(f"✗ Export failed ({name}): {svg_path}")
        if msg:
            print(f"  {msg}")
        return 1

    print("ERROR: No PNG exporter available.")
    print("Install one of:")
    print("  pip install cairosvg")
    print("  Ubuntu/Debian: sudo apt install librsvg2-bin")
    print("  macOS: brew install librsvg")
    print("  Windows: choco install rsvg-convert")
    print("  Or install Inkscape")
    return 1


if __name__ == "__main__":
    sys.exit(main())
