# Neon Cyber Style Reference

Use this file as the **source of truth** for the `neon-cyber` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: dramatic, energized, and unmistakably sci-fi. This theme channels cyberpunk HUDs, Tron-style neon lines, and high-contrast demo visuals with intense glow, scan-lines, vivid semantic colors, and full-motion presentation effects.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #0a0a0f | SVG background |
| node-fill | #111118 | Node background |
| node-stroke | #39ff14 | Primary node border |
| node-stroke-secondary | #ff006e | Secondary node border |
| text-primary | #39ff14 | Node labels |
| text-secondary | #e0e0e0 | Sublabels, annotations |
| text-title | #39ff14 | Diagram title |
| edge-data | #39ff14 | Data flow edges |
| edge-control | #ff006e | Control flow edges |
| edge-dependency | #00d4ff | Dependency edges |
| edge-async | #bf5af2 | Async edges |
| group-fill | rgba(17,17,24,0.65) | Group background |
| group-stroke | #ff006e | Group border |
| group-label | #00d4ff | Group title text |
| accent | #39ff14 | Primary accent color |
| glow-color | rgba(57,255,20,0.55) | Primary glow |
| glow-color-secondary | rgba(255,0,110,0.45) | Secondary glow |
| edge-glow-color | rgba(57,255,20,0.6) | Animated edge glow |
| scan-line | rgba(224,224,224,0.05) | Scan-line overlay |

## Typography

font-family: "Orbitron", "Share Tech Mono", "Rajdhani", monospace
- Title: 22px, font-weight 700, color text-title
- Node label: 14px, font-weight 600, color text-primary
- Sub-label: 12px, font-weight 400, color text-secondary
- Edge label: 11px, font-weight 500, color text-secondary
- Group label: 11px, font-weight 700, text-transform uppercase, letter-spacing 1.2px, color group-label

## Node Styles

```css
.node-shape {
  fill: #111118;
  stroke: #39ff14;
  stroke-width: 1.8;
  filter: url(#glow-neon);
}

.node-secondary .node-shape {
  stroke: #ff006e;
  filter: url(#glow-pink);
}
```

## Filter / Effect Definitions

```svg
<filter id="glow-neon" x="-40%" y="-40%" width="180%" height="180%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="blur"/>
  <feFlood flood-color="rgba(57,255,20,0.55)" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="glow"/>
  <feMerge>
    <feMergeNode in="glow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<filter id="glow-pink" x="-40%" y="-40%" width="180%" height="180%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="blur"/>
  <feFlood flood-color="rgba(255,0,110,0.45)" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="glow"/>
  <feMerge>
    <feMergeNode in="glow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<pattern id="scan-lines" width="4" height="4" patternUnits="userSpaceOnUse">
  <rect width="4" height="4" fill="transparent"/>
  <line x1="0" y1="1" x2="4" y2="1" stroke="rgba(224,224,224,0.05)" stroke-width="1"/>
  <line x1="0" y1="3" x2="4" y2="3" stroke="rgba(224,224,224,0.03)" stroke-width="1"/>
</pattern>
```

Optional hover refinement for interactive SVGs:

```css
.node:hover .node-shape {
  filter: url(#glow-neon) drop-shadow(0 0 16px rgba(57,255,20,0.55));
}

.node-secondary:hover .node-shape {
  filter: url(#glow-pink) drop-shadow(0 0 16px rgba(255,0,110,0.5));
}
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#39ff14"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ff006e"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00d4ff"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#bf5af2"/>
</marker>
```

## Edge Styles

```css
.edge-data { stroke: #39ff14; stroke-width: 1.8; marker-end: url(#arrow-data); }
.edge-control { stroke: #ff006e; stroke-width: 1.8; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #00d4ff; stroke-width: 1.8; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #bf5af2; stroke-width: 1.8; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }
```

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 1.2s, dasharray: 8,4 |
| Hover glow | ✓ | radius: 16px, color matches node stroke |
| Hover lift | ✗ | — |
| Entrance | ✓ | stagger: 0.08s, duration: 0.28s |
| Pulse | ✓ | cycle: 1.5s on key nodes |
| Edge glow | ✓ | cycle: 2s, pulsing drop-shadow |

## CSS Variables Block

```css
:root {
  --canvas-bg: #0a0a0f;
  --node-fill: #111118;
  --node-stroke: #39ff14;
  --node-stroke-secondary: #ff006e;
  --text-primary: #39ff14;
  --text-secondary: #e0e0e0;
  --text-title: #39ff14;
  --edge-data: #39ff14;
  --edge-control: #ff006e;
  --edge-dependency: #00d4ff;
  --edge-async: #bf5af2;
  --group-fill: rgba(17,17,24,0.65);
  --group-stroke: #ff006e;
  --group-label: #00d4ff;
  --glow-color: rgba(57,255,20,0.55);
  --glow-color-secondary: rgba(255,0,110,0.45);
  --edge-glow-color: rgba(57,255,20,0.6);
  --hover-glow-radius: 16px;
  --flow-duration: 1.2s;
  --entrance-duration: 0.28s;
  --entrance-stagger: 0.08s;
  --pulse-duration: 1.5s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #0a0a0f;
    --node-fill: #111118;
    --node-stroke: #39ff14;
    --node-stroke-secondary: #ff006e;
    --text-primary: #39ff14;
    --text-secondary: #e0e0e0;
    --text-title: #39ff14;
    --edge-data: #39ff14;
    --edge-control: #ff006e;
    --edge-dependency: #00d4ff;
    --edge-async: #bf5af2;
    --group-fill: rgba(17,17,24,0.65);
    --group-stroke: #ff006e;
    --group-label: #00d4ff;
    --glow-color: rgba(57,255,20,0.55);
    --glow-color-secondary: rgba(255,0,110,0.45);
    --edge-glow-color: rgba(57,255,20,0.6);
    --hover-glow-radius: 16px;
    --flow-duration: 1.2s;
    --entrance-duration: 0.28s;
    --entrance-stagger: 0.08s;
    --pulse-duration: 1.5s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "Orbitron", "Share Tech Mono", "Rajdhani", monospace;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .scanlines {
    fill: url(#scan-lines);
    opacity: 0.12;
    pointer-events: none;
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .node {
    animation: cg-node-enter var(--entrance-duration) ease both;
    animation-delay: calc(var(--enter-index, 0) * var(--entrance-stagger));
    transform-origin: center;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 1.8;
    filter: url(#glow-neon);
    transition: filter 0.2s ease, stroke 0.2s ease;
  }

  .node-secondary .node-shape {
    stroke: var(--node-stroke-secondary);
    filter: url(#glow-pink);
  }

  .node:hover .node-shape {
    filter: url(#glow-neon) drop-shadow(0 0 var(--hover-glow-radius) var(--glow-color));
  }

  .node-secondary:hover .node-shape {
    filter: url(#glow-pink) drop-shadow(0 0 var(--hover-glow-radius) var(--glow-color-secondary));
  }

  .node-pulse .node-shape {
    animation: cg-pulse var(--pulse-duration) ease infinite;
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
    stroke-width: 1.5;
    stroke-dasharray: 8,4;
    filter: url(#glow-pink);
  }

  .group-label {
    fill: var(--group-label);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 1.8; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 1.8; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 1.8; stroke-dasharray: 6,3; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 1.8; stroke-dasharray: 4,3; marker-end: url(#arrow-async); }

  .edge-animated {
    stroke-dasharray: 8,4;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  .edge-glow {
    animation: cg-edge-glow 2s ease infinite;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -24; }
  }

  @keyframes cg-node-enter {
    from {
      opacity: 0;
      transform: translateY(10px) scale(0.98);
    }
    to {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }

  @keyframes cg-pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.6; }
  }

  @keyframes cg-edge-glow {
    0%, 100% { filter: drop-shadow(0 0 4px var(--edge-glow-color)); }
    50% { filter: drop-shadow(0 0 10px var(--edge-glow-color)); }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <filter id="glow-neon" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="blur"/>
    <feFlood flood-color="rgba(57,255,20,0.55)" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="glow"/>
    <feMerge>
      <feMergeNode in="glow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <filter id="glow-pink" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="blur"/>
    <feFlood flood-color="rgba(255,0,110,0.45)" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="glow"/>
    <feMerge>
      <feMergeNode in="glow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <pattern id="scan-lines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="4" fill="transparent"/>
    <line x1="0" y1="1" x2="4" y2="1" stroke="rgba(224,224,224,0.05)" stroke-width="1"/>
    <line x1="0" y1="3" x2="4" y2="3" stroke="rgba(224,224,224,0.03)" stroke-width="1"/>
  </pattern>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#39ff14"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ff006e"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#00d4ff"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#bf5af2"/>
  </marker>
</defs>
```

For staggered entrance, set `--enter-index` on each node group (for example: `<g class="node" style="--enter-index: 3">...</g>`). Add the scan-line overlay as a top-level rect when desired:

```svg
<rect class="scanlines" x="0" y="0" width="100%" height="100%"/>
```

## Usage Notes

- Use for marketing demos, keynote visuals, flashy prototypes, and intentionally dramatic presentations.
- This theme should feel high-energy and unmistakably synthetic.
- Keep neon semantic colors consistent: green=data, pink=control, cyan=dependency, purple=async.
- Use pulse only on a few focal nodes so the diagram stays readable.
- Avoid this theme for dense, formal, or print-oriented diagrams.
