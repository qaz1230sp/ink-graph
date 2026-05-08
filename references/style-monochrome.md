# Monochrome Style Reference

Use this file as the **source of truth** for the `monochrome` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: formal, print-ready, and institutional. This theme is optimized for academic papers, compliance docs, PDF export, grayscale printing, and any context where clarity and reproduction matter more than visual flair.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #ffffff | SVG background |
| node-fill | #ffffff | Node background |
| node-stroke | #1f2937 | Node border |
| text-primary | #111827 | Node labels |
| text-secondary | #374151 | Sublabels, annotations |
| text-title | #111827 | Diagram title |
| edge-data | #374151 | Data flow edges |
| edge-control | #374151 | Control flow edges |
| edge-dependency | #374151 | Dependency edges |
| edge-async | #374151 | Async edges |
| group-fill | #ffffff | Group background |
| group-stroke | #9ca3af | Group border |
| group-label | #374151 | Group title text |
| accent | #111827 | Primary emphasis |

## Typography

font-family: Georgia, Cambria, "Times New Roman", serif
- Title: 22px, font-weight 700, color text-title
- Node label: 14px, font-weight 600, color text-primary
- Sub-label: 12px, font-weight 400, color text-secondary
- Edge label: 12px, font-weight 400, color text-secondary
- Group label: 12px, font-weight 700, letter-spacing 0.3px, color group-label

## Node Styles

```css
.node-shape {
  fill: #ffffff;
  stroke: #1f2937;
  stroke-width: 1.5;
  filter: none;
}
```

Use plain geometry only. No glow, gradients, shadow, or decorative effects.

## Filter / Effect Definitions

This theme intentionally uses no filters or gradients.

```svg
<!-- No filters, gradients, or effects for monochrome output. -->
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
</marker>
```

## Edge Styles

```css
.edge-data { stroke: #374151; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-control { stroke: #374151; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #374151; stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #374151; stroke-width: 1.5; stroke-dasharray: 2,3; marker-end: url(#arrow-async); }
```

All semantic differentiation should come from line pattern and labels, not color.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✗ | — |
| Hover glow | ✗ | — |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #ffffff;
  --node-fill: #ffffff;
  --node-stroke: #1f2937;
  --text-primary: #111827;
  --text-secondary: #374151;
  --text-title: #111827;
  --edge-data: #374151;
  --edge-control: #374151;
  --edge-dependency: #374151;
  --edge-async: #374151;
  --group-fill: #ffffff;
  --group-stroke: #9ca3af;
  --group-label: #374151;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #ffffff;
    --node-fill: #ffffff;
    --node-stroke: #1f2937;
    --text-primary: #111827;
    --text-secondary: #374151;
    --text-title: #111827;
    --edge-data: #374151;
    --edge-control: #374151;
    --edge-dependency: #374151;
    --edge-async: #374151;
    --group-fill: #ffffff;
    --group-stroke: #9ca3af;
    --group-label: #374151;
  }

  svg {
    background: var(--canvas-bg);
    font-family: Georgia, Cambria, "Times New Roman", serif;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 700;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    filter: none;
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 14px;
    font-weight: 600;
  }

  .node-sublabel,
  .edge-label {
    fill: var(--text-secondary);
    font-size: 12px;
    font-weight: 400;
  }

  .group-shape {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 1.2;
    stroke-dasharray: 5,3;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: butt;
    stroke-linejoin: miter;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 1.5; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 1.5; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 1.5; stroke-dasharray: 2,3; marker-end: url(#arrow-async); }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#111827"/>
  </marker>
</defs>
```

## Usage Notes

- Use for formal documents, print output, grayscale export, compliance packs, and academic diagrams.
- Never use animation, glow, hover effects, gradients, or shadows.
- Keep linework crisp and depend on dash patterns plus labels for semantics.
- This is the safest auto-choice for PDF or print targets.
- Prefer simple geometry and conservative spacing over decorative layout.
