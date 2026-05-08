## Common Pitfalls (Lessons Learned)

These are real bugs encountered during development. Check each one before finalizing any SVG.

### 1. CSS Transform Overrides SVG Positioning

**Problem:** CSS `@keyframes` with `transform: scale()` or `transform: translate()` will OVERRIDE an element's SVG `transform="translate(x, y)"` attribute. Positioned groups collapse to (0,0). This is the #1 cause of "nodes invisible, only edges showing" bugs.

**Affected scenarios (all confirmed in production):**
- `@keyframes cg-node-enter { from { transform: translateY(10px); } }` → all nodes pile at y=0
- `@keyframes cg-group-enter { from { transform: scale(0.97); } }` → groups at (0,0)
- `.node:hover { transform: translateY(-3px); }` → node jumps to wrong position on hover

**Fix:** For elements with SVG `transform` attributes (groups, positioned containers), use **opacity-only** animations. If motion is needed, apply it to an **inner child** (`.node-shape`) rather than the positioned `<g>`.

```css
/* ❌ BAD — kills SVG translate on the <g> wrapper */
@keyframes enter { from { transform: scale(0.98); } }
.node:hover { transform: translateY(-3px); }

/* ✅ GOOD — opacity on wrapper preserves position */
@keyframes enter { from { opacity: 0; } to { opacity: 1; } }

/* ✅ GOOD — motion on inner shape, not the positioned group */
.node:hover .node-shape { transform: translateY(-3px); }
```

**Self-check:** After writing any `@keyframes` or hover rule, verify the selector does NOT target a `<g>` that has `transform="translate(...)"`. If it does, the diagram WILL break.

### 2. Arrowheads Hidden Under Nodes (Layer Order)

**Problem:** SVG layer order: edges render first, nodes render on top. Node fills cover the arrowhead at the connection point.

**Fix:** End edge paths **8px before** the target node border. The marker's `refX` aligns the arrow tip at the path endpoint, so the arrow appears to touch the node without being covered.

```text
Target node top: y=200
Edge endpoint:   y=200 - 8 = 192  ← arrow visible
```

### 3. Edges Routing Through Intermediate Nodes

**Problem:** When an edge connects two non-adjacent nodes, the straight-line or simple L-shaped path often cuts through nodes in between.

**Fix:** Before finalizing any edge path, check if intermediate nodes occupy the same x or y band. Route around them:
- Calculate bounding boxes of ALL nodes between source and target
- Add at least **20px clearance** from any intermediate node edge
- Prefer routing OUTSIDE the node cluster (go further right/left/below) rather than threading between nodes
- After routing, verify the viewBox is wide/tall enough for the detour

```text
Example: Node A (top) → Node C (bottom), Node B in between

❌ BAD:  M 500 416 V 248  (passes through Node B at y=360-416)
✅ GOOD: M 500 416 V 460 H 800 V 248 H 718  (goes below B, routes around)
```

### 4. ViewBox Too Tight for Routed Edges

**Problem:** After routing an edge around nodes, the path exceeds the original viewBox bounds, causing clipping or cramped appearance.

**Fix:** After all edge paths are finalized, recompute the viewBox:
- Find the maximum x and y coordinates across all elements AND edge paths
- Add **40px padding** on all sides
- Ensure routed edges have at least **30px** from the canvas edge

### 5. Edge Labels Overlapping Nodes

**Problem:** Labels placed at the mathematical midpoint of an edge may land inside a nearby node's bounding box.

**Fix:**
- Place labels at edge midpoint, then check against ALL node bounding boxes
- If overlap detected, shift the label **away from the node** (outward direction)
- For decision branches (Yes/No), place labels **between** the diamond tip and the next node, offset from the line by 12px
- Keep labels within 20px of their edge line (not floating far away)

### 6. Redundant Edge Labels

**Problem:** Labeling every edge (especially in dependency graphs) creates visual noise without adding information.

**Fix:**
- Label only when the relationship is ambiguous (e.g., "auth", "events", "async")
- If all edges represent the same semantic (e.g., "imports"), label NONE — the diagram title and edge style already communicate this
- Decision branches (Yes/No) always need labels
- Maximum 40% of edges should have labels in any diagram

### 7. Sequence Diagram Activation Boxes

**Problem:** White vertical rectangles on lifelines add visual clutter without aiding comprehension in most cases.

**Fix:** Use simple dashed lifelines for all participants. Only add activation boxes when explicitly showing concurrent active scopes that overlap in time.

### 8. Architecture Group Animations

**Problem:** Heavy entrance animations (scale, translate) on architecture groups make the initial render feel chaotic.

**Fix:** Use opacity-only fade-in for groups. Reserve motion animations for edges (flow indication) only.

### 9. Hover/Entrance Transform on Positioned Elements

**Problem:** CSS `transform` on `.node` or `.group` wrappers overrides their SVG `transform="translate(x,y)"` positioning, moving them to (0,0). This applies to hover lift, entrance slide, and scale effects.

**Fix:** Apply CSS motion only to **inner elements** (`.node-shape`, `.node-label`) rather than the positioned `<g>` wrapper. Entrance animations on `.node`/`.group` must be opacity-only.

### 10. Layout Auto-Routing Through Intermediate Nodes

**Problem:** When `layout.py` operates in fallback mode (no Graphviz), edges between non-adjacent nodes may route through intermediate nodes because the fallback uses straight-line paths.

**Fix:** After receiving layout output, manually verify all edges. For any edge whose path intersects an intermediate node, reroute around the cluster with 20px clearance. This is an agent responsibility, not handled by layout.py.

### 11. Undefined Shape Accessory Classes

**Problem:** Shape snippets in `shapes.md` use `.node-accent`, `.group-title-bar`, `.group-divider` classes that no theme file defines. These render as black fills by default.

**Fix:** Always include the base accessory styles documented in the SVG generation rules. Themes can override as needed.

### 12. Legend Line/Text Misalignment

**Problem:** Legend entries place edge lines at one y-coordinate and text at another, causing visual mismatch where lines don't correspond to their labels.

**Fix:** Use `dominant-baseline="middle"` on legend text elements AND ensure the text y-coordinate matches the line's vertical midpoint exactly. Test pattern:

```svg
<path d="M 14 34 H 52" class="edge-data"/>
<text x="58" y="34" dominant-baseline="middle" class="legend-text">data</text>
```

Both share `y=34`; `dominant-baseline="middle"` vertically centers the text on that coordinate.

### 13. Edge Label / Text Contrast on Dark Backgrounds

**Problem:** Using `var(--text-secondary)` (typically #8b949e / #94a3b8) for edge labels on dark backgrounds (#0d1117, #0f172a) produces insufficient contrast (ratio < 4.5:1). Labels appear "invisible" to users.

**Fix:** Use `var(--text-primary)` or an explicit lighter color (#c9d1d9 / #e2e8f0) for edge labels in dark themes. Reserve `--text-secondary` only for sublabels that are deliberately de-emphasized. Minimum contrast ratio: 4.5:1 against the background.

```css
/* ❌ BAD — too dim on #0d1117 background */
.edge-label { fill: #8b949e; }

/* ✅ GOOD — readable on dark backgrounds */
.edge-label { fill: #c9d1d9; }
```

### 14. Horizontal Legend Cramming

**Problem:** Placing all legend entries in a single horizontal row causes text overlap when there are more than 3 entries, and wastes horizontal space.

**Fix:** ALWAYS use vertical legend layout — one entry per row. Each row is 20px tall with a 40px line sample followed by text. See the "Legend (图例)" section above for the exact template. Never use a horizontal legend.

### 15. Decorative Icons Overlapping Node Text

**Problem:** Adding small SVG icons (paths, circles) inside the left area of a node while centering the label text across the full node width causes visual overlap — the text covers the icon or vice versa.

**Fix:** Choose ONE approach per node:
- **Text-only** (recommended for clarity): Center label text in the node, no icons. This is simpler, more readable, and avoids collision issues.
- **Icon + text**: If icons are needed, shift the text to the right half (`text-anchor: start`, `x = icon_area_width + gap`) and reserve the left area exclusively for the icon.

Never center text across the full node width when an icon occupies part of that space.

### 16. Missing Inter-Layer Connections in Architecture Diagrams

**Problem:** In layered architecture diagrams, nodes within the same layer are connected horizontally, but the vertical connections between layers are missing or terminate in empty space (e.g., ending between a layer boundary and the first node inside it).

**Fix:**
- Every layer must have at least one incoming edge from the layer above (except the top layer) and one outgoing edge to the layer below (except the bottom layer).
- Vertical edges should route clearly: exit the source node's bottom → travel vertically → optionally route horizontally to reach the target's x-position → enter the target node's top.
- If the target node is not vertically aligned with the source, use an L-shaped or Z-shaped orthogonal path (e.g., `M srcX bottomY V midY H tgtX V tgtTopY`).

### 17. Edge Alignment Inconsistency

**Problem:** When multiple edges fan out from a single source (e.g., one node distributing to 3 targets), the vertical segments use slightly different x-coordinates or the horizontal routing is uneven, making the diagram look messy.

**Fix:**
- Fan-out pattern: start all branches from the same source point, drop to a shared horizontal routing channel (a consistent y-coordinate), then split horizontally to each target's x-position before dropping vertically to the target.
- Use the target nodes' center-x for vertical entry. Keep all vertical segments perfectly aligned to node centers.
- Template: `M srcCenterX srcBottomY V channelY H tgt1CenterX V tgt1TopY` for each branch.

### 18. Empty Placeholder Content in Class/Entity Nodes

**Problem:** When generating UML class diagrams or ER diagrams, some nodes have empty sections filled with "—" or left blank. This looks like a rendering error and provides no value.

**Fix:** Every section in a multi-section node must contain real, meaningful content:
- Class diagrams: attributes section must list at least one real attribute; methods section must list at least one real method. If a class truly has no attributes, omit the attributes section entirely rather than showing a placeholder.
- ER diagrams: entity fields must be real column names, never placeholders.
- If the source data is unclear, infer reasonable attributes from the class/entity name and context.

### 19. UML Multiplicity Numbers Confuse Non-technical Readers

**Problem:** Standard UML multiplicity annotations like `1`, `0..*`, `1..*` are placed near relationship endpoints. Non-UML-savvy readers see random numbers floating near lines and don't understand them.

**Fix:** Use readable English labels instead of raw multiplicity numbers:
- `1` → `one` (or omit if obvious)
- `1..*` → `many`
- `0..*` → `zero or more`
- `0..1` → `optional`
- For named relationships, prefer a verb label: `owns`, `uses`, `manages`, `contains`

Place labels close to the line midpoint or near the target end, with enough offset (8-12px) to avoid overlapping the line itself.

### 20. Nodes Overlapping Title or Canvas Edges

**Problem:** The first row of nodes is positioned too close to the title text, causing visual overlap. Often happens when title is at y=74 and the first node starts at y=80.

**Fix:** Maintain at least **40px clear space** between the title/subtitle bottom and the first node top. If title is at y=40 with subtitle at y=58, first nodes should start no earlier than y=100.

### 21. Duplicate Labels on Connected Elements

**Problem:** Interface/relationship labels appear on BOTH the source side and target side of a connection (e.g., "ui_actions" written inside the MCP Manager AND again on the executor's lollipop). This creates visual clutter and confusion.

**Fix:** Each label should appear exactly ONCE at the most semantically meaningful location:
- For provided interfaces (lollipop): label goes above the lollipop circle only
- For required interfaces (socket): label goes near the socket only
- Do NOT repeat the same label inside the component body AND on the connection point
- If a component has many required interfaces, show them only as sockets on its edge — not also as a text list inside the box

### 22. Socket/Connection Coordinate Mismatch with Parent Transform

**Problem:** When elements use `transform="translate(x,y)"`, child coordinates are in LOCAL space. A socket drawn at local `y=280` inside a group translated to `y=210` renders at ABSOLUTE `y=490` — far below intended position. This causes connections to float in empty space, completely disconnected from the components.

**Fix:**
- Calculate absolute positions FIRST, then derive local coordinates: `local_y = absolute_target - parent_translate_y`
- For sockets at a component's bottom edge: use `y = component_height` (e.g., box height=66 → sockets at local y=66~70)
- For connection lines BETWEEN layers: use absolute coordinates (no parent transform) so start/end align exactly with the source bottom and target top
- Always verify: `parent_translate + local_coord = intended_absolute_position`

### 23. Title/Filename Mismatch

**Problem:** The `<title>` text or visible heading says "Architecture" but the file is named `component.svg`. This confuses users who open the file expecting one diagram type and see another name.

**Fix:** Ensure the SVG `<title>`, the visible heading `<text>`, and the filename all agree on the diagram type. When generating, derive the heading from the requested diagram type — never copy-paste from a template without updating.

### 24. Disconnected Connection Lines (Gap Between Layers)

**Problem:** Connection lines start/end at hardcoded Y values that don't match the actual component edges. E.g., MCP Manager bottom is at y=261 but lines start at y=330, leaving a 70px visible gap.

**Fix:** Calculate connection endpoints from actual geometry:
- Line START = source component translate_y + height (bottom edge)
- Line END = target component translate_y - lollipop_height (top of lollipop)
- Verify visually: there should be NO gap between a component edge and the start/end of its connection line
- If using sockets/lollipops as intermediaries, the line connects socket_bottom → lollipop_top

### 25. Insufficient Gap Between Connected Nodes for Edge Labels

**Problem:** When two nodes are placed only 30px apart, there is no room for an edge label between them. The label text gets clipped or overlaps the nodes. This commonly happens in horizontal flow diagrams where processing nodes are packed too tightly.

**Fix:**
- Minimum gap between connected nodes: **60px** (allows a short label like "prompt")
- Preferred gap for longer labels: **70-80px**
- If the canvas is too narrow to fit all nodes with minimum gaps, INCREASE the canvas width rather than compressing gaps
- Edge label should be centered in the gap: `label_x = (source_right + target_left) / 2`
- Rule of thumb: `min_gap = max_label_width + 20px padding`

### 26. Oversized Arrow Markers

**Problem:** Arrow markers with `markerWidth="10" markerHeight="7"` appear disproportionately large compared to the stroke-width of the connection line (e.g., 2px stroke with 10px arrow head). This makes the diagram look heavy and the arrows dominate visually.

**Fix:**
- Arrow marker size should be proportional to stroke width: `markerWidth ≈ stroke-width × 3`, `markerHeight ≈ stroke-width × 2.5`
- For a 2px stroke line: use `markerWidth="6" markerHeight="5"`
- For a 1.5px stroke line: use `markerWidth="5" markerHeight="4"`
- Set `refX` to markerWidth so the tip aligns with the line endpoint

### 27. Invisible or Too-Short Dashes in Dashed Lines

**Problem:** `stroke-dasharray: 2 8` creates 2px dashes with 8px gaps — the dashes are almost invisible and the line looks like scattered dots. This commonly happens when trying to differentiate line types without checking visual appearance.

**Fix:**
- Minimum dash length: **8px** for any visible dashed line
- Recommended patterns:
  - Primary flow: `16 8` (prominent)
  - Secondary flow: `14 8` (slightly shorter)
  - Tertiary/storage: `10 6` (distinct but visible)
- Gap should never exceed dash length (ratio ≤ 1:1)
- Test: at zoom-out, dashes must still read as a continuous line, not dots

### 28. Chaotic Orthogonal Routing (Zigzag Edges)

**Problem:** Orthogonal (H/V) edge routing where each edge independently picks its own path creates a tangle of zigzag lines. E.g., one edge routes right to x=800 then back left to x=420, crossing multiple nodes.

**Fix:** Use shared routing channels:
- Pick ONE horizontal Y value per layer gap as the routing channel (e.g., y=130 between layer 0 and 1)
- ALL edges crossing that gap share the same channel
- Edges exit the source vertically, travel on the channel horizontally, then drop vertically to the target

### 29. Edge Bundling: Fan-Out and Fan-In

**Best practice:** When one node connects to multiple targets (fan-out) or multiple sources connect to one target (fan-in), bundle the edges:

**Fan-out pattern (1 → N):**
```
   source
     |          ← trunk (no arrow)
     •          ← junction dot (r=3)
  ───┼───       ← horizontal bar (no arrow)
  ↓  ↓  ↓      ← drops with arrows
  A  B  C
```
- Single trunk exits the source
- Horizontal bar spans from leftmost to rightmost target
- Individual drops from bar to each target carry the arrowhead
- Junction dot marks the split point

**Fan-in pattern (N → 1):**
```
  A  B  C  D
  |  |  |  |   ← vertical drops (no arrow)
  ───┼──────    ← horizontal merge bus (no arrow)
     •          ← junction dot
     ↓          ← trunk with arrow
   target
```
- Each source drops vertically to a shared horizontal merge bus
- Single trunk exits the bus at the target's x-coordinate with an arrowhead
- Junction dot marks the merge point

**Implementation:** Use two CSS classes:
- `.trunk` — dashed line, NO marker-end (for shared segments and bars)
- `.edge` — dashed line WITH marker-end (for final segments entering nodes)

### 30. Layout: Center Parents Above Children in Dependency Graphs

**Problem:** Placing nodes in a rigid grid without considering parent-child relationships causes long diagonal edges that cross multiple unrelated nodes.

**Fix:**
- Center each parent directly above its children group
- If a node has many children, it should be at the horizontal midpoint of the children spread
- Group related subtrees spatially — use dashed boxes with light fill to visually separate them
- Place the most-connected node (e.g., `core` with many incoming edges) where it minimizes total edge length — often below the group with the most connections to it

### 31. Fake Orthogonal Jogs (Tiny Vertical Offsets)

**Problem:** Orthogonal routing between two entities whose vertical ranges overlap produces a barely-visible vertical jog (e.g., 6-8px), which looks like a rendering bug rather than intentional routing.

**Fix:**
- Before routing, check if the source exit-y and target entry-y overlap within a reasonable band (< 30px difference AND both entities share a vertical range)
- If yes, pick a single y within the overlap zone and draw a **straight horizontal line**: `M x1,y H x2`
- Reserve orthogonal routing for connections with large vertical differences (> 40px) where a straight line would become a steep diagonal

### 32. ER Diagram: Legend Competing with Entities for Space

**Problem:** Placing the legend next to the densest entity cluster (e.g., right column) causes zero-gap adjacency or overlap with entities.

**Fix:**
- Place the legend in the **least populated corner** — typically bottom-left in a left-to-right ER layout
- Size the legend generously (min 180×76) so rows aren't cramped
- Ensure at least **40px gap** between legend and nearest entity

### 33. ER Diagram: Cardinality and Relationship Labels Overlapping

**Problem:** Cardinality marks (1, N, M) and relationship labels ("contains", "runs on") placed at similar y-offsets overlap each other or overlap the line itself.

**Fix:**
- **Cardinality marks** go close to their respective entity edge, offset ~8px horizontally inward from the edge, ~6px above the line
- **Relationship labels** go at the midpoint of the line segment, ~12px above the line
- For straight horizontal lines, all labels share the same y-band — offset cardinality by -6px and label by -13px from line y
- For orthogonal lines, place the label along the longest segment (usually the vertical channel)

### 34. Insufficient Gap Between Title/Subtitle and First Content Row

**Problem:** The first diagram element (node, legend, etc.) starts immediately below the subtitle text with only a few pixels of clearance, making the title area feel cramped and the content appear to overlap the header.

**Fix:**
- Maintain a minimum **30px clear gap** between the subtitle baseline and the top of the first content element
- If the title area occupies y=0 to y=66 (title + subtitle), the first content should start no earlier than y=100
- When fixing, shift ALL content (nodes, edges, legend) down uniformly — do not move title/subtitle up, as they need padding from the canvas top edge too
- Increase the canvas height by the same offset to avoid clipping the bottom

### 35. Mind-Map Connector Endpoints Misaligned with Nodes

**Problem:** In radial mind-maps, connector Q-curve endpoints are calculated independently from node positions, causing lines to miss their target nodes by 10-60px — creating visible gaps or lines that terminate in empty space.

**Fix:**
- Each connector MUST start at the parent node's card edge and end at the child node's card edge
- Calculate edge intersection: for a card at `(cx, cy)` with half-width `hw` and half-height `hh`, find the exit/entry point on the edge closest to the other node
- For Q curves: the control point should lie roughly along the radial direction, between parent and child
- **Verify** after placing: does the path's start coordinate touch the parent card boundary? Does the end coordinate touch the child card boundary?

### 36. Mind-Map Sibling Node Overlap

**Problem:** In a radial mind-map, sibling nodes at the same depth can overlap when their angular separation is too small relative to card size. Common at level 2 where nodes are closely spaced (e.g., Constellation DAG overlapping Multi-device by 6-8px).

**Fix:**
- After placing all nodes, check every pair of siblings for bounding-box overlap
- If overlap detected, push the overlapping node outward along its radial direction, or increase the angular spread
- Minimum gap between any two cards: **4px** (visual separation without wasted space)
- For horizontally adjacent nodes (e.g., a level-1 node and its inline level-2 child like UFO² ↔ AppAgent), ensure `parent_right_edge + 10px ≤ child_left_edge`

### 37. Q-Curve Loop-Back When Start and End X Are Nearly Equal

**Problem:** When a connector's start-x and end-x are nearly identical (< 5px difference) but the control point is offset in x, the Q curve creates a visible loop or bump instead of a smooth connection. Example: Galaxy right edge (683) → Orchestrator left edge (679) with control point at (710, 182) creates a rightward bulge then loops back.

**Fix:**
- If start-x ≈ end-x (within 10px), do NOT use a control point that pushes far in x — the curve will loop back
- Instead, choose a different connection strategy:
  - Connect from the **top/bottom edge** of one node to the **top/bottom edge** of the other
  - Use a control point along the y-axis (vertical direction) rather than x-axis
- Rule of thumb: the control point should ALWAYS lie **between** the start and end in BOTH x and y, or at most slightly beyond in ONE axis

### 38. Mind-Map: Central Node IS the Title

**Problem:** Adding a separate title/subtitle text above a mind-map wastes vertical space and duplicates information — the central node already serves as the diagram's title.

**Fix:**
- For mind-map type diagrams, do NOT generate a top-level title/subtitle text element
- The central node's label is the title
- If additional context is needed, add it as a `<desc>` metadata element (not rendered)

### 39. Legend Colors Must Match Diagram Content

**Problem:** Legend uses specific colors (e.g., amber, orange) that don't correspond to any actual element in the diagram. Each branch has its own color, but the legend shows unrelated colors.

**Fix:**
- If the legend illustrates a property like **line thickness** or **dash pattern**, use a neutral color (e.g., `#9ca3af` gray) so the legend isn't confused with a branch color
- If the legend maps colors to meaning, each legend entry must use the EXACT same color as the corresponding diagram elements
- Label the legend title to match what it actually shows (e.g., "Line Weight" not "Hierarchy" when showing thickness)

### 40. Network Topology: Zone Labels Covered by Device Icons

**Problem:** Subnet zone labels (e.g., "CORPORATE LAN", "DMZ") are placed at the same y-position as device icons, causing device nodes to render on top and obscure the text.

**Fix:**
- Zone boxes should start **≥ 30px** above the device layer to leave room for labels
- Place zone label text **inside the zone box but above devices** — ensure at least 20px vertical gap between label baseline and device top edge
- If needed, push all devices down uniformly and expand the canvas height to compensate

### 41. Network Topology: Prefer Simple Star Lines Over Edge Bundling

**Problem:** Complex edge-bundling (horizontal bars, junction dots, fan-out patterns) makes network topology diagrams look cluttered and hard to read, especially when combined with VPN overlay curves that cross the physical links.

**Fix:**
- For network topology, use **direct straight lines** from the central hub (router/switch) to each end device — a standard star topology layout
- Follow TD routing rules: exit **bottom center** of router, enter **top center** of each device
- Avoid adding VPN overlay curves on top of physical links — if VPN must be shown, consider using a separate annotation or label rather than additional crossing lines
- Edge bundling is better suited for **dependency** diagrams where many edges share a common path; network topology benefits from visual clarity over line consolidation

### 42. Network Topology: One Link Per Subnet, Not Per Device

**Problem:** When using intermediate structures (bars, trunks), each individual device gets its own drop line from the main bar, but logically a subnet should receive a single entry link that branches internally.

**Fix:**
- If using edge bundling (not recommended per Pitfall #41, but if needed): route **one drop** to each subnet's center, then add an **internal fan-out** within the subnet to individual devices
- Standalone devices (not in any subnet) get a direct link
- This matches actual network semantics: a router connects to a network segment, not to each individual host
