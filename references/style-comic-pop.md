# Comic Pop Style Reference

Use this file as the **source of truth** for the `comic-pop` theme. The Agent should copy these values and snippets directly into generated SVG output with no reinterpretation.

Design intent: bold, energetic, and playful. This theme evokes comic books, pop art, and manga with thick black outlines, halftone dot patterns, high-saturation colors, speech-bubble nodes, and punchy motion effects.

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| canvas-bg | #2b2b2b | Dark gray background |
| canvas-dots | #3a3a3a | Halftone dot color |
| node-fill | #ffffff | Bright white node fill |
| node-stroke | #1a1a1a | Thick black outlines |
| node-stroke-hover | #ff4444 | Red highlight on hover |
| text-primary | #1a1a1a | Dark node labels |
| text-secondary | #555555 | Sublabels, annotations |
| text-title | #ffd700 | Gold/yellow title |
| edge-data | #4488ff | Blue data flow edges |
| edge-control | #ffffff | White control flow edges |
| edge-dependency | #ff4444 | Red dependency edges |
| edge-async | #44dd44 | Green async edges |
| group-fill | rgba(255,215,0,0.08) | Faint gold group background |
| group-stroke | #1a1a1a | Black group border |
| group-label | #ffd700 | Gold group title text |
| accent | #ff4444 | Primary accent (red) |
| accent-secondary | #4488ff | Secondary accent (blue) |
| accent-tertiary | #44dd44 | Tertiary accent (green) |

## Typography

font-family: "Bangers", "Comic Neue", "Comic Sans MS", cursive
- Title: 24px, font-weight 700, color text-title, letter-spacing 2px, text-transform uppercase
- Node label: 13px, font-weight 700, color text-primary
- Sub-label: 11px, font-weight 400, color text-secondary
- Edge label: 11px, font-weight 700, color text-secondary
- Group label: 12px, font-weight 700, text-transform uppercase, letter-spacing 2px, color group-label

## Node Styles

```css
.node-shape {
  fill: #ffffff;
  stroke: #1a1a1a;
  stroke-width: 3;
  filter: url(#comic-shadow);
}
```

Nodes have thick black outlines and a hard drop shadow (no blur, offset only) to create a comic panel effect.

## Filter / Effect Definitions

```svg
<!-- Halftone dot pattern for background -->
<pattern id="comic-dots" width="8" height="8" patternUnits="userSpaceOnUse">
  <circle cx="4" cy="4" r="1.5" fill="#3a3a3a"/>
</pattern>

<!-- Hard drop shadow (comic style - no blur) -->
<filter id="comic-shadow" x="-5%" y="-5%" width="115%" height="115%">
  <feOffset dx="3" dy="3" in="SourceGraphic" result="offset"/>
  <feFlood flood-color="#000000" flood-opacity="0.4" result="color"/>
  <feComposite in="color" in2="offset" operator="in" result="shadow"/>
  <feMerge>
    <feMergeNode in="shadow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<!-- Glow for highlighted/active nodes -->
<filter id="comic-glow" x="-10%" y="-10%" width="120%" height="120%">
  <feGaussianBlur stdDeviation="4" in="SourceGraphic" result="blur"/>
  <feFlood flood-color="#ffd700" flood-opacity="0.6" result="color"/>
  <feComposite in="color" in2="blur" operator="in" result="glow"/>
  <feMerge>
    <feMergeNode in="glow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

## Arrow Markers

```svg
<marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#4488ff"/>
</marker>

<marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffffff"/>
</marker>

<marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ff4444"/>
</marker>

<marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 Z" fill="#44dd44"/>
</marker>
```

Note: markers use standard 6×6 size for clean proportions.

## Edge Styles

```css
.edge-data { stroke: #4488ff; stroke-width: 2.5; marker-end: url(#arrow-data); }
.edge-control { stroke: #ffffff; stroke-width: 2.5; marker-end: url(#arrow-control); }
.edge-dependency { stroke: #ff4444; stroke-width: 2.5; stroke-dasharray: 8,4; marker-end: url(#arrow-dependency); }
.edge-async { stroke: #44dd44; stroke-width: 2.5; stroke-dasharray: 4,4; marker-end: url(#arrow-async); }
```

Edges are thicker (2.5px vs 1.5px) to match the bold outline aesthetic.

## Animation Config

| Animation | Enabled | Parameters |
|-----------|---------|------------|
| Edge flow | ✓ | duration: 2s, dasharray: 12,6 (faster, bolder dashes) |
| Hover glow | ✓ | filter: comic-glow on hover |
| Hover lift | ✗ | — |
| Entrance | ✓ | pop-in scale 0→1, duration 0.4s, ease-back |
| Pulse | ✗ | — |
| Edge glow | ✗ | — |

## CSS Variables Block

```css
:root {
  --canvas-bg: #2b2b2b;
  --canvas-dots: #3a3a3a;
  --node-fill: #ffffff;
  --node-stroke: #1a1a1a;
  --node-stroke-hover: #ff4444;
  --text-primary: #1a1a1a;
  --text-secondary: #555555;
  --text-title: #ffd700;
  --edge-data: #4488ff;
  --edge-control: #ffffff;
  --edge-dependency: #ff4444;
  --edge-async: #44dd44;
  --group-fill: rgba(255,215,0,0.08);
  --group-stroke: #1a1a1a;
  --group-label: #ffd700;
  --flow-duration: 2s;
}
```

## Complete Style Block Example

```svg
<style>
  :root {
    --canvas-bg: #2b2b2b;
    --canvas-dots: #3a3a3a;
    --node-fill: #ffffff;
    --node-stroke: #1a1a1a;
    --node-stroke-hover: #ff4444;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --text-title: #ffd700;
    --edge-data: #4488ff;
    --edge-control: #ffffff;
    --edge-dependency: #ff4444;
    --edge-async: #44dd44;
    --group-fill: rgba(255,215,0,0.08);
    --group-stroke: #1a1a1a;
    --group-label: #ffd700;
    --flow-duration: 2s;
  }

  svg {
    background: var(--canvas-bg);
    font-family: "Bangers", "Comic Neue", "Comic Sans MS", cursive;
  }

  .canvas-bg {
    fill: var(--canvas-bg);
  }

  .canvas-dots {
    fill: url(#comic-dots);
  }

  .diagram-title {
    fill: var(--text-title);
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  .node-shape {
    fill: var(--node-fill);
    stroke: var(--node-stroke);
    stroke-width: 3;
    filter: url(#comic-shadow);
  }

  .node-label {
    fill: var(--text-primary);
    font-size: 13px;
    font-weight: 700;
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
    stroke-width: 2.5;
    stroke-dasharray: 12,6;
  }

  .group-label {
    fill: var(--group-label);
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
  }

  .edge-data,
  .edge-control,
  .edge-dependency,
  .edge-async {
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .edge-data { stroke: var(--edge-data); stroke-width: 2.5; marker-end: url(#arrow-data); }
  .edge-control { stroke: var(--edge-control); stroke-width: 2.5; marker-end: url(#arrow-control); }
  .edge-dependency { stroke: var(--edge-dependency); stroke-width: 2.5; stroke-dasharray: 8,4; marker-end: url(#arrow-dependency); }
  .edge-async { stroke: var(--edge-async); stroke-width: 2.5; stroke-dasharray: 4,4; marker-end: url(#arrow-async); }

  .edge-animated {
    stroke-dasharray: 12,6;
    animation: cg-edge-flow var(--flow-duration) linear infinite;
  }

  @keyframes cg-edge-flow {
    to { stroke-dashoffset: -36; }
  }
</style>
```

Pair the style block with these reusable SVG defs:

```svg
<defs>
  <pattern id="comic-dots" width="8" height="8" patternUnits="userSpaceOnUse">
    <circle cx="4" cy="4" r="1.5" fill="#3a3a3a"/>
  </pattern>

  <filter id="comic-shadow" x="-5%" y="-5%" width="115%" height="115%">
    <feOffset dx="3" dy="3" in="SourceGraphic" result="offset"/>
    <feFlood flood-color="#000000" flood-opacity="0.4" result="color"/>
    <feComposite in="color" in2="offset" operator="in" result="shadow"/>
    <feMerge>
      <feMergeNode in="shadow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <filter id="comic-glow" x="-10%" y="-10%" width="120%" height="120%">
    <feGaussianBlur stdDeviation="4" in="SourceGraphic" result="blur"/>
    <feFlood flood-color="#ffd700" flood-opacity="0.6" result="color"/>
    <feComposite in="color" in2="blur" operator="in" result="glow"/>
    <feMerge>
      <feMergeNode in="glow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <marker id="arrow-data" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#4488ff"/>
  </marker>
  <marker id="arrow-control" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ffffff"/>
  </marker>
  <marker id="arrow-dependency" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ff4444"/>
  </marker>
  <marker id="arrow-async" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#44dd44"/>
  </marker>
</defs>
```

Use two full-size background rects when generating SVGs:

```svg
<rect class="canvas-bg" x="0" y="0" width="100%" height="100%"/>
<rect class="canvas-dots" x="0" y="0" width="100%" height="100%"/>
```

## Usage Notes

- Use for fun presentations, developer talks, hackathon demos, and social media graphics.
- Keep the palette bold: black outlines, white fills, with red/blue/green/gold accents.
- Prefer slightly rounded corners (rx=12) for the bubble/comic panel feel.
- The hard drop shadow (no blur, 3px offset) is the signature effect — do not replace with soft shadows.
- Edge strokes are thicker (2.5px) to match the outline weight.
- Edge flow animation is faster (2s) and uses bigger dashes (12,6) for punchy movement.
- This theme should feel fun and energetic, not corporate or subtle.
