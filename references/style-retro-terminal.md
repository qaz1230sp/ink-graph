# Retro Terminal Style Reference

Use this file as the **source of truth** for the `retro-terminal` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: classic CRT terminal. This theme uses a near-black canvas, phosphor green primary strokes and text, dimmer green secondary text and control edges, amber dependency wiring, scanline texture, faint text glow, subtle CRT flicker, sharp corners, and a flat no-shadow rendering style.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #0a0a0a | Near-black CRT background |
| node-fill | #0a0a0a | Node interior fill |
| node-stroke | #00ff41 | Primary phosphor green node border |
| text-primary | #00ff41 | Primary labels and legend text |
| text-secondary | #00cc33 | Secondary labels, subtitle, control edges |
| text-title | #00ff41 | Main title |
| edge-data | #00ff41 | Data flow edges |
| edge-control | #00cc33 | Control flow edges |
| edge-dependency | #ffaa00 | Dependency / warning edges |
| group-fill | rgba(0,255,65,0.04) | Faint grouped region fill |
| group-stroke | #00ff41 | Group outlines and dividers |
| group-label | #00ff41 | Group heading text |
| legend-panel | rgba(10,10,10,0.92) | Legend panel background |
| scanline-stroke | #00ff41 | Scanline overlay line color |
| scanline-opacity | 0.03 | Scanline line opacity |

## Typography

font-family: "IBM Plex Mono", "Courier New", monospace
- Title: 22px, font-weight 700, color text-title, letter-spacing 1.8px, text-transform uppercase, filter `url(#text-glow)`
- Subtitle: 12px, color text-secondary, letter-spacing 1.2px, filter `url(#text-glow)`
- Node label: 13px, font-weight 600, color text-primary, filter `url(#text-glow)`
- Sub-label: 11px, color text-secondary, filter `url(#text-glow)`
- Group label: 11px, font-weight 700, text-transform uppercase, letter-spacing 1.2px, color group-label, filter `url(#text-glow)`
- Legend title: 12px, font-weight 700, color text-primary, filter `url(#text-glow)`
- Legend text: 11px, color text-primary, filter `url(#text-glow)`

## Node Styles

```css
.node-shape {
  fill: #0a0a0a;
  stroke: #00ff41;
  stroke-width: 1.5;
  animation: crt-flicker 3s ease-in-out infinite;
}
```

Nodes use sharp CRT corners (`rx="2"` in the sample), flat fills, no drop shadow, and only a subtle opacity flicker for motion.

## Filter / Effect Definitions

```svg
<!-- Scanline pattern for CRT texture -->
<pattern id="scanlines" width="820" height="4" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0.5" x2="820" y2="0.5" stroke="#00ff41" stroke-opacity="0.03" stroke-width="1"/>
</pattern>

<!-- Faint green text glow -->
<filter id="text-glow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="1" in="SourceGraphic" result="blur"/>
  <feMerge>
    <feMergeNode in="blur"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00ff41"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00cc33"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffaa00"/>
</marker>
```

Note: markers use the standard 6×6 size with the same triangle path for all edge types.

## Edge Styles

```css
.edge-data,
.edge-control,
.edge-dependency {
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.edge-control { stroke: #00cc33; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-data { stroke: #00ff41; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-dependency { stroke: #ffaa00; stroke-width: 1.5; stroke-dasharray: 10 6; marker-end: url(#arrow-dependency); }
.edge-animated { stroke-dasharray: 8 4; animation: cg-edge-flow 2s linear infinite; }
```

Edges stay thin and crisp for terminal clarity. Data edges animate, control edges stay static, and dependency edges use longer amber dashes.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 2s, dasharray: 8 4, keyframe dashoffset: -24 |
| CRT flicker | ✓ | duration: 3s, ease-in-out, infinite, opacity 1 → 0.92 → 1 |
| Hover glow | ✗ | — |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #0a0a0a;
  --node-fill: #0a0a0a;
  --node-stroke: #00ff41;
  --text-primary: #00ff41;
  --text-secondary: #00cc33;
  --text-title: #00ff41;
  --edge-data: #00ff41;
  --edge-control: #00cc33;
  --edge-dependency: #ffaa00;
  --group-fill: rgba(0,255,65,0.04);
  --group-stroke: #00ff41;
  --group-label: #00ff41;
  --flow-duration: 2s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #0a0a0a;
    --node-fill: #0a0a0a;
    --node-stroke: #00ff41;
    --text-primary: #00ff41;
    --text-secondary: #00cc33;
    --text-title: #00ff41;
    --edge-data: #00ff41;
    --edge-control: #00cc33;
    --edge-dependency: #ffaa00;
    --group-fill: rgba(0,255,65,0.04);
    --group-stroke: #00ff41;
    --group-label: #00ff41;
    --flow-duration: 2s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "IBM Plex Mono", "Courier New", monospace;
    shape-rendering: geometricPrecision;
    text-rendering: geometricPrecision;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    filter: url(#text-glow);
  }

  .subtitle {
    fill: var(--text-secondary);
    font-size: 12px;
    letter-spacing: 1.2px;
    filter: url(#text-glow);
  }

  .group-shape {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 1.5;
    stroke-dasharray: 6 4;
  }

  .group-divider {
    stroke: var(--group-stroke);
    stroke-width: 1;
    stroke-dasharray: 6 4;
    opacity: 0.75;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    filter: url(#text-glow);
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    animation: crt-flicker 3s ease-in-out infinite;
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 13px;
    font-weight: 600;
    filter: url(#text-glow);
  }

  .node-sublabel {
    fill: var(--text-secondary);
    font-size: 11px;
    filter: url(#text-glow);
  }

  .edge-control,
  .edge-data,
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
    stroke-dasharray: 10 6;
    marker-end: url(#arrow-dependency);
  }

  .edge-animated {
    stroke-dasharray: 8 4;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  .edge-no-marker {
    marker-start: none;
    marker-end: none;
  }

  .edge-bidirectional {
    marker-start: url(#arrow-dependency);
    marker-end: url(#arrow-dependency);
  }

  .junction-control {
    fill: var(--edge-control);
  }

  .junction-data {
    fill: var(--edge-data);
  }

  .legend-panel {
    fill: rgba(10,10,10,0.92);
    stroke: var(--group-stroke);
    stroke-width: 1;
  }

  .legend-title {
    fill: var(--text-primary);
    font-size: 12px;
    font-weight: 700;
    filter: url(#text-glow);
  }

  .legend-text {
    fill: var(--text-primary);
    font-size: 11px;
    filter: url(#text-glow);
  }

  .scanline-overlay {
    fill: url(#scanlines);
    pointer-events: none;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }

  @keyframes crt-flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.92; }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <pattern id="scanlines" width="820" height="4" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0.5" x2="820" y2="0.5" stroke="#00ff41" stroke-opacity="0.03" stroke-width="1"/>
  </pattern>
  <filter id="text-glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="1" in="SourceGraphic" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00ff41"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00cc33"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffaa00"/>
  </marker>
</defs>
```

Use two full-canvas background rects when generating SVGs. In the sample SVG these were sized to the 820×840 canvas:

```svg
<rect class="canvas-bg" x="0" y="0" width="820" height="840"/>
<rect class="scanline-overlay" x="0" y="0" width="820" height="840"/>
```

## Usage Notes

- Keep the look flat and terminal-like: no drop shadows, no glossy fills, no rounded comic-style corners.
- Use `rx="2"` for nodes and `rx="4"` for enclosing group panels to preserve the sample geometry.
- Apply `filter="url(#text-glow)"` to text elements, not node rectangles.
- Place the scanline overlay as the final full-canvas rect so it sits over the entire diagram.
- Use phosphor green for primary content, dimmer green for secondary/control content, and amber only for dependency/warning semantics.
- Preserve `shape-rendering: geometricPrecision` and `text-rendering: geometricPrecision` for the crisp CRT feel.
