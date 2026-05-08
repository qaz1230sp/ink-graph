# Layout Rules for Manual SVG Positioning

Use these rules when placing nodes manually for small diagrams (8 nodes or fewer). All coordinates assume the SVG origin is the top-left corner.

## Grid System

- Base unit: **40px**
- Node minimum width: **120px**
- Typical node width: **160px**
- Node minimum height: **44px**
- Typical node height: **50px**
- Snap all x/y positions, widths, heights, and gaps to multiples of **20px** whenever possible; prefer full **40px** increments for main layout anchors.

## Spacing Rules

- Horizontal gap between sibling nodes: **80px**
- Vertical gap between layers: **100px**
- Group internal padding: **20px** on all sides
- Group title area height: **32px** additional at the top
- Edge label clearance: **16px** from the stroke
- Recommended outer canvas padding: **40px** on all sides

## Canvas Sizing Formula

Use the widest layer and total layer count to determine the viewBox.

```text
canvas_width = max_layer_width + (num_columns - 1) × h_gap + 2 × 40px_padding
canvas_height = num_layers × (node_height + v_gap) + 2 × 40px_padding + title_height
```

Definitions:

- `max_layer_width`: total width of the widest layer's nodes only
- `num_columns`: maximum number of node columns in any row/layer
- `h_gap`: horizontal gap between sibling nodes (**80px**)
- `node_height`: chosen node height for the diagram (**44-50px**, usually **50px**)
- `v_gap`: vertical gap between layers (**100px**)
- `title_height`: **24px** when a canvas title is present, otherwise **0px**

## Direction Defaults by Diagram Type

| Type | Direction | Explanation |
|------|-----------|-------------|
| architecture | TD | Layers flow top to bottom |
| flowchart | TD | Steps flow downward |
| data-flow | LR | Data flows left to right |
| sequence | TD | Time flows downward |
| dependency | TD | Imports flow downward |
| mind-map | Radial | Branches expand outward from center |
| timeline | LR | Time progresses left to right |
| network-topology | TD | Hierarchy: core → distribution → access |
| comparison | — | Matrix/table layout, no directional flow |
| class-diagram | TD | Inheritance flows downward |
| er-diagram | LR | Relationships read left to right |
| use-case | TD | System boundary top, actors sides |
| state-machine | LR | Transitions progress left to right |
| component | TD | High-level components above low-level |

## Mechanical Placement Procedure

1. Choose the default direction from the table above.
2. Assign each node to a layer based on the primary reading flow.
3. Size nodes using the minimum/typical dimensions. Use one shared node size per peer set unless a label clearly needs more width.
4. For **TD** diagrams:
   - Place layer 1 at `y = 40 + title_height + 24`.
   - Put the next layer at `previous_layer_y + node_height + 100`.
   - Within a layer, place siblings left to right with **80px** gaps.
5. For **LR** diagrams:
   - Place column 1 at `x = 40`.
   - Put the next column at `previous_column_x + node_width + 80`.
   - Within a column, stack nodes top to bottom with **100px** gaps.
6. If a layer/column has fewer nodes than its neighbors, center that smaller set within the available span.
7. Add groups after node positions are known. Expand the group bounds by **20px** on every side and add an extra **32px** title strip at the top.
8. Recompute canvas size using the formula above and keep at least **40px** outer padding.

## Edge Routing Rules

- Edges connect from the **node boundary**, not the center.
- Orthogonal routing for **architecture** and **dependency** diagrams.
- Smooth bezier curves for **data-flow** diagrams.
- Straight lines for simple adjacency.
- **Never route through node interiors.** Before finalizing any edge, verify the path does not cross any intermediate node's bounding box.
- Arrowhead tip must visually touch the node border without being occluded by the node fill. Since nodes render ABOVE edges (layer order), **shorten the path endpoint by 8px** (the marker depth) so the arrowhead is fully visible.
- For **TD**: exit **bottom center** of the source (+0px), enter **top center - 8px** of the target.
- For **LR**: exit **right center** of the source (+0px), enter **left center - 8px** of the target.
- Minimum edge length: **60px** so labels have room.

### Avoiding Intermediate Nodes

When an edge must skip over intermediate nodes (e.g., a back-edge or cross-layer connection):

1. **Identify blockers:** List all nodes whose bounding box intersects the naive straight path.
2. **Choose detour direction:** Route outside the node cluster — prefer going further right/below for back-edges, left/above for forward shortcuts.
3. **Maintain 20px clearance** from any intermediate node's nearest edge.
4. **Extend the viewBox** if the detour exceeds current canvas bounds (add 40px padding beyond the furthest point).
5. **Use orthogonal segments** (H/V only) for the detour — no diagonal shortcuts through gaps.

```text
Example — back-edge from bottom node to top node, with 2 nodes in between:

Nodes in column at x=500:
  A: y=80-136
  B: y=220-276   ← blocker
  C: y=360-416   ← blocker  
  D: y=500-556   (source)

Edge D → A (back-edge):
  ❌ M 500 500 V 144            (cuts through B and C)
  ✅ M 590 528 H 700 V 108 H 508  (exits D right, routes outside, enters A right)
```

### TD Routing Pattern

- Start point: `(source_x + source_w/2, source_y + source_h)`
- End point: `(target_x + target_w/2, target_y - 8)` (8px gap for arrowhead)
- If source and target are in adjacent layers and aligned, use one vertical segment.
- If they are offset horizontally, route: vertical out of source → horizontal mid-segment → vertical into target.
- Put the bend line halfway between layers unless another edge already occupies that lane.

### LR Routing Pattern

- Start point: `(source_x + source_w, source_y + source_h/2)`
- End point: `(target_x - 8, target_y + target_h/2)` (8px gap for arrowhead)
- If aligned, use one horizontal segment.
- If vertically offset, route: horizontal out of source → vertical mid-segment → horizontal into target.

## Alignment Rules

- Nodes in the same layer share the same **y-coordinate** in **TD** layouts.
- Nodes in the same layer share the same **x-coordinate** in **LR** layouts.
- Center-align nodes within their column or row.
- If a layer has fewer nodes than adjacent layers, center the group.
- Groups should have even internal margins.
- Preserve a single dominant reading axis; avoid small diagonal drifts between peers.

## Label Placement

- Node labels: centered horizontally and vertically within the node.
- Edge labels: placed at the visual midpoint, offset **12px** from the stroke.
- Keep edge labels at least **16px** away from arrowheads, bends, and nearby nodes.
- Group labels: top-left corner, inside the group padding area, smaller and bolder than node labels.
- Title: centered at the top of the canvas, **24px** below the top edge.

## Diagram-Type Specific Guidance

### Architecture

- Common layers: client → gateway → services → data
- Use groups for zones: public/private, edge/core, control/data plane
- Prefer orthogonal routing
- Reserve extra vertical spacing between layers for arrow labels

### Flowchart

- Rounded rectangles for processes, diamonds for decisions
- Keep yes/no branches symmetric
- Limit crossing edges aggressively
- Labels: short action phrases, 1–4 words

### Data-Flow

- Emphasize named arrows; thicker/animated for primary streams
- Group by: producers, processors, consumers
- Storage/sinks at right or bottom edge
- Transformations visually central

### Sequence

Geometry:
- Participant header width: 140–180px
- Lifeline spacing: 180–240px
- Message row height: 44–56px
- Top margin before first message: 80px
- Activation bar width: 14–18px

Rules:
- Lifelines vertical, evenly spaced
- Participants left-to-right in interaction or authority order
- Messages progress top to bottom
- Loop/alt/opt frames sit behind message arrows

### Dependency

- Group by package, domain, or ownership boundary
- Dashed edges for dependency semantics
- Minimize decorative effects; structure is primary

### Mind Map

- Central topic node larger (200×60 minimum), bold
- Level 1 branches radiate outward with curved connectors (quadratic Bézier)
- Level 2+ nodes smaller, positioned along branch direction
- Even angular distribution around center; avoid overlaps
- Branch colors: each primary branch uses a distinct hue
- No arrowheads; connections are organic/curved
- Spacing: 120px minimum between level 1 nodes

### Timeline / Gantt

- Central horizontal axis line at vertical center
- Milestones: circles on the axis, labeled above or below (alternate)
- Phase bars: rounded rects spanning start→end along axis
- Time labels below the axis, evenly spaced
- Milestone spacing: 160–200px horizontal
- If vertical timeline: axis vertical, events alternate left/right

### Network Topology

- Hierarchical layers: Internet/Cloud → Firewall/Router → Switch → Endpoints
- Use subnet groups (dashed boundaries) to cluster related devices
- Connections: solid for physical, dashed for logical/VPN
- Device labels below icons
- Min spacing between devices: 120px

### Comparison / Matrix

- Table-like grid: header row + header column + cells
- Row height: 50–60px; column width: 140–200px

## Legend Template

```svg
<!-- Legend panel — position at bottom-left, inside viewBox padding -->
<g class="legend" transform="translate({x}, {y})">
  <!-- Enclosing panel: semi-transparent bg + accent border -->
  <rect class="legend-panel" x="-12" y="-4" width="{total_w}" height="{total_h}" rx="8"/>
  <text class="legend-title" x="0" y="14" font-size="12" font-weight="bold">Legend</text>
  <!-- Entry 1: line sample + label -->
  <line x1="0" y1="32" x2="40" y2="32" class="{edge-class-1}"/>
  <text x="52" y="36" font-size="11" class="legend-text">{label1}</text>
  <!-- Entry N: y = 32 + (n-1) * 20 -->
</g>
```

**Legend panel CSS (add to style block):**
```css
.legend-panel {
  fill: rgba(canvas-bg, 0.6);   /* use theme's canvas bg at 60% */
  stroke: var(--group-stroke);   /* accent border */
  stroke-width: 1;
  rx: 8;
}
```

**Sizing:**
- Each entry row height: **20px**
- Line sample width: **40px**, gap to text: **12px**
- Panel width = max(label_text_width) + 80 (12 left pad + 40 line + 12 gap + text + 16 right pad)
- Panel height = `24(title) + entries × 20 + 8(bottom padding)`
- Position: bottom-left of canvas, 20px inside viewBox edge (default)
- Cell content: text, checkmarks (✓), crosses (✗), or small icons
- Header cells: distinct fill color (darker/bolder)
- Grid lines: thin (1px), subtle color
- No directional edges; structure is purely tabular

### Class Diagram (UML)

- Three-section rectangles: name | attributes | methods
- Section dividers: horizontal lines within the box
- Inheritance arrows: solid line + hollow triangle head (points to parent)
- Implementation: dashed line + hollow triangle
- Association: solid line + open arrow
- Composition: solid line + filled diamond at owner end
- Min class box width: 160px; height adapts to content
- Attribute format: `- name: Type` or `+ name: Type`

### ER Diagram

- Entity boxes: two-section rects (name header + fields list)
- Primary key fields marked with underline or key icon
- Relationships: lines with cardinality notation (1, N, 0..1, 0..*)
- Cardinality labels placed near the entity end (8–12px from border)
- Diamond shape optional for relationship names
- Spacing: 200px+ between entities

### Use Case Diagram

- System boundary: large dashed rectangle containing use cases
- Actors: stick figures outside the boundary (left or right)
- Use cases: ellipses inside the boundary
- Association: solid line (actor → use case)
- Include: dashed arrow + `<<include>>` label
- Extend: dashed arrow + `<<extend>>` label
- Actor spacing: 100px; use case spacing: 80px vertical

### State Machine

- States: rounded-pill rectangles (wide rx, like 20+)
- Initial state: small filled black circle (r=8)
- Final state: bullseye — inner filled circle + outer ring
- Transitions: solid arrows with event/guard labels
- Self-transitions: curved arrow looping back to same state
- Guard conditions: `[condition]` on the transition label
- Event format: `event [guard] / action`
- State entry/exit actions inside state box in smaller text

### Component Diagram

- Component boxes: rectangles with small double-bar (≡) icon in top-left
- Provided interfaces: circle (lollipop) on component edge
- Required interfaces: half-circle (socket) on component edge
- Dependency arrows: dashed with open arrowhead
- Package grouping: large container with tab
- Port labels: small text near interface symbols

## Quick Checks

- No two nodes overlap.
- Labels fit within node width or the node is widened.
- Group borders do not touch internal nodes or edge labels.
- Arrowheads stop at borders instead of entering fills.
- The main flow is obvious in one scan from top-to-bottom or left-to-right.
