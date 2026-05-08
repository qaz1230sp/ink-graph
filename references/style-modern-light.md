# Modern Light Style Reference

Use this file as the **source of truth** for the `modern-light` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: clean, minimal, professional, and quiet. This theme favors white surfaces, subtle separation, restrained accent color, and generous whitespace.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #ffffff | SVG background |
| node-fill | #ffffff | Node background |
| node-stroke | #e5e7eb | Node border |
| node-stroke-hover | #d1d5db | Node border on hover |
| text-primary | #111827 | Node labels |
| text-secondary | #6b7280 | Sublabels, annotations |
| text-title | #111827 | Diagram title |
| edge-data | #3b82f6 | Data flow edges |
| edge-control | #6b7280 | Control flow edges |
| edge-dependency | #9ca3af | Dependency edges |
| edge-async | #8b5cf6 | Async edges |
| group-fill | #f9fafb | Group background |
| group-stroke | #e5e7eb | Group border |
| group-label | #374151 | Group title text |
| accent | #3b82f6 | Primary accent color |
| shadow | rgba(0,0,0,0.06) | Drop shadow color |

## Typography

font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
- Title: 22px, font-weight 600, color text-title
- Node label: 14px, font-weight 500, color text-primary
- Sub-label: 12px, font-weight 400, color text-secondary
- Edge label: 12px, font-weight 400, color text-secondary
- Group label: 12px, font-weight 600, text-transform uppercase, letter-spacing 0.5px, color group-label

## Node Styles

```css
.node-shape {
  fill: #ffffff;
  stroke: #e5e7eb;
  stroke-width: 1.5;
  filter: url(#shadow-sm);
}
```

Optional hover refinement for interactive SVGs:

```css
.node:hover .node-shape {
  stroke: #d1d5db;
}
```

## Shadow Filter

```svg
<filter id="shadow-sm" x="-10%" y="-10%" width="120%" height="130%">
  <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.06)" flood-opacity="1"/>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#3b82f6"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#6b7280"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#9ca3af"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#8b5cf6"/>
</marker>
```

## Edge Styles

```css
.edge-data { stroke: #3b82f6; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-control { stroke: #6b7280; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #9ca3af; stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #8b5cf6; stroke-width: 1.5; stroke-dasharray: 3,3; marker-end: url(#arrow-async); }
```

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 3s, dasharray: 8,4 |
| Hover glow | ✗ | — |
| Hover lift | ✓ | translateY: -3px, duration: 0.25s |
| Entrance | ✗ | — |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #ffffff;
  --node-fill: #ffffff;
  --node-stroke: #e5e7eb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --edge-data: #3b82f6;
  --edge-control: #6b7280;
  --edge-dependency: #9ca3af;
  --edge-async: #8b5cf6;
  --group-fill: #f9fafb;
  --group-stroke: #e5e7eb;
  --flow-duration: 3s;
  --shadow-color: rgba(0,0,0,0.06);
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #ffffff;
    --node-fill: #ffffff;
    --node-stroke: #e5e7eb;
    --node-stroke-hover: #d1d5db;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --text-title: #111827;
    --edge-data: #3b82f6;
    --edge-control: #6b7280;
    --edge-dependency: #9ca3af;
    --edge-async: #8b5cf6;
    --group-fill: #f9fafb;
    --group-stroke: #e5e7eb;
    --group-label: #374151;
    --flow-duration: 3s;
    --shadow-color: rgba(0,0,0,0.06);
  }

  svg {
    background: var(--canvas-bg);
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 600;
  }

  .node {
    transition: transform 0.25s ease;
  }

  .node:hover {
    transform: translateY(-3px);
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    filter: url(#shadow-sm);
    transition: stroke 0.25s ease;
  }

  .node:hover .node-shape {
    stroke: var(--node-stroke-hover);
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 14px;
    font-weight: 500;
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
    stroke-width: 1.5;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
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
  <filter id="shadow-sm" x="-10%" y="-10%" width="120%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.06)" flood-opacity="1"/>
  </filter>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#3b82f6"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#6b7280"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#9ca3af"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#8b5cf6"/>
  </marker>
</defs>
```

## Usage Notes

- This is the **DEFAULT** theme when no preference is stated.
- Prioritize whitespace and readability over decoration.
- Shadows should be barely noticeable and never heavy.
- Use color sparingly: most structure should remain grayscale with blue as the main accent.
- Prefer blue for primary data emphasis; reserve purple for explicit async meaning only.
- The hover lift effect replaces hover glow in this theme: subtle motion, not luminous emphasis.
