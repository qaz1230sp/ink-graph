#!/usr/bin/env python3
"""Validate SVG file syntax.

Uses (in priority order):
1. rsvg-convert (most reliable SVG validation)
2. xmllint (XML-level validation)
3. Python xml.etree.ElementTree (built-in fallback, no external deps)

Exit 0 = valid, Exit 1 = invalid or missing file.
"""

import subprocess
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def find_tool(*names: str) -> str | None:
    for name in names:
        if shutil.which(name):
            return name
    return None


def validate_with_rsvg(filepath: Path) -> tuple[bool, str]:
    result = subprocess.run(
        ["rsvg-convert", str(filepath), "-o", "/dev/null" if sys.platform != "win32" else "NUL"],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr.strip()


def validate_with_xmllint(filepath: Path) -> tuple[bool, str]:
    result = subprocess.run(
        ["xmllint", "--noout", str(filepath)],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr.strip()


def validate_with_etree(filepath: Path) -> tuple[bool, str]:
    """Built-in Python XML parser. Catches malformed XML and basic SVG issues."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        ns = root.tag.split("}")[0] + "}" if "}" in root.tag else ""
        tag_local = root.tag.replace(ns, "")
        if tag_local != "svg":
            return False, f"Root element is <{tag_local}>, expected <svg>"

        # Check viewBox exists
        vb = root.get("viewBox")
        if vb:
            parts = vb.replace(",", " ").split()
            if len(parts) != 4:
                return False, f"viewBox has {len(parts)} values, expected 4"
            try:
                nums = [float(p) for p in parts]
                if nums[2] <= 0 or nums[3] <= 0:
                    return False, f"viewBox width/height must be positive: {vb}"
            except ValueError:
                return False, f"viewBox contains non-numeric values: {vb}"

        # Check for duplicate IDs
        all_ids: dict[str, int] = {}
        for elem in root.iter():
            eid = elem.get("id")
            if eid:
                all_ids[eid] = all_ids.get(eid, 0) + 1
        dupes = [k for k, v in all_ids.items() if v > 1]
        if dupes:
            return False, f"Duplicate IDs: {', '.join(dupes[:5])}"

        # Check url(#id) references have matching definitions
        import re
        url_pattern = re.compile(r'url\(#([^)]+)\)')
        referenced_ids: set[str] = set()
        for elem in root.iter():
            for attr_val in elem.attrib.values():
                referenced_ids.update(url_pattern.findall(attr_val))
            if elem.text:
                referenced_ids.update(url_pattern.findall(elem.text))
        missing = referenced_ids - set(all_ids.keys())
        if missing:
            return False, f"Missing referenced IDs: {', '.join(sorted(missing)[:5])}"

        return True, ""
    except ET.ParseError as e:
        return False, str(e)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python validate_svg.py <file.svg>")
        return 1

    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"ERROR: File not found: {filepath}")
        return 1

    # Try validators in priority order
    tool = find_tool("rsvg-convert")
    if tool:
        valid, msg = validate_with_rsvg(filepath)
        validator = "rsvg-convert"
    elif find_tool("xmllint"):
        valid, msg = validate_with_xmllint(filepath)
        validator = "xmllint"
    else:
        valid, msg = validate_with_etree(filepath)
        validator = "python-xml"

    if valid:
        print(f"✓ Valid SVG ({validator}): {filepath}")
        return 0
    else:
        print(f"✗ Invalid SVG ({validator}): {filepath}")
        if msg:
            print(f"  {msg}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
