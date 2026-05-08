# Warm Minimal Style Reference

Use this file as the **source of truth** for the `warm-minimal` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: friendly, inviting, and quietly polished. This theme draws from warm editorial layouts, approachable product docs, and cozy note-taking tools with cream surfaces, soft peach borders, rounded geometry, and gentle orange emphasis.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #fffbf5 | SVG background |
| node-fill | #fff7ed | Node background |
| node-stroke | #fed7aa | Node border |
| node-stroke-hover | #fb923c | Node border on hover |
| text-primary | #92400e | Node labels |
| text-secondary | #b45309 | Sublabels, annotations |
| text-title | #78350f | Diagram title |
| edge-data | #fb923c | Data flow edges |
| edge-control | #92400e | Control flow edges |
| edge-dependency | #d4a574 | Dependency edges |
| edge-async | #c084fc | Async edges |
| group-fill | rgba(255,247,237,0.9) | Group background |
| group-stroke | #fed7aa | Group border |
| group-label | #b45309 | Group title text |
| accent | #f97316 | Primary accent color |
| shadow | rgba(249,115,22,0.12) | Warm drop shadow |
| hover-glow | rgba(249,115,22,0.35) | Hover glow color |

## Typography

font-family: "Nunito", "Quicksand", "Avenir Next", "Segoe UI", sans-serif
- Title: 22px, font-weight 700, color text-title
- Node label: 14px, font-weight 600, color text-primary
- Sub-label: 12px, font-weight 500, color text-secondary
- Edge label: 12px, font-weight 500, color text-secondary
- Group label: 12px, font-weight 700, letter-spacing 0.4px, color group-label

## Node Styles

```css
.node-shape {
  fill: #fff7ed;
  stroke: #fed7aa;
  stroke-width: 1.5;
  filter: url(#shadow-warm);
}
```

Use rounded rectangles with `rx="16" ry="16"` for the primary node shape.

## Filter / Effect Definitions

```svg
<filter id="shadow-warm" x="-15%" y="-15%" width="130%" height="140%">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="rgba(249,115,22,0.12)" flood-opacity="1"/>
</filter>
```

Optional hover refinement for interactive SVGs:

```css
.node:hover .node-shape {
  stroke: #fb923c;
  filter: url(#shadow-warm) drop-shadow(0 0 6px rgba(249,115,22,0.35));
}
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#fb923c"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#92400e"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#d4a574"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#c084fc"/>
</marker>
```

## Edge Styles

```css
.edge-data { stroke: #fb923c; stroke-width: 1.6; marker-end: url(#arrow-data); }
.edge-control { stroke: #92400e; stroke-width: 1.6; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #d4a574; stroke-width: 1.6; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #c084fc; stroke-width: 1.6; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }
```

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 2.5s, dasharray: 8,4 |
| Hover glow | ✓ | radius: 6px, color: rgba(249,115,22,0.35) |
| Hover lift | ✗ | — |
| Entrance | ✗ | — |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #fffbf5;
  --node-fill: #fff7ed;
  --node-stroke: #fed7aa;
  --node-stroke-hover: #fb923c;
  --text-primary: #92400e;
  --text-secondary: #b45309;
  --text-title: #78350f;
  --edge-data: #fb923c;
  --edge-control: #92400e;
  --edge-dependency: #d4a574;
  --edge-async: #c084fc;
  --group-fill: rgba(255,247,237,0.9);
  --group-stroke: #fed7aa;
  --group-label: #b45309;
  --accent: #f97316;
  --shadow-color: rgba(249,115,22,0.12);
  --hover-glow-color: rgba(249,115,22,0.35);
  --hover-glow-radius: 6px;
  --flow-duration: 2.5s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #fffbf5;
    --node-fill: #fff7ed;
    --node-stroke: #fed7aa;
    --node-stroke-hover: #fb923c;
    --text-primary: #92400e;
    --text-secondary: #b45309;
    --text-title: #78350f;
    --edge-data: #fb923c;
    --edge-control: #92400e;
    --edge-dependency: #d4a574;
    --edge-async: #c084fc;
    --group-fill: rgba(255,247,237,0.9);
    --group-stroke: #fed7aa;
    --group-label: #b45309;
    --accent: #f97316;
    --shadow-color: rgba(249,115,22,0.12);
    --hover-glow-color: rgba(249,115,22,0.35);
    --hover-glow-radius: 6px;
    --flow-duration: 2.5s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "Nunito", "Quicksand", "Avenir Next", "Segoe UI", sans-serif;
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
    filter: url(#shadow-warm);
    transition: stroke 0.25s ease, filter 0.25s ease;
  }

  .node:hover .node-shape {
    stroke: var(--node-stroke-hover);
    filter: url(#shadow-warm) drop-shadow(0 0 var(--hover-glow-radius) var(--hover-glow-color));
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
    font-weight: 500;
  }

  .group-shape {
    fill: var(--group-fill);
    stroke: var(--group-stroke);
    stroke-width: 1.5;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.4px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 1.6; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 1.6; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 1.6; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 1.6; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }

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
  <filter id="shadow-warm" x="-15%" y="-15%" width="130%" height="140%">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="rgba(249,115,22,0.12)" flood-opacity="1"/>
  </filter>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#fb923c"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#92400e"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#d4a574"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#c084fc"/>
  </marker>
</defs>
```

## Usage Notes

- Use for blog explainers, product docs, walkthroughs, onboarding diagrams, and friendly internal communication.
- Keep the mood warm and approachable: soft cream surfaces, peach borders, brown text.
- Use large-radius rectangles (`rx="16" ry="16"`) for most nodes.
- Motion should stay calm: flowing edges plus a small warm hover glow only.
- Avoid entrance effects, heavy contrast, or aggressive neon accents.
