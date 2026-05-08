# SVG Animations Reference

Use this file as a **copy-paste code library** for SVG `<style>` blocks and inline SMIL snippets. All examples are self-contained, valid inside SVGs, and rely on CSS custom properties so the Agent can tune values per theme.

Conventions:

- `.node` is the outer node `<g>` wrapper.
- `.node-shape` is the primary visible shape inside the node.
- `.group` is the outer container/group `<g>` wrapper.
- `.edge-animated` and `.edge-glow` apply to edge `<path>` or `<line>` elements.
- These snippets are designed for **zero JavaScript** SVG output.

## 1. Edge Flow Animation

Use this for animated dashed edges that imply direction or data movement.

```css
/* Base flowing dash animation */
.edge-animated {
  stroke-dasharray: 8, 4;
  animation: cg-edge-flow var(--flow-duration, 2s) linear infinite;
}

@keyframes cg-edge-flow {
  to { stroke-dashoffset: -24; }
}

/* Speed presets */
.edge-flow-standard {
  --flow-duration: 2s;
}

.edge-flow-slow {
  --flow-duration: 4s;
}

.edge-flow-fast {
  --flow-duration: 1.2s;
}

/* Reverse direction for backflow / return paths */
.edge-flow-reverse {
  animation-name: cg-edge-flow-reverse;
}

@keyframes cg-edge-flow-reverse {
  to { stroke-dashoffset: 24; }
}
```

Notes:

- Use **standard flow** for general diagrams.
- Use **slow flow (4s)** for `blueprint` so motion stays calm.
- Use **fast flow (1.2s)** for `neon-cyber`.
- Add `.edge-flow-reverse` only when the visual story needs reversed direction.

## 2. Node Hover Glow

Use this when a theme supports hover emphasis via glow.

```css
/* Smooth glow transition on node geometry */
.node rect,
.node circle,
.node polygon,
.node path {
  transition: filter 0.3s ease, transform 0.3s ease;
}

.node:hover rect,
.node:hover circle,
.node:hover polygon,
.node:hover path {
  filter: drop-shadow(0 0 var(--glow-radius, 8px) var(--glow-color, rgba(56,189,248,0.4)))
          drop-shadow(0 0 calc(var(--glow-radius, 8px) * 2) var(--glow-color, rgba(56,189,248,0.2)));
}
```

Typical theme values:

- `dark-tech`: `--glow-radius: 8px; --glow-color: rgba(56,189,248,0.4);`
- `warm-minimal`: `--glow-radius: 6px; --glow-color: rgba(251,146,60,0.35);`
- `neon-cyber`: `--glow-radius: 16px; --glow-color: rgba(57,255,20,0.55);`

## 3. Node Hover Lift

Use this for subtle interactive depth without changing the node styling itself.

**Important:** Do NOT apply CSS `transform` on the `.node` wrapper — it overrides SVG positioning. Instead, apply the lift to the inner `.node-shape` element.

```css
/* Gentle upward lift on hover — applied to inner shape, not the positioned group */
.node .node-shape {
  transition: transform 0.25s ease;
}

.node:hover .node-shape {
  transform: translateY(-3px);
}
```

Notes:

- Best fit: `modern-light`.
- Skip this in themes that already use strong glow or entrance motion.

## 4. Node Entrance Animation (Staggered)

Use this when nodes should fade in sequentially. The full delay list below supports up to 20 nodes.

**Important:** Nodes use SVG `transform="translate(x,y)"` for positioning. CSS `transform` properties OVERRIDE this, causing nodes to collapse to (0,0). Therefore, entrance animations must use **opacity only** — no CSS `transform`.

```css
/* Node entrance: opacity-only fade in (preserves SVG transform positioning) */
.node {
  opacity: 0;
  animation: cg-enter var(--entrance-duration, 0.4s) ease forwards;
}

@keyframes cg-enter {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Stagger via CSS custom property */
.node { animation-delay: calc(var(--enter-index, 0) * var(--entrance-stagger, 0.1s)); }
```

Set `--enter-index` per node using inline style or utility classes:

```svg
<!-- Option A: inline CSS variable (preferred — concise) -->
<g class="node" style="--enter-index: 0" transform="translate(100,80)">...</g>
<g class="node" style="--enter-index: 1" transform="translate(100,180)">...</g>

<!-- Option B: utility classes -->
<g class="node enter-3" transform="translate(100,380)">...</g>
```

```css
/* Utility classes (optional, for agents that prefer class-only styling) */
.enter-0 { --enter-index: 0; }
.enter-1 { --enter-index: 1; }
.enter-2 { --enter-index: 2; }
/* ... up to .enter-19 */
```

## 5. Group Entrance

Use this when container groups should appear before their child nodes.

**Important:** Groups also use SVG `transform="translate(x,y)"` for positioning. Use opacity-only animation, same as nodes.

```css
/* Group entrance: opacity-only (preserves SVG transform positioning) */
.group {
  opacity: 0;
  animation: cg-group-enter 0.5s ease forwards;
}

@keyframes cg-group-enter {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

Notes:

- Render groups before nodes in the SVG structure when possible.
- If both are animated, let groups start at `0s` and nodes begin stagger after that.

## 6. Pulse Animation (SMIL)

Use this only for `neon-cyber` or other intentionally high-energy themes.

### SMIL snippet

```svg
<animate attributeName="opacity" values="1;0.6;1" dur="1.5s" repeatCount="indefinite"/>
```

### CSS-only variant

```css
/* CSS fallback / alternative to SMIL pulse */
.node-pulse .node-shape {
  animation: cg-pulse 1.5s ease infinite;
}

@keyframes cg-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}
```

## Diagram-Type Animation Defaults

| Type | Animation Level |
|------|----------------|
| architecture | subtle entrance + optional data-flow |
| flowchart | light entrance only |
| data-flow | entrance + animated primary edges |
| sequence | minimal (clarity first) |
| dependency | little or none |
| mind-map | gentle radial expansion from center |
| timeline | left-to-right stagger entrance |
| network-topology | subtle entrance, optional pulse on active links |
| comparison | none or minimal fade-in |
| class-diagram | minimal entrance only |
| er-diagram | minimal entrance only |
| use-case | light entrance |
| state-machine | entrance + optional edge pulse for active transitions |
| component | subtle entrance |
```

Usage note:

- Prefer applying pulse to a small number of focal nodes, not every node in the diagram.

## 7. Edge Glow Pulse (for neon-cyber)

Use this on important edges when `neon-cyber` needs a stronger energized look.

```css
/* Pulsing glow for highlighted neon edges */
.edge-glow {
  animation: cg-edge-glow 2s ease infinite;
}

@keyframes cg-edge-glow {
  0%, 100% { filter: drop-shadow(0 0 3px var(--edge-glow-color)); }
  50% { filter: drop-shadow(0 0 8px var(--edge-glow-color)); }
}
```

## 8. Theme Animation Configuration Table

Use this table to decide exactly which animation snippets to include for each theme.

| Animation | modern-light | dark-tech | blueprint | warm-minimal | monochrome | neon-cyber |
|-----------|-------------|-----------|-----------|--------------|------------|------------|
| Edge flow | ✓ (3s) | ✓ (1.5s) | ✓ (4s) | ✓ (2.5s) | ✗ | ✓ (1.2s) |
| Hover glow | ✗ | ✓ (8px, cyan) | ✗ | ✓ (6px, orange) | ✗ | ✓ (16px, neon) |
| Hover lift | ✓ (-3px) | ✗ | ✗ | ✗ | ✗ | ✗ |
| Entrance | ✗ | ✓ (0.1s stagger) | ✗ | ✗ | ✗ | ✓ (0.08s stagger) |
| Pulse | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (1.5s) |
| Edge glow | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |

## 9. CSS Variables Section

Define these variables near the top of the SVG `<style>` block, then override per theme as needed.

```css
:root {
  --flow-duration: 2s;
  --glow-radius: 8px;
  --glow-color: rgba(56,189,248,0.4);
  --entrance-duration: 0.4s;
  --entrance-stagger: 0.1s;
  --edge-glow-color: rgba(57,255,20,0.6);
}
```

Common overrides:

- `modern-light`: `--flow-duration: 3s;`
- `dark-tech`: `--flow-duration: 1.5s; --glow-radius: 8px; --glow-color: rgba(56,189,248,0.4);`
- `blueprint`: `--flow-duration: 4s;`
- `warm-minimal`: `--flow-duration: 2.5s; --glow-radius: 6px; --glow-color: rgba(251,146,60,0.35);`
- `neon-cyber`: `--flow-duration: 1.2s; --glow-radius: 16px; --glow-color: rgba(57,255,20,0.55); --edge-glow-color: rgba(57,255,20,0.6);`

## 10. Usage Notes

- All animations are pure CSS + SMIL — zero JavaScript.
- SVG is fully self-contained (no external dependencies).
- For print/export, animations are harmless (static first frame shown).
- `monochrome` theme should skip loading this file entirely (or use no animation classes).
- Entrance animations use `animation-fill-mode: forwards` to stay visible after animation.
- Multiple animation systems can coexist (e.g., entrance + edge flow).
- Keep infinite animations limited to edges/subtle effects — don't make the whole diagram pulse.
