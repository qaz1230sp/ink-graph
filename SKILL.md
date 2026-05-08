---
name: ink-graph
description: Use when the user asks to draw, generate, visualize, or export a technical diagram as SVG/PNG — architecture, flowchart, data-flow, sequence, dependency, class, ER, state, component, network, timeline, comparison, use-case, or mind-map diagrams. Triggers on "画图", "帮我画", "架构图", "流程图", "数据流", "可视化", "出图", "generate diagram", "draw diagram", "visualize", or codebase visualization requests.
---

# Ink-Graph

Generate polished SVG technical diagrams that feel presentation-ready. Combines disciplined classification, layout rules, theme selection, reusable SVG patterns, CSS/SMIL animation, and validation-first output.

## When to Use

Use for explicit diagram requests or when a diagram would materially clarify a system, process, data movement, interaction sequence, or dependency structure.

Do not use when the user only wants textual explanation, code changes, or debugging — unless they ask for visualization.

## Core Output Contract

1. **Valid SVG first.** Beauty never comes before validity.
2. **Readable without zooming** at typical browser width.
3. **Consistent visual language** within a single diagram.
4. **Animation used with restraint.** Motion should clarify flow, not create noise.
5. **Deliver both SVG and PNG** when export tooling is available.
6. **Never deliver an invalid SVG.** If validation fails repeatedly, stop and report failure.

## Workflow

Follow this workflow in order. Do not skip validation.

### 1. Understand Request

Extract: diagram type, title, nodes, edges, groups, direction preference, theme preference, special constraints (print-safe, no animation, etc.).

**Diagram type classification:**

| Type | Key Signals |
|------|-------------|
| architecture | systems, services, layers, APIs, tiers, microservices |
| flowchart | steps, branching, if/else, decisions, approvals |
| data-flow | data movement, ETL, pipeline, stream, input/output |
| sequence | ordered messages, request/response, timing, interactions |
| dependency | imports, packages, module coupling, depends-on |
| mind-map | brainstorm, concepts, topics, hierarchy, exploration |
| timeline | milestones, phases, schedule, history, roadmap, gantt |
| network-topology | servers, routers, switches, subnets, devices, infrastructure |
| comparison | versus, compare, pros/cons, features, trade-offs |
| class-diagram | OOP, classes, inheritance, interfaces, methods, UML |
| er-diagram | entities, relationships, tables, fields, cardinality, database schema |
| use-case | actors, use cases, system boundary, includes, extends |
| state-machine | states, transitions, events, guards, initial/final state |
| component | components, interfaces, ports, provided/required, packages |

Direction defaults per type are in `references/layout-rules.md`.

**Classification priority** when ambiguous: sequence > state-machine > flowchart > data-flow > dependency > class-diagram > architecture (default).

#### V2: Code Repository Analysis

If the user asks to **visualize a codebase or repository** (triggers: "对这个项目生成架构图", "visualize this codebase", "show module dependencies from code", "画出代码结构"):

1. Read `prompts/code-analysis.md` for the full scanning and analysis procedure
2. Execute the 3-phase scan: orientation → structural scan → relationship discovery
3. Apply complexity management rules (collapse, omit tests/generated files, target 6-15 nodes)
4. Produce the graph JSON structure
5. Continue with step 2 (theme selection) and the normal generation workflow

**Default theme for code-generated diagrams:** dark-tech (unless user specifies otherwise).

If underspecified, make the smallest reasonable assumptions and keep the structure simple.

### 2. Select Theme

- If user names a theme → use it.
- Otherwise → auto-select using `references/style-selection.md`.
- Load the matching `references/style-{name}.md` for exact colors, CSS, markers.

Available themes: `modern-light` (default), `dark-tech`, `blueprint`, `warm-minimal`, `monochrome` (no animation), `neon-cyber`, `comic-pop`, `retro-terminal`, `papercraft`, `hud-hologram`, `starfield`.

### 3. Plan Layout

- **≤8 nodes:** Follow `references/layout-rules.md`, place manually.
- **>8 nodes:** Build graph JSON → `python scripts/layout.py --direction {dir}`

For layout JSON contract and usage, see the Layout Call section below.

### 4. Load Components

**CRITICAL: You MUST read and follow the reference files — do not generate from memory alone.**

Load these files and apply their rules literally:
- `references/layout-rules.md` — spacing, routing, direction defaults, legend template **(always load)**
- Active style file (e.g. `references/style-blueprint.md`) — exact colors, CSS, markers, defs **(always load)**
- `references/shapes.md` — node shape SVG snippets (when using specialized shapes)
- `references/animations.md` — animation CSS/SMIL (skip for monochrome)
- `references/pitfalls.md` — when using animation, legends, groups, complex routing, or after any failure

### 5. Generate SVG

Build SVG as a list/string builder to prevent truncation. Write complete file with `utf-8` encoding.

**Layer order** (strict): background rect → `<defs>` → `<style>` → groups → edges → nodes → floating labels.

**Rules:**
- Every tag properly closed; `viewBox` encompasses all elements + 40px padding
- Text fits in nodes (`char_count × 8px < node_width - 20px`)
- Use `class=` for styling, not inline `style=`
- All `url(#id)` references must have matching `<defs>` entries
- Escape XML-sensitive characters in labels
- Include base accessory styles: `.node-accent`, `.group-title-bar`, `.group-divider` (see `references/shapes.md`)

### 6. Validate

```bash
python scripts/validate_svg.py {file}.svg
```

Validation is mandatory. Do not present SVG as complete if it fails.

### 7. Export PNG

```bash
python scripts/export_png.py {file}.svg
```

### 8. Report

```text
Generated:
- SVG: {path}.svg
- PNG: {path}.png
Notes:
- Theme: {theme-id}
- Diagram type: {type}
- Open the SVG in a browser to view animations.
```

## Edge Types & Semantics

| Type | Visual | Meaning |
|------|--------|---------|
| data | solid + animated flow | Data transfer |
| control | solid | Control flow |
| dependency | dashed | Import / depends-on |
| async | dotted | Async event / notification |

Rules:
- Every edge type used must have a defined marker in `<defs>`.
- Data edges may animate; dependency/async should stay calm.
- Never use four different bright edge colors in a dense diagram unless the style supports it.

## Node & Shape Semantics

Use shape semantics consistently — one dominant shape per object class:
- process/service → rounded rect; decision → diamond; datastore → cylinder
- queue/stream → tube; external system → dashed rect; actor/user → avatar
- group/boundary → container with title bar

For UML, ER, state-machine, use-case, timeline, network, and component-specific shapes, see `references/shapes.md`.

## Text & Sizing

- Label width ≈ `char_count × 8px`; horizontal padding 10px per side
- Max label lines: 2; wrap or widen node if text overflows
- Node labels: 13–15px; sublabels: 11–12px; titles: 20–28px
- Canvas = layout bounds + 40px padding all sides + title/label clearance

## Legend (图例)

Add a legend when 2+ edge types or visual encodings are used.
- **Vertical layout mandatory** — one entry per row, never horizontal
- **Enclosed in a rounded-rect panel** — semi-transparent fill + subtle border (see template below)
- Include only edge types actually used in the diagram
- Match line styles (solid/dashed/dotted, color, marker) exactly
- Position: bottom-left inside viewBox (20px margin), or bottom-right if bottom-left conflicts
- Legend text must pass contrast check (min 4.5:1 ratio)

**Legend panel template:**
```svg
<g class="legend" transform="translate({x}, {y})">
  <rect class="legend-panel" x="-12" y="-4" width="{w}" height="{h}" rx="8"/>
  <text class="legend-title" x="0" y="14">Legend</text>
  <!-- Entry 1: visual center at y=36 -->
  <line x1="0" y1="36" x2="40" y2="36" class="{edge-class-1}"/>
  <text class="legend-text" x="52" y="36" dominant-baseline="middle">{label1}</text>
  <!-- Entry N: visual center at y = 36 + (n-1) × 24 -->
</g>
```
- **Entry spacing: 24px between visual centers** (not top edges)
- Panel sizing: width = max_label_width + 80, height = 24 + entries × 24 + 8
- `.legend-panel`: `fill: rgba(bg, 0.6); stroke: accent; stroke-width: 1; rx: 8`
- When entries have different icon heights (line=2px, rect=16px, cylinder=16px), align text `dominant-baseline="middle"` to the icon's vertical center

Full sizing rules in `references/layout-rules.md`.

## Layout Call Format

For large diagrams (>8 nodes):

```bash
echo '{"direction":"TD","nodes":[{"id":"a","label":"API","width":160,"height":50}],"edges":[{"source":"a","target":"b"}],"groups":[]}' | python scripts/layout.py --direction TD
```

Input/output JSON contracts are documented in `references/layout-rules.md`.

Rules:
- Provide stable IDs with realistic widths/heights
- Use returned coordinates as baseline
- Recompute viewBox with 40px padding after layout
- Route edges so arrowheads terminate **8px before** node borders (nodes render above edges, so the path must be shortened to prevent overlap)

## Animation Policy

Animation enhances understanding; it is not the main content.

- Default: subtle opacity entrance only
- Animate primary data-flow edges when it aids comprehension
- Disable for monochrome, print-safe, compliance, or dense diagrams (dependency/class/ER)
- Max two motion systems per diagram
- CSS preferred over SMIL; durations: `0.3s–0.8s` entrance, `1.2s–4s` edge flow

Per-type defaults and CSS/SMIL code in `references/animations.md`.

## Validation & Recovery

Before writing the file, run these checks **in order**. Fix any failure before proceeding.

### Coordinate Verification (mandatory)
For every edge path, extract all (x, y) waypoints and verify:
1. **No edge crosses any node interior.** For each path segment, check against every node's bounding box `(x, y, x+w, y+h)`. If any segment intersects a node that is not the source or target, reroute with ≥20px clearance around the node.
2. **Arrowhead visibility.** Path endpoint must be 8px before the target node border (nodes render above edges).
3. **Parallel edge separation.** If two edges share the same x or y corridor (within 10px), offset one by ≥20px to avoid visual overlap.
4. **Fan-out junction clearance.** When multiple edges share a trunk, the junction bar must be ≥20px away from any group border or node edge.

### Layout Verification
5. **Title/content gap** ≥ 30px between subtitle baseline and first node/group top.
6. **Node collision check.** For every pair of nodes, verify bounding boxes do not overlap (min 4px gap).
7. **Edge labels** do not overlap nodes or other labels.

### Legend Verification
8. **Panel encloses all entries** with ≥8px padding on all sides.
9. **Equal visual spacing** between legend entries — measure from visual center of each icon/line, ensure ≈24px uniform gaps. When entries have different heights (line vs rect vs cylinder), space by visual center, not by top edge.
10. **Colors match** the actual edge/node styles used in the diagram.

### General
- viewBox large enough (all nodes + 40px margin)
- All tags closed; all `url(#id)` have matching `<defs>`
- Text fits in nodes; no overlapping nodes
- Title and reading flow obvious in 3 seconds

**Avoid:** half-finished SVG, arbitrary positions without alignment, over-animation, inline `style=`, tiny text, edges through nodes, decorative gradients reducing contrast.

**Recovery:** Strike 1 → fix and re-validate. Strike 2 → simplify (reduce animation, expand canvas). Strike 3 → STOP, report failure. Never deliver an invalid SVG.

## Common Pitfalls

Top-priority checks (apply always):
1. **CSS transform overrides SVG positioning** (#1, #9) — use opacity-only animation on positioned `<g>`
2. **Arrowheads hidden under nodes** (#2) — end paths 8px before target border
3. **Edges through intermediate nodes** (#3, #10) — for EVERY edge path, check all waypoints against all node bounding boxes; reroute with 20px clearance
4. **Title/content overlap** (#20, #34) — min 30-40px gap below subtitle
5. **Legend issues** (#12, #14, #39) — vertical layout, panel-enclosed, 24px visual-center spacing, matching colors
6. **Coordinate mismatches** (#22, #24) — always verify `parent_translate + local = absolute`
7. **Parallel edges overlap** — if two edges share the same x or y corridor, offset by ≥20px
8. **Fan-out junction too close to group border** — junction bar must be ≥20px from any group/node edge
9. **Legend entry spacing uneven** — measure by visual center of each icon (line, rect, cylinder differ in height)

Read `references/pitfalls.md` (42 pitfalls) when using animation, legends, groups, complex routing, >8 nodes, or after any validation/visual failure.
