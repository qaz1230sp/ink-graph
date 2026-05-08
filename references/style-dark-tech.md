# Dark Tech Style Reference

Use this file as the **source of truth** for the `dark-tech` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: technical, sophisticated, and high-contrast. This theme draws from VS Code dark mode, observability dashboards, Grafana, and terminal UIs. It uses dark blue surfaces, neon/cyan accents, monospace typography, and subtle glow to suggest active systems without becoming visually noisy.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #0f172a | SVG background (very dark blue) |
| node-fill | #1e293b | Node background |
| node-stroke | #38bdf8 | Node border (cyan) |
| text-primary | #e2e8f0 | Node labels (light gray) |
| text-secondary | #94a3b8 | Sublabels |
| text-title | #f1f5f9 | Diagram title |
| edge-data | #38bdf8 | Data flow (cyan) |
| edge-control | #f97316 | Control flow (orange) |
| edge-dependency | #64748b | Dependency (muted) |
| edge-async | #a78bfa | Async (purple) |
| group-fill | #1e293b80 | Group bg (semi-transparent) |
| group-stroke | #334155 | Group border |
| group-label | #94a3b8 | Group title |
| accent | #38bdf8 | Primary accent (cyan) |
| glow-color | rgba(56,189,248,0.3) | Glow effect color |

## Typography

font-family: "JetBrains Mono", "Fira Code", "Cascadia Code", monospace
- Title: 20px, font-weight 600, color text-title
- Node label: 13px, font-weight 500, color text-primary
- Sub-label: 11px, font-weight 400, color text-secondary
- Edge label: 11px, font-weight 400, color text-secondary
- Group label: 11px, font-weight 600, text-transform uppercase, letter-spacing 1px, color group-label

## Node Styles with Glow Filter

```css
.node-shape {
  fill: #1e293b;
  stroke: #38bdf8;
  stroke-width: 1.5;
  filter: url(#glow-sm);
}
```

Optional hover refinement for interactive SVGs:

```css
.node:hover .node-shape {
  stroke: #7dd3fc;
  filter: url(#glow-sm) drop-shadow(0 0 8px rgba(56,189,248,0.4));
}
```

## Glow Filter

```svg
<filter id="glow-sm" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="blur"/>
  <feFlood flood-color="rgba(56,189,248,0.3)" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="shadow"/>
  <feMerge>
    <feMergeNode in="shadow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#38bdf8"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#f97316"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#64748b"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#a78bfa"/>
</marker>
```

- data: cyan (#38bdf8)
- control: orange (#f97316)
- dependency: gray (#64748b)
- async: purple (#a78bfa)

## Edge Styles

```css
.edge-data { stroke: #38bdf8; stroke-width: 1.5; marker-end: url(#arrow-data); }
.edge-control { stroke: #f97316; stroke-width: 1.5; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #a78bfa; stroke-width: 1.5; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }
```

Use the cyan/orange/purple differentiation consistently so the viewer can distinguish data, control, and async semantics at a glance.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 1.5s |
| Hover glow | ✓ | radius: 8px, color: rgba(56,189,248,0.4) |
| Hover lift | ✗ | — |
| Entrance | ✓ | stagger: 0.1s, duration: 0.4s |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #0f172a;
  --node-fill: #1e293b;
  --node-stroke: #38bdf8;
  --node-stroke-hover: #7dd3fc;
  --text-primary: #e2e8f0;
  --text-secondary: #94a3b8;
  --text-title: #f1f5f9;
  --edge-data: #38bdf8;
  --edge-control: #f97316;
  --edge-dependency: #64748b;
  --edge-async: #a78bfa;
  --group-fill: #1e293b80;
  --group-stroke: #334155;
  --group-label: #94a3b8;
  --accent: #38bdf8;
  --glow-color: rgba(56,189,248,0.3);
  --hover-glow-color: rgba(56,189,248,0.4);
  --hover-glow-radius: 8px;
  --flow-duration: 1.5s;
  --entrance-duration: 0.4s;
  --entrance-stagger: 0.1s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #0f172a;
    --node-fill: #1e293b;
    --node-stroke: #38bdf8;
    --node-stroke-hover: #7dd3fc;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-title: #f1f5f9;
    --edge-data: #38bdf8;
    --edge-control: #f97316;
    --edge-dependency: #64748b;
    --edge-async: #a78bfa;
    --group-fill: #1e293b80;
    --group-stroke: #334155;
    --group-label: #94a3b8;
    --accent: #38bdf8;
    --glow-color: rgba(56,189,248,0.3);
    --hover-glow-color: rgba(56,189,248,0.4);
    --hover-glow-radius: 8px;
    --flow-duration: 1.5s;
    --entrance-duration: 0.4s;
    --entrance-stagger: 0.1s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "JetBrains Mono", "Fira Code", "Cascadia Code", monospace;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 20px;
    font-weight: 600;
  }

  .node {
    animation: cg-node-enter var(--entrance-duration) ease both;
    animation-delay: calc(var(--enter-index, 0) * var(--entrance-stagger));
    transform-origin: center;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.5;
    filter: url(#glow-sm);
    transition: stroke 0.2s ease, filter 0.2s ease;
  }

  .node:hover .node-shape {
    stroke: var(--node-stroke-hover);
    filter: url(#glow-sm) drop-shadow(0 0 var(--hover-glow-radius) var(--hover-glow-color));
    animation: cg-hover-glow 1.2s ease-in-out infinite;
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
    stroke-dasharray: 6,4;
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
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 1.5; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 1.5; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 1.5; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 1.5; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }

  .edge-animated {
    stroke-dasharray: 8,4;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }

  @keyframes cg-node-enter {
    from {
      opacity: 0;
      transform: translateY(6px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes cg-hover-glow {
    0%, 100% {
      filter: url(#glow-sm) drop-shadow(0 0 4px rgba(56,189,248,0.25));
    }
    50% {
      filter: url(#glow-sm) drop-shadow(0 0 var(--hover-glow-radius) var(--hover-glow-color));
    }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <filter id="glow-sm" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="blur"/>
    <feFlood flood-color="rgba(56,189,248,0.3)" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="shadow"/>
    <feMerge>
      <feMergeNode in="shadow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#38bdf8"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#f97316"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#64748b"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#a78bfa"/>
  </marker>
</defs>
```

For staggered entrance, set `--enter-index` on each node group (for example: `<g class="node" style="--enter-index: 3">...</g>`).

## Usage Notes

- Use for technical/engineering audiences.
- Good for architecture diagrams, infrastructure maps, AI/ML pipelines, and observability views.
- The glow should be subtle — just enough to suggest luminosity, not blinding.
- Monospace font reinforces the technical feel.
- Edge colors differentiate flow types clearly: cyan for data, orange for control, purple for async.
- High contrast is essential: keep text light and backgrounds dark.
