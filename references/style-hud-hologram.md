# HUD Hologram Style Reference

Use this file as the **source of truth** for the `hud-hologram` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: tactical HUD, hologram, and helmet-display aesthetics. This theme uses a near-black blue-tinted canvas, cyan-forward typography and nodes, scanline overlays, thin military UI strokes, sharp corners, and subtle pulse/flow animation to evoke an always-online command interface.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #0a0e17 | Near-black blue-tinted background |
| node-fill | rgba(0,200,255,0.06) | Hologram node fill |
| node-stroke | #00c8ff | Primary cyan node stroke, brackets, crosshair |
| text-primary | #00c8ff | Primary labels, legend, status text |
| text-secondary | #0090bb | Sublabels and subtitle text |
| text-title | #00c8ff | Diagram title |
| edge-data | #00c8ff | Data edges and data junctions |
| edge-control | #00ff88 | Control edges and control junctions |
| edge-dependency | #ff6040 | Dependency / warning edges |
| group-fill | rgba(0,200,255,0.03) | Group container fill |
| group-stroke | rgba(0,200,255,0.4) | Group borders, dividers, legend stroke |
| group-label | #00c8ff | Group title text |
| legend-bg | rgba(10,14,23,0.9) | Legend panel background |
| scanline-stroke | #00c8ff @ 0.02 opacity | Scanline overlay line color |
| glow-flood | #00c8ff @ 0.3 opacity | HUD glow filter flood color |
| group-title-bar | rgba(0,200,255,0.05) | Optional section title bar fill |

## Typography

font-family: "IBM Plex Mono", "Consolas", monospace
- Global text rule: text-transform uppercase
- Title: 22px, font-weight 700, color text-title, letter-spacing 6px
- Subtitle: 12px, color text-secondary, letter-spacing 3px
- Node label: 13px, font-weight 700, color text-primary, letter-spacing 1px
- Sub-label: 11px, color text-secondary, letter-spacing 1px
- Group label: 11px, font-weight 700, color group-label, letter-spacing 2px
- Status text: 9px, color text-primary, letter-spacing 2px, opacity 0.4
- Legend title: 12px, font-weight 700, color text-primary, letter-spacing 2px
- Legend text: 11px, color text-primary, letter-spacing 1px

## Node Styles

```css
.node-shape {
  fill: var(--node-fill);
  stroke: var(--node-stroke);
  stroke-width: 1.5;
  filter: url(#hud-glow);
  animation: hud-pulse 2.5s ease-in-out infinite;
}

.node-accent {
  fill: none;
  stroke: var(--node-stroke);
  stroke-width: 1;
  opacity: 0.35;
}
```

Nodes use sharp military corners (`rx="2"`) with a cyan glow and subtle opacity flicker to simulate HUD refresh.

## Filter / Effect Definitions

```svg
<!-- Scanline overlay pattern -->
<pattern id="hud-scanlines" x="0" y="0" width="820" height="2" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="820" y2="0" stroke="#00c8ff" stroke-opacity="0.02" stroke-width="1"/>
</pattern>

<!-- Cyan hologram glow -->
<filter id="hud-glow" x="-15%" y="-15%" width="130%" height="130%">
  <feGaussianBlur stdDeviation="2" in="SourceGraphic" result="blur"/>
  <feFlood flood-color="#00c8ff" flood-opacity="0.3" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="glow"/>
  <feMerge>
    <feMergeNode in="glow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 6 3 L 0 6 Z" fill="#00c8ff"/>
</marker>

<marker id="arrow-control" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 6 3 L 0 6 Z" fill="#00ff88"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ff6040"/>
</marker>
```

Note: markers use the compact 6×6 HUD geometry with `refX="5.2"` and `refY="3"`.

## Edge Styles

```css
.edge-data,
.edge-control,
.edge-dependency {
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.edge-data {
  stroke: var(--edge-data);
  stroke-width: 1.5;
  marker-end: url(#arrow-data);
}

.edge-control {
  stroke: var(--edge-control);
  stroke-width: 1.5;
  marker-end: url(#arrow-control);
}

.edge-dependency {
  stroke: var(--edge-dependency);
  stroke-width: 1.5;
  stroke-dasharray: 8 4;
  marker-end: url(#arrow-dependency);
}

.edge-animated {
  stroke-dasharray: 8 4;
  animation: cg-edge-flow 2s linear infinite;
}

.edge-no-marker {
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
```

Edges stay thin and precise, with green control lines, cyan animated data flow, and orange-red bidirectional dependency warnings.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 2s, stroke-dasharray: 8 4, dashoffset: -24, linear infinite |
| Hover glow | ✗ | — |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✓ | `hud-pulse`, duration: 2.5s, ease-in-out infinite, opacity: 1 → 0.88 → 1 |
| Edge glow | ✓ | always-on `hud-glow` filter, blur: 2, flood-opacity: 0.3 |

## CSS Variables Block

```css
:root {
  --canvas-bg: #0a0e17;
  --node-fill: rgba(0,200,255,0.06);
  --node-stroke: #00c8ff;
  --text-primary: #00c8ff;
  --text-secondary: #0090bb;
  --text-title: #00c8ff;
  --edge-data: #00c8ff;
  --edge-control: #00ff88;
  --edge-dependency: #ff6040;
  --group-fill: rgba(0,200,255,0.03);
  --group-stroke: rgba(0,200,255,0.4);
  --group-label: #00c8ff;
  --legend-bg: rgba(10,14,23,0.9);
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #0a0e17;
    --node-fill: rgba(0,200,255,0.06);
    --node-stroke: #00c8ff;
    --text-primary: #00c8ff;
    --text-secondary: #0090bb;
    --text-title: #00c8ff;
    --edge-data: #00c8ff;
    --edge-control: #00ff88;
    --edge-dependency: #ff6040;
    --group-fill: rgba(0,200,255,0.03);
    --group-stroke: rgba(0,200,255,0.4);
    --group-label: #00c8ff;
    --legend-bg: rgba(10,14,23,0.9);
  }

  svg {
    background: var(--canvas-bg);
    font-family: "IBM Plex Mono", "Consolas", monospace;
    shape-rendering: geometricPrecision;
    text-rendering: geometricPrecision;
  }

  text {
    text-transform: uppercase;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .group-shape {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 1;
    stroke-dasharray: 6 4;
  }

  .group-divider {
    stroke: var(--group-stroke);
    stroke-width: 1;
    stroke-dasharray: 6 4;
    opacity: 0.65;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    filter: url(#hud-glow);
    animation: hud-pulse 2.5s ease-in-out infinite;
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .node-sublabel {
    fill: var(--text-secondary);
    font-size: 11px;
    letter-spacing: 1px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data {
    stroke: var(--edge-data);
    stroke-width: 1.5;
    marker-end: url(#arrow-data);
  }

  .edge-control {
    stroke: var(--edge-control);
    stroke-width: 1.5;
    marker-end: url(#arrow-control);
  }

  .edge-dependency {
    stroke: var(--edge-dependency);
    stroke-width: 1.5;
    stroke-dasharray: 8 4;
    marker-end: url(#arrow-dependency);
  }

  .edge-animated {
    stroke-dasharray: 8 4;
    animation: cg-edge-flow 2s linear infinite;
  }

  .edge-no-marker {
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

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 6px;
  }

  .subtitle {
    fill: var(--text-secondary);
    font-size: 12px;
    letter-spacing: 3px;
  }

  .status-text {
    fill: var(--text-primary);
    font-size: 9px;
    letter-spacing: 2px;
    opacity: 0.4;
  }

  .hud-bracket line,
  .crosshair line,
  .crosshair circle {
    stroke: var(--node-stroke);
    stroke-width: 1;
    fill: none;
  }

  .crosshair {
    opacity: 0.3;
  }

  .legend-panel {
    fill: var(--legend-bg);
    stroke: var(--group-stroke);
    stroke-width: 1;
  }

  .legend-title {
    fill: var(--text-primary);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
  }

  .legend-text {
    fill: var(--text-primary);
    font-size: 11px;
    letter-spacing: 1px;
  }

  .scanline-overlay {
    fill: url(#hud-scanlines);
    pointer-events: none;
  }

  .node-accent {
    fill: none;
    stroke: var(--node-stroke);
    stroke-width: 1;
    opacity: 0.35;
  }

  .group-title-bar {
    fill: rgba(0,200,255,0.05);
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }

  @keyframes hud-pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.88; }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <pattern id="hud-scanlines" x="0" y="0" width="820" height="2" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="820" y2="0" stroke="#00c8ff" stroke-opacity="0.02" stroke-width="1"/>
  </pattern>
  <filter id="hud-glow" x="-15%" y="-15%" width="130%" height="130%">
    <feGaussianBlur stdDeviation="2" in="SourceGraphic" result="blur"/>
    <feFlood flood-color="#00c8ff" flood-opacity="0.3" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="glow"/>
    <feMerge>
      <feMergeNode in="glow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <marker id="arrow-data" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 6 3 L 0 6 Z" fill="#00c8ff"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 6 3 L 0 6 Z" fill="#00ff88"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 6 6" refX="5.2" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ff6040"/>
  </marker>
</defs>
```

Use these two full-size background rects in the HUD composition layer from the source SVG:

```svg
<rect class="canvas-bg" x="0" y="0" width="820" height="840"/>
<rect class="scanline-overlay" x="0" y="0" width="820" height="840"/>
```

## Usage Notes

- Use for tactical dashboards, system architecture diagrams, AI orchestration maps, and security/control-room visuals.
- Keep the palette restrained: cyan for nodes and data, green for healthy control paths, orange-red for dependencies or warnings.
- Preserve sharp corners (`rx="2"`) on nodes for the military precision feel.
- The scanline overlay is part of the identity, not an optional flourish.
- The cyan glow should stay subtle; it should read as projected glass, not neon signage.
- Decorative brackets, crosshair, and `STATUS: ONLINE` text are key theme cues and should remain light-weight and low-opacity.
- Prefer thin 1px–1.5px strokes and precise spacing over chunky cyberpunk styling.

## HUD Decorations

These decorative elements are essential to the theme and should be carried into generated SVGs when space allows.

### Corner Brackets

```svg
<g class="hud-bracket" opacity="0.5">
  <line x1="12" y1="12" x2="32" y2="12"/>
  <line x1="12" y1="12" x2="12" y2="32"/>
</g>
<g class="hud-bracket" opacity="0.5">
  <line x1="808" y1="12" x2="788" y2="12"/>
  <line x1="808" y1="12" x2="808" y2="32"/>
</g>
<g class="hud-bracket" opacity="0.5">
  <line x1="12" y1="828" x2="32" y2="828"/>
  <line x1="12" y1="828" x2="12" y2="808"/>
</g>
<g class="hud-bracket" opacity="0.5">
  <line x1="808" y1="828" x2="788" y2="828"/>
  <line x1="808" y1="828" x2="808" y2="808"/>
</g>
```

### Status Text

```svg
<text x="790" y="24" text-anchor="end" class="status-text">STATUS: ONLINE</text>
```

### Crosshair

```svg
<g class="crosshair">
  <circle cx="268" cy="28" r="3"/>
  <line x1="262" y1="28" x2="274" y2="28"/>
  <line x1="268" y1="22" x2="268" y2="34"/>
</g>
```

Use brackets to frame the canvas, place status text near the top edge, and keep the crosshair subtle (`opacity: 0.3`) so it reads as instrumentation rather than content.