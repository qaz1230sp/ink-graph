# Papercraft Style Reference

Use this file as the **source of truth** for the `papercraft` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: warm, handmade, and tactile. This theme evokes layered paper cutouts, card-stock shapes, soft shadows, subtle texture, and handwritten labeling with gentle motion rather than sharp contrast.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #faf6f0 | Warm cream background |
| canvas-texture | #f0e8dc | Subtle paper texture overlay fill |
| text-primary | #4a4a4a | Main node labels and legend text |
| text-secondary | #7a7a7a | Sublabels and subtitle text |
| text-title | #3a3a3a | Diagram title |
| edge-data | #5c8a97 | Teal data flow edges |
| edge-control | #7a7a7a | Gray control flow edges |
| edge-dependency | #c0735e | Brown dependency edges and junction pins |
| group-stroke | #c0c0c0 | Dashed group outlines and dividers |
| group-label | #5a5a5a | Group headings and legend title |
| node-orch-fill | #b8d4e3 | Orchestration group node fill (light blue card-stock) |
| node-core-fill | #c8e6c9 | Agent Core group node fill (light green card-stock) |
| node-exec-fill | #ffe0b2 | Execution group node fill (light orange card-stock) |
| tape-fill | rgba(255,255,255,0.48) | Decorative masking-tape accent fill |
| tape-stroke | rgba(192,192,192,0.35) | Decorative masking-tape accent stroke |
| legend-panel | rgba(250,246,240,0.92) | Legend panel background |
| shadow-color | #000000 @ 0.12 opacity | Soft paper shadow filter flood color |

## Typography

font-family: "Patrick Hand", "Comic Neue", "Segoe Print", cursive
- Title: 22px, font-weight 700, color text-title, letter-spacing 0.4px
- Subtitle: 12px, font-weight 500, color text-secondary
- Node label: 14px, font-weight 700, color text-primary
- Sub-label: 12px, font-weight 500, color text-secondary
- Group label: 12px, font-weight 700, letter-spacing 1px, color group-label
- Legend title: 12px, font-weight 700, color group-label
- Legend text: 11px, font-weight 500, color text-primary

## Node Styles

```css
.node-shape {
  stroke: none;
  filter: url(#paper-shadow);
}

.node-orch .node-shape { fill: #b8d4e3; }
.node-core .node-shape { fill: #c8e6c9; }
.node-exec .node-shape { fill: #ffe0b2; }
```

Nodes have no hard outlines. The signature look is the group-based card-stock fill system plus a soft paper shadow; use rounded corners (`rx="8"`) on node rects.

## Filter / Effect Definitions

```svg
<!-- Soft paper shadow -->
<filter id="paper-shadow" x="-5%" y="-5%" width="115%" height="120%">
  <feGaussianBlur stdDeviation="2" in="SourceAlpha" result="blur"/>
  <feOffset dx="2" dy="3" result="offset"/>
  <feFlood flood-color="#000000" flood-opacity="0.12" result="color"/>
  <feComposite in="color" in2="offset" operator="in" result="shadow"/>
  <feMerge>
    <feMergeNode in="shadow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<!-- Subtle paper grain / texture -->
<filter id="paper-texture" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="4" result="noise"/>
  <feColorMatrix type="saturate" values="0" in="noise" result="gray"/>
  <feBlend in="SourceGraphic" in2="gray" mode="multiply" result="textured"/>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#5c8a97"/>
</marker>

<marker id="arrow-control" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#7a7a7a"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#c0735e"/>
</marker>
```

Note: markers use a compact 6×6 format with a curved handmade arrowhead silhouette.

## Edge Styles

```css
.edge-data,
.edge-control,
.edge-dependency {
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.edge-control { stroke: #7a7a7a; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-data { stroke: #5c8a97; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-dependency { stroke: #c0735e; stroke-width: 1.5; stroke-dasharray: 7 5; marker-end: url(#arrow-dependency); }
```

Edges stay light and hand-drawn rather than bold; animated data edges add motion without overpowering the paper cutout aesthetic.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 3s, dasharray: 8 4, stroke-dashoffset: -24 |
| Hover glow | ✗ | — |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #faf6f0;
  --text-primary: #4a4a4a;
  --text-secondary: #7a7a7a;
  --text-title: #3a3a3a;
  --edge-data: #5c8a97;
  --edge-control: #7a7a7a;
  --edge-dependency: #c0735e;
  --group-stroke: #c0c0c0;
  --group-label: #5a5a5a;
  --flow-duration: 3s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #faf6f0;
    --text-primary: #4a4a4a;
    --text-secondary: #7a7a7a;
    --text-title: #3a3a3a;
    --edge-data: #5c8a97;
    --edge-control: #7a7a7a;
    --edge-dependency: #c0735e;
    --group-stroke: #c0c0c0;
    --group-label: #5a5a5a;
    --flow-duration: 3s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "Patrick Hand", "Comic Neue", "Segoe Print", cursive;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .canvas-texture {
    fill: #f0e8dc;
    opacity: 0.1;
    filter: url(#paper-texture);
    pointer-events: none;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.4px;
  }

  .subtitle {
    fill: var(--text-secondary);
    font-size: 12px;
    font-weight: 500;
  }

  .group-shape {
    fill: transparent;
    stroke: var(--group-stroke);
    stroke-width: 1.4;
    stroke-dasharray: 6 5;
  }

  .group-divider {
    stroke: var(--group-stroke);
    stroke-width: 1;
    stroke-dasharray: 4 6;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .tape {
    fill: rgba(255,255,255,0.48);
    stroke: rgba(192,192,192,0.35);
    stroke-width: 1;
  }

  .node-shape {
    stroke: none;
    filter: url(#paper-shadow);
  }

  .node-orch .node-shape { fill: #b8d4e3; }
  .node-core .node-shape { fill: #c8e6c9; }
  .node-exec .node-shape { fill: #ffe0b2; }

  .node-label {
    fill: var(--text-primary);
    font-size: 14px;
    font-weight: 700;
  }

  .node-sublabel {
    fill: var(--text-secondary);
    font-size: 12px;
    font-weight: 500;
  }

  .edge-data,
  .edge-control,
  .edge-dependency {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-control {
    stroke: var(--edge-control);
    stroke-width: 1.5;
    marker-end: url(#arrow-control);
  }

  .edge-data {
    stroke: var(--edge-data);
    stroke-width: 1.5;
    marker-end: url(#arrow-data);
  }

  .edge-dependency {
    stroke: var(--edge-dependency);
    stroke-width: 1.5;
    stroke-dasharray: 7 5;
    marker-end: url(#arrow-dependency);
  }

  .edge-no-marker {
    marker-end: none;
  }

  .edge-bidirectional {
    marker-start: url(#arrow-dependency);
  }

  .edge-animated {
    stroke-dasharray: 8 4;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }

  .junction-pin {
    fill: var(--edge-dependency);
  }

  .legend-panel {
    fill: rgba(250,246,240,0.92);
    stroke: var(--group-stroke);
    stroke-width: 1;
  }

  .legend-title {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 700;
  }

  .legend-text {
    fill: var(--text-primary);
    font-size: 11px;
    font-weight: 500;
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <filter id="paper-shadow" x="-5%" y="-5%" width="115%" height="120%">
    <feGaussianBlur stdDeviation="2" in="SourceAlpha" result="blur"/>
    <feOffset dx="2" dy="3" result="offset"/>
    <feFlood flood-color="#000000" flood-opacity="0.12" result="color"/>
    <feComposite in="color" in2="offset" operator="in" result="shadow"/>
    <feMerge>
      <feMergeNode in="shadow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <filter id="paper-texture" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="4" result="noise"/>
    <feColorMatrix type="saturate" values="0" in="noise" result="gray"/>
    <feBlend in="SourceGraphic" in2="gray" mode="multiply" result="textured"/>
  </filter>

  <marker id="arrow-data" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#5c8a97"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#7a7a7a"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0.8 0.6 Q 1.5 0.8 4.8 3 Q 1.5 5.2 0.8 5.4 Q 1.9 3 0.8 0.6 Z" fill="#c0735e"/>
  </marker>
</defs>
```

Use two full-size background rects when generating SVGs:

```svg
<rect class="canvas-bg" x="0" y="0" width="100%" height="100%"/>
<rect class="canvas-texture" x="0" y="0" width="100%" height="100%"/>
```

## Usage Notes

- Use for handmade architecture diagrams, craft-inspired presentations, learning visuals, and friendly system overviews.
- Keep the warm paper base (`#faf6f0`) and the group-specific node fills: orchestration `#b8d4e3`, agent core `#c8e6c9`, execution `#ffe0b2`.
- Do not add hard node outlines; the soft paper shadow is the signature depth treatment.
- Keep node corners gently rounded (`rx=8`) and group containers more rounded (`rx=18`) for the cut-paper feel.
- Preserve the subtle paper texture overlay and optional tape accents for tactile warmth.
- Edge animation should stay gentle at 3s with `8 4` dashes; this theme should feel calm and handmade, not high-energy.
- Control edges are plain gray, data edges are teal, and dependency edges are brown dashed links; keep those semantics consistent.
