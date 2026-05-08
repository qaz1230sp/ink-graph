# Starfield Style Reference

Use this file as the **source of truth** for the `starfield` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: deep space, quiet cosmic glow, and elegant technical clarity. This theme evokes star maps and nebula fields with a radial space backdrop, low-opacity color washes, thin typography, luminous blue nodes, restrained group containers, and sparse animated starlight.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| space-bg-center | #0d1b2a | Radial background center |
| space-bg-edge | #050a14 | Radial background edge |
| nebula-purple | #7850b4 | Nebula wash 1 |
| nebula-teal | #50b4c8 | Nebula wash 2 |
| nebula-blue | #5f7fd6 | Nebula wash 3 |
| star-white | #ffffff | Primary stars, title |
| star-ice | #c0d8ff | Secondary stars |
| node-stroke | #7eb8da | Node borders, data accents, glow tint |
| edge-data | #7eb8da | Data flow edges |
| edge-control | #c0a0e0 | Control edges |
| edge-dependency | #e8a060 | Dependency edges |
| text-title | #ffffff | Diagram title |
| text-subtitle | #8aacc0 | Subtitle, node sublabels |
| text-primary | #e0e8f0 | Node labels, legend text |
| group-fill | rgba(126,184,218,0.04) | Group background |
| group-stroke | rgba(126,184,218,0.25) | Group border |
| group-label | #7eb8da | Group titles, legend title |
| node-fill | rgba(13,27,42,0.85) | Node body fill |
| legend-fill | rgba(5,10,20,0.9) | Legend panel fill |
| junction-control | #c0a0e0 | Control junction dots |
| junction-data | #7eb8da | Data junction dots |

## Typography

font-family: "Inter", "Segoe UI", sans-serif
- Title: 24px, font-weight 300, color text-title, letter-spacing 3px
- Subtitle: 12px, font-weight 400, color text-subtitle, letter-spacing 1.2px
- Node label: 14px, font-weight 600, color text-primary
- Sub-label: 11px, font-weight 400, color text-subtitle
- Legend text: 11px, font-weight 400, color text-primary
- Group label: 12px, font-weight 600, letter-spacing 1.4px, color group-label
- Legend title: 12px, font-weight 600, letter-spacing 0.8px, color group-label

## Node Styles

```css
.node-shape {
  fill: rgba(13,27,42,0.85);
  stroke: #7eb8da;
  stroke-width: 1;
  filter: url(#star-glow);
}
```

Nodes use a dark translucent fill, 1px stellar-blue stroke, soft glow, and rx="8" for subtle rounded corners.

## Filter / Effect Definitions

```svg
<filter id="star-glow" x="-10%" y="-10%" width="120%" height="120%">
  <feGaussianBlur stdDeviation="2" in="SourceGraphic" result="blur"/>
  <feFlood flood-color="#7eb8da" flood-opacity="0.2" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="glow"/>
  <feMerge>
    <feMergeNode in="glow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

This is the only node effect in the sample SVG. Keep it subtle; do not replace it with a heavy blur or shadow.

## Arrow Markers

```svg
<marker id="marker-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#7eb8da"/>
</marker>

<marker id="marker-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#c0a0e0"/>
</marker>

<marker id="marker-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#e8a060"/>
</marker>
```

Note: all markers use the same 7×7 geometry and only differ by fill color.

## Edge Styles

```css
.edge,
.edge-trunk {
  fill: none;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.edge-data { stroke: #7eb8da; marker-end: url(#marker-data); }
.edge-control { stroke: #c0a0e0; marker-end: url(#marker-control); }
.edge-dependency { stroke: #e8a060; stroke-dasharray: 6 4; marker-end: url(#marker-dependency); }
.edge-animated { stroke-dasharray: 8 4; animation: edge-flow 2.5s linear infinite; }
.control-trunk { stroke: #c0a0e0; }
.data-trunk { stroke: #7eb8da; stroke-dasharray: 8 4; animation: edge-flow 2.5s linear infinite; }
.junction-control { fill: #c0a0e0; opacity: 0.85; }
.junction-data { fill: #7eb8da; opacity: 0.85; }
```

Edges stay thin and elegant at 1.5px; the theme relies on color and motion, not stroke weight.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 2.5s, timing: linear, infinite, dasharray: 8 4, dashoffset target: -24 |
| Star twinkle | ✓ | duration: 4s, ease-in-out, infinite, keyframes: opacity 0.7 → 0.3 → 0.7 |
| Twinkle stagger | ✓ | delays: 0s, 0.6s, 1.2s, 1.8s, 2.4s, 3s |
| Hover glow | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✗ | — |

## CSS Variables Block

```css
:root {
  --space-bg-center: #0d1b2a;
  --space-bg-edge: #050a14;
  --nebula-purple: #7850b4;
  --nebula-teal: #50b4c8;
  --nebula-blue: #5f7fd6;
  --star-white: #ffffff;
  --star-ice: #c0d8ff;
  --node-fill: rgba(13,27,42,0.85);
  --node-stroke: #7eb8da;
  --text-title: #ffffff;
  --text-subtitle: #8aacc0;
  --text-primary: #e0e8f0;
  --group-fill: rgba(126,184,218,0.04);
  --group-stroke: rgba(126,184,218,0.25);
  --group-label: #7eb8da;
  --edge-data: #7eb8da;
  --edge-control: #c0a0e0;
  --edge-dependency: #e8a060;
  --legend-fill: rgba(5,10,20,0.9);
  --junction-control: #c0a0e0;
  --junction-data: #7eb8da;
  --edge-flow-duration: 2.5s;
  --twinkle-duration: 4s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --space-bg-center: #0d1b2a;
    --space-bg-edge: #050a14;
    --nebula-purple: #7850b4;
    --nebula-teal: #50b4c8;
    --nebula-blue: #5f7fd6;
    --star-white: #ffffff;
    --star-ice: #c0d8ff;
    --node-fill: rgba(13,27,42,0.85);
    --node-stroke: #7eb8da;
    --text-title: #ffffff;
    --text-subtitle: #8aacc0;
    --text-primary: #e0e8f0;
    --group-fill: rgba(126,184,218,0.04);
    --group-stroke: rgba(126,184,218,0.25);
    --group-label: #7eb8da;
    --edge-data: #7eb8da;
    --edge-control: #c0a0e0;
    --edge-dependency: #e8a060;
    --legend-fill: rgba(5,10,20,0.9);
    --junction-control: #c0a0e0;
    --junction-data: #7eb8da;
    --edge-flow-duration: 2.5s;
    --twinkle-duration: 4s;
  }

  svg {
    font-family: "Inter", "Segoe UI", sans-serif;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 24px;
    font-weight: 300;
    letter-spacing: 3px;
  }

  .diagram-subtitle {
    fill: var(--text-subtitle);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 1.2px;
  }

  .group-box {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 0.5;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.4px;
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 14px;
    font-weight: 600;
  }

  .node-sublabel {
    fill: var(--text-subtitle);
    font-size: 11px;
    font-weight: 400;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1;
    filter: url(#star-glow);
  }

  .edge,
  .edge-trunk {
    fill: none;
    stroke-width: 1.5;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data {
    stroke: var(--edge-data);
    marker-end: url(#marker-data);
  }

  .edge-control {
    stroke: var(--edge-control);
    marker-end: url(#marker-control);
  }

  .edge-dependency {
    stroke: var(--edge-dependency);
    stroke-dasharray: 6 4;
    marker-end: url(#marker-dependency);
  }

  .edge-animated {
    stroke-dasharray: 8 4;
    animation: edge-flow var(--edge-flow-duration) linear infinite;
  }

  .control-trunk {
    stroke: var(--edge-control);
  }

  .data-trunk {
    stroke: var(--edge-data);
    stroke-dasharray: 8 4;
    animation: edge-flow var(--edge-flow-duration) linear infinite;
  }

  .junction-control {
    fill: var(--junction-control);
    opacity: 0.85;
  }

  .junction-data {
    fill: var(--junction-data);
    opacity: 0.85;
  }

  .legend-panel {
    fill: var(--legend-fill);
    stroke: var(--node-stroke);
    stroke-width: 1;
  }

  .legend-title {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.8px;
  }

  .legend-text {
    fill: var(--text-primary);
    font-size: 11px;
    font-weight: 400;
  }

  .star-twinkle {
    animation: twinkle var(--twinkle-duration) ease-in-out infinite;
  }

  .tw1 { animation-delay: 0s; }
  .tw2 { animation-delay: 0.6s; }
  .tw3 { animation-delay: 1.2s; }
  .tw4 { animation-delay: 1.8s; }
  .tw5 { animation-delay: 2.4s; }
  .tw6 { animation-delay: 3s; }

  @keyframes edge-flow {
    to { stroke-dashoffset: -24; }
  }

  @keyframes twinkle {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <radialGradient id="space-bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="#0d1b2a"/>
    <stop offset="100%" stop-color="#050a14"/>
  </radialGradient>

  <radialGradient id="nebula1" cx="20%" cy="25%" r="35%">
    <stop offset="0%" stop-color="#7850b4" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#7850b4" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="nebula2" cx="80%" cy="65%" r="30%">
    <stop offset="0%" stop-color="#50b4c8" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#50b4c8" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="nebula3" cx="34%" cy="82%" r="28%">
    <stop offset="0%" stop-color="#5f7fd6" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#5f7fd6" stop-opacity="0"/>
  </radialGradient>

  <filter id="star-glow" x="-10%" y="-10%" width="120%" height="120%">
    <feGaussianBlur stdDeviation="2" in="SourceGraphic" result="blur"/>
    <feFlood flood-color="#7eb8da" flood-opacity="0.2" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="glow"/>
    <feMerge>
      <feMergeNode in="glow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <marker id="marker-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#7eb8da"/>
  </marker>
  <marker id="marker-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#c0a0e0"/>
  </marker>
  <marker id="marker-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#e8a060"/>
  </marker>
</defs>
```

Use four full-size background rects when generating SVGs:

```svg
<rect x="0" y="0" width="100%" height="100%" fill="url(#space-bg)"/>
<rect x="0" y="0" width="100%" height="100%" fill="url(#nebula1)"/>
<rect x="0" y="0" width="100%" height="100%" fill="url(#nebula2)"/>
<rect x="0" y="0" width="100%" height="100%" fill="url(#nebula3)"/>
```

## Stars & Nebula Background

- The sample SVG uses **37 stars** total: 6 animated twinkle stars (`tw1`-`tw6`) plus 31 static stars.
- Actual star palette is limited to `#ffffff` and `#c0d8ff`; static star opacity ranges from **0.3** to **0.64** and radii range from **0.4** to **0.9**, while twinkle stars use radii **0.9, 1.0, 1.0, 1.1, 1.1, 1.2**.
- Preserve the observed placement strategy: a dense top band (`y=24-78`), a left gutter (`x=24-96`, `y=118-800`), a right gutter (`x=726-790`, `y=110-804`), plus sparse interior corridor stars near `y≈398` and `y≈552`.
- Keep stars in safe zones: outer margins, gaps between group boxes, and open horizontal corridors. Do not place stars inside nodes, over labels, or where markers terminate.
- Nebula layering order is fixed: `nebula1` purple at `cx="20%" cy="25%" r="35%"`, then `nebula2` teal at `cx="80%" cy="65%" r="30%"`, then `nebula3` blue at `cx="34%" cy="82%" r="28%"`.
- Nebula opacity must stay extremely low (`0.08`, `0.06`, `0.05` at center, fading to `0`) so the diagram remains readable. These are color washes, not foreground objects.
- For new diagrams, keep at least 30 stars, preserve asymmetry, and distribute brighter stars as occasional accents rather than evenly spacing them.

## Usage Notes

- Use for architecture maps, orchestration diagrams, memory/agent flows, and other technical visuals that should feel cosmic rather than playful or corporate.
- Keep the background layered: one space gradient plus exactly three subtle nebula washes.
- Node corners should stay soft (`rx="8"`); group containers can be slightly larger (`rx="12"`) but must remain barely visible.
- Group styling is intentionally restrained: `stroke-width: 0.5`, low-opacity fill, no heavy dashed outlines.
- Use stellar blue for nodes and data flow, nebula purple for control links, and warm orange only for dependency links.
- Twinkle should be sparse. The sample animates only six stars; avoid turning the whole background into motion.
- This theme should read as calm, luminous, and spacious.
