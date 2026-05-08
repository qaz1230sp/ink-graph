# SVG Shape Reference

These snippets are intended for direct copy-paste into generated SVG output. Replace placeholder tokens such as `{x}`, `{y}`, `{w}`, `{h}`, `{cx}`, `{cy}`, and `{label}` with concrete values before rendering.

Conventions:

- Node snippets use `transform="translate({x},{y})"` so inner coordinates are local to the node box.
- `class="node-shape"` is the primary geometry class.
- `class="node-label"` is the primary text class.
- XML comments inside the snippets explain the key geometry calculations.

## 1. Process (Rounded Rectangle)

```svg
<g class="node node-process" transform="translate({x},{y})">
  <!-- Label center = ({w/2}, {h/2}) -->
  <rect width="{w}" height="{h}" rx="8" ry="8" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 2. Database (Cylinder)

```svg
<g class="node node-database" transform="translate({x},{y})">
  <!-- Ellipse depth = 8px; top and bottom arcs share radius ({w/2}, 8) -->
  <path d="M 0,8 A {w/2},8 0 0 1 {w},8 L {w},{h-8} A {w/2},8 0 0 1 0,{h-8} Z" class="node-shape"/>
  <path d="M 0,8 A {w/2},8 0 0 0 {w},8" class="node-accent"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 3. Decision (Diamond)

```svg
<g class="node node-decision" transform="translate({x},{y})">
  <!-- Diamond points = top, right, bottom, left around center ({w/2}, {h/2}) -->
  <polygon points="{w/2},0 {w},{h/2} {w/2},{h} 0,{h/2}" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 4. Gateway (Hexagon)

```svg
<g class="node node-gateway" transform="translate({x},{y})">
  <!-- Regular horizontal hexagon with 25% corner insets -->
  <polygon points="{w*0.25},0 {w*0.75},0 {w},{h/2} {w*0.75},{h} {w*0.25},{h} 0,{h/2}" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 5. Queue (Tube / Pipe)

```svg
<g class="node node-queue" transform="translate({x},{y})">
  <!-- End-cap radius = 12px; inner guide lines suggest a tube/pipe -->
  <path d="M 12,0 H {w-12} A 12,12 0 0 1 {w},12 V {h-12} A 12,12 0 0 1 {w-12},{h} H 12 A 12,12 0 0 1 0,{h-12} V 12 A 12,12 0 0 1 12,0 Z" class="node-shape"/>
  <path d="M 18,8 V {h-8} M {w-18},8 V {h-8}" class="node-accent"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 6. File / Document (Folded Corner)

```svg
<g class="node node-file" transform="translate({x},{y})">
  <!-- Fold size = 18px at top-right corner -->
  <polygon points="0,0 {w-18},0 {w},18 {w},{h} 0,{h}" class="node-shape"/>
  <path d="M {w-18},0 V 18 H {w}" class="node-accent"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 7. External System (Dashed Rect)

```svg
<g class="node node-external" transform="translate({x},{y})">
  <!-- Same geometry as process; dashed stroke differentiates external ownership -->
  <rect width="{w}" height="{h}" rx="8" ry="8" class="node-shape" stroke-dasharray="6,3"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 8. User / Actor (Avatar)

```svg
<g class="node node-actor" transform="translate({x},{y})">
  <!-- Head center = ({w/2}, 12); shoulders begin near y=26 -->
  <circle cx="{w/2}" cy="12" r="10" class="node-shape actor-head"/>
  <path d="M {w/2-16},{h-10} V {h-18} C {w/2-16},{h-30} {w/2-8},26 {w/2},26 C {w/2+8},26 {w/2+16},{h-30} {w/2+16},{h-18} V {h-10}" class="node-shape actor-body" fill="none"/>
  <text x="{w/2}" y="{h-4}" text-anchor="middle" dominant-baseline="ideographic" class="node-label">{label}</text>
</g>
```

## 9. Cloud

```svg
<g class="node node-cloud" transform="translate({x},{y})">
  <!-- Multi-lobe cloud built from cubic curves across the local box -->
  <path d="M {w*0.22},{h*0.68} C {w*0.10},{h*0.68} 0,{h*0.58} 0,{h*0.46} C 0,{h*0.34} {w*0.10},{h*0.24} {w*0.22},{h*0.24} C {w*0.27},{h*0.10} {w*0.40},0 {w*0.55},0 C {w*0.68},0 {w*0.80},{h*0.08} {w*0.86},{h*0.20} C {w*0.95},{h*0.20} {w},{h*0.30} {w},{h*0.40} C {w},{h*0.54} {w*0.89},{h*0.66} {w*0.76},{h*0.66} C {w*0.70},{h*0.76} {w*0.58},{h*0.82} {w*0.46},{h*0.80} C {w*0.37},{h*0.84} {w*0.27},{h*0.80} {w*0.22},{h*0.68} Z" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 10. Container / Group

```svg
<g class="group" transform="translate({x},{y})">
  <!-- Outer padding = 20px; title bar height = 32px -->
  <rect width="{w}" height="{h}" rx="12" ry="12" class="group-shape"/>
  <path d="M 12,0 H {w-12} A 12,12 0 0 1 {w},12 V 32 H 0 V 12 A 12,12 0 0 1 12,0 Z" class="group-title-bar"/>
  <path d="M 0,32 H {w}" class="group-divider"/>
  <text x="20" y="20" text-anchor="start" dominant-baseline="central" class="group-label">{label}</text>
</g>
```

## 11. UML Class (Three-Section Rectangle)

```svg
<g class="node node-class" transform="translate({x},{y})">
  <!-- Name section: 0 → {section1_h}; Attributes: {section1_h} → {section2_y}; Methods: {section2_y} → {h} -->
  <rect width="{w}" height="{h}" rx="2" ry="2" class="node-shape"/>
  <line x1="0" y1="{section1_h}" x2="{w}" y2="{section1_h}" class="node-divider"/>
  <line x1="0" y1="{section2_y}" x2="{w}" y2="{section2_y}" class="node-divider"/>
  <text x="{w/2}" y="{section1_h/2}" text-anchor="middle" dominant-baseline="central" font-weight="bold" class="node-label">{className}</text>
  <!-- Attributes listed below first divider, Methods below second -->
</g>
```

## 12. Entity (Two-Section Rectangle for ER)

```svg
<g class="node node-entity" transform="translate({x},{y})">
  <!-- Header: 0 → 32px; Fields below -->
  <rect width="{w}" height="{h}" rx="2" ry="2" class="node-shape"/>
  <rect width="{w}" height="32" rx="2" ry="2" class="node-header"/>
  <line x1="0" y1="32" x2="{w}" y2="32" class="node-divider"/>
  <text x="{w/2}" y="16" text-anchor="middle" dominant-baseline="central" font-weight="bold" class="node-label">{entityName}</text>
  <!-- Field list starts at y=48, each field 20px tall -->
</g>
```

## 13. Use Case (Ellipse)

```svg
<g class="node node-usecase" transform="translate({x},{y})">
  <ellipse cx="{w/2}" cy="{h/2}" rx="{w/2}" ry="{h/2}" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 14. State (Rounded Pill)

```svg
<g class="node node-state" transform="translate({x},{y})">
  <!-- Pill shape: rx = h/2 for fully rounded ends -->
  <rect width="{w}" height="{h}" rx="{h/2}" ry="{h/2}" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 15. Initial State (Filled Circle)

```svg
<g class="node node-initial" transform="translate({x},{y})">
  <circle cx="{r}" cy="{r}" r="{r}" class="node-shape" fill="currentColor"/>
</g>
```

## 16. Final State (Bullseye)

```svg
<g class="node node-final" transform="translate({x},{y})">
  <!-- Outer ring + inner filled circle -->
  <circle cx="{r}" cy="{r}" r="{r}" class="node-shape" fill="none" stroke-width="2"/>
  <circle cx="{r}" cy="{r}" r="{r*0.6}" class="node-shape" fill="currentColor"/>
</g>
```

## 17. Component (Rectangle with Double-Bar Icon)

```svg
<g class="node node-component" transform="translate({x},{y})">
  <rect width="{w}" height="{h}" rx="4" ry="4" class="node-shape"/>
  <!-- Component icon: two small rectangles on left edge -->
  <rect x="-8" y="{h*0.3}" width="16" height="8" rx="1" class="node-accent component-tab"/>
  <rect x="-8" y="{h*0.55}" width="16" height="8" rx="1" class="node-accent component-tab"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## 18. Mind-Map Center Node (Large Pill)

```svg
<g class="node node-mindmap-center" transform="translate({x},{y})">
  <rect width="{w}" height="{h}" rx="30" ry="30" class="node-shape"/>
  <text x="{w/2}" y="{h/2}" text-anchor="middle" dominant-baseline="central" font-weight="bold" font-size="16" class="node-label">{label}</text>
</g>
```

## 19. Timeline Milestone (Circle on Axis)

```svg
<g class="node node-milestone" transform="translate({x},{y})">
  <circle cx="0" cy="0" r="{r}" class="node-shape"/>
  <text x="0" y="{r+16}" text-anchor="middle" dominant-baseline="hanging" class="node-label">{label}</text>
</g>
```

## 20. Network Device (Icon-Rect)

```svg
<g class="node node-device" transform="translate({x},{y})">
  <rect width="{w}" height="{h}" rx="6" ry="6" class="node-shape"/>
  <!-- Device icon placeholder area: top 60% for icon, bottom 40% for label -->
  <text x="{w/2}" y="{h*0.35}" text-anchor="middle" dominant-baseline="central" font-size="20" class="node-icon">{icon}</text>
  <text x="{w/2}" y="{h*0.75}" text-anchor="middle" dominant-baseline="central" class="node-label">{label}</text>
</g>
```

## Notes for Substitution

- Replace `{x}` and `{y}` with the top-left corner of the node or group.
- Replace `{w}` and `{h}` with the final box dimensions.
- Replace `{cx}` and `{cy}` only if you prefer center-based calculations elsewhere; the snippets above use local coordinates inside translated groups.
- Keep text anchored exactly as shown so labels remain centered after substitution.
- For class/entity shapes, compute section heights based on number of attributes/fields (each line ~20px).
- For state machines, `{r}` is typically 8px for initial/final states.
- For mind-map center nodes, use `rx=30` for pronounced pill shape; branch nodes use smaller `rx=12`.
