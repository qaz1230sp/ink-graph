# Blueprint Style Reference

Use this file as the **source of truth** for the `blueprint` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: precise, measured, and technical. This theme evokes engineering blueprints, architectural drafts, and CAD printouts with deep navy surfaces, crisp white/cyan strokes, monospace typography, subtle grid structure, and restrained motion.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #1e3a5f | SVG background |
| canvas-grid | rgba(224,242,254,0.16) | Grid lines at 40px intervals |
| node-fill | rgba(30,58,95,0.18) | Subtle node fill |
| node-stroke | #e0f2fe | Node border |
| node-stroke-hover | #e0f2fe | Node border on hover (unchanged) |
| text-primary | #f8fafc | Node labels |
| text-secondary | #cfe8f7 | Sublabels, annotations |
| text-title | #ffffff | Diagram title |
| edge-data | #e0f2fe | Data flow edges |
| edge-control | #ffffff | Control flow edges |
| edge-dependency | #bae6fd | Dependency edges |
| edge-async | #7dd3fc | Async edges |
| group-fill | rgba(30,58,95,0.08) | Group background |
| group-stroke | #93c5fd | Group border |
| group-label | #e0f2fe | Group title text |
| accent | #e0f2fe | Primary accent color |

## Typography

font-family: "IBM Plex Mono", "SFMono-Regular", Consolas, monospace
- Title: 20px, font-weight 600, color text-title
- Node label: 13px, font-weight 500, color text-primary
- Sub-label: 11px, font-weight 400, color text-secondary
- Edge label: 11px, font-weight 400, color text-secondary
- Group label: 11px, font-weight 600, text-transform uppercase, letter-spacing 1px, color group-label

## Node Styles

```css
.node-shape {
  fill: rgba(30,58,95,0.18);
  stroke: #e0f2fe;
  stroke-width: 1.5;
  filter: none;
}
```

This theme intentionally avoids hover emphasis, shadows, and lift effects.

## Filter / Effect Definitions

```svg
<pattern id="blueprint-grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(224,242,254,0.16)" stroke-width="1"/>
</pattern>
```

No blur, glow, or shadow filters should be used in this theme.

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#e0f2fe"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffffff"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#bae6fd"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#7dd3fc"/>
</marker>
```

## Edge Styles

```css
.edge-data { stroke: #e0f2fe; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-control { stroke: #ffffff; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #bae6fd; stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #7dd3fc; stroke-width: 1.5; stroke-dasharray: 3,3; marker-end: url(#arrow-async); }
```

Prefer straight or minimally bent connectors so the diagram feels drafted rather than decorative.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 4s, dasharray: 8,4 |
| Hover glow | ✗ | — |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #1e3a5f;
  --canvas-grid: rgba(224,242,254,0.16);
  --node-fill: rgba(30,58,95,0.18);
  --node-stroke: #e0f2fe;
  --node-stroke-hover: #e0f2fe;
  --text-primary: #f8fafc;
  --text-secondary: #cfe8f7;
  --text-title: #ffffff;
  --edge-data: #e0f2fe;
  --edge-control: #ffffff;
  --edge-dependency: #bae6fd;
  --edge-async: #7dd3fc;
  --group-fill: rgba(30,58,95,0.08);
  --group-stroke: #93c5fd;
  --group-label: #e0f2fe;
  --flow-duration: 4s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #1e3a5f;
    --canvas-grid: rgba(224,242,254,0.16);
    --node-fill: rgba(30,58,95,0.18);
    --node-stroke: #e0f2fe;
    --node-stroke-hover: #e0f2fe;
    --text-primary: #f8fafc;
    --text-secondary: #cfe8f7;
    --text-title: #ffffff;
    --edge-data: #e0f2fe;
    --edge-control: #ffffff;
    --edge-dependency: #bae6fd;
    --edge-async: #7dd3fc;
    --group-fill: rgba(30,58,95,0.08);
    --group-stroke: #93c5fd;
    --group-label: #e0f2fe;
    --flow-duration: 4s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "IBM Plex Mono", "SFMono-Regular", Consolas, monospace;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .canvas-grid {
    fill: url(#blueprint-grid);
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 20px;
    font-weight: 600;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    filter: none;
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 13px;
    font-weight: 500;
  }

  .node-sublabel,
  .edge-label {
    fill: var(--text-secondary);
    font-size: 11px;
    font-weight: 400;
  }

  .group-shape {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 1.5;
    stroke-dasharray: 8,4;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: square;
    stroke-linejoin: miter;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 1.5; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 1.5; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 1.5; stroke-dasharray: 3,3; marker-end: url(#arrow-async); }

  .edge-animated {
    stroke-dasharray: 8,4;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <pattern id="blueprint-grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(224,242,254,0.16)" stroke-width="1"/>
  </pattern>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#e0f2fe"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffffff"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#bae6fd"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#7dd3fc"/>
  </marker>
</defs>
```

Use two full-size background rects when generating SVGs:

```svg
<rect class="canvas-bg" x="0" y="0" width="100%" height="100%"/>
<rect class="canvas-grid" x="0" y="0" width="100%" height="100%"/>
```

## Usage Notes

- Use for engineering specs, design docs, architecture drafts, and technical reviews.
- Keep the palette nearly monochrome: white and light-cyan strokes over deep navy.
- Prefer straight routing and evenly spaced alignment to preserve the drafted feel.
- Do not add shadows, hover glow, entrance effects, or pulse.
- This theme should feel like documentation, not a marketing graphic.
