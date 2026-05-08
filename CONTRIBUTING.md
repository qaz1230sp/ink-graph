# Contributing to Ink-Graph

Thank you for your interest in Ink-Graph! This project exists to help AI assistants generate polished, valid, presentation-ready SVG technical diagrams, and contributions of all sizes are welcome.

Ink-Graph currently supports 11 themes, 14 diagram types, and a rich reference system that guides layout, styling, animation, and validation. The best contributions improve visual clarity, keep SVG output valid, and make the references easier for agents and humans to follow.

## Ways to Contribute

- 🐛 Report visual bugs (edge crossing nodes, spacing issues, clipping, overlap, broken markers, invalid SVG)
- 🎨 Add new themes
- 📊 Add new diagram types
- 📏 Improve layout rules
- 📝 Add to the pitfalls database
- 📖 Improve documentation

## Project Structure at a Glance

- `SKILL.md` — core skill instructions and supported theme/type list
- `references/style-*.md` — theme source-of-truth files
- `references/style-selection.md` — theme recommendation matrix
- `references/layout-rules.md` — spacing, routing, and per-type layout guidance
- `references/shapes.md` — reusable node shape definitions
- `references/animations.md` — animation defaults and snippets
- `references/pitfalls.md` — known visual failure modes and fixes
- `samples/` — example SVG outputs
- `scripts/validate_svg.py` — SVG validation helper

## Reporting Visual Bugs

When reporting SVG rendering issues:

1. Include the SVG file or a screenshot
2. Describe what is wrong (for example, "edge passes through node X" or "arrowhead is hidden under the node")
3. Note which browser and version you are using
4. If possible, describe what you expected to see instead
5. Mention the theme and diagram type if you know them

The more concrete your report is, the faster it is to reproduce and fix.

## Adding a New Theme

This is the most common reference contribution. Please follow these steps closely.

### 1. Choose a theme name

Use a lowercase, hyphenated identifier such as `ocean-breeze` or `glass-noir`.

Your theme file and sample names should use that exact ID consistently:

- `references/style-{name}.md`
- `samples/{name}-architecture.svg`

### 2. Create the style reference

Create `references/style-{name}.md` and follow the exact structure used by existing style files such as `references/style-comic-pop.md`.

Keep the section order the same and include all required sections:

1. Title and short design intent
2. `## Colors` table with `Token | Value | Usage`
3. `## Typography`
4. `## Node Styles` with CSS snippet
5. `## Filter / Effect Definitions` with SVG snippets
6. `## Arrow Markers` with SVG snippets
7. `## Edge Styles` with CSS snippet
8. `## Animation Config` table
9. `## CSS Variables Block`
10. `## Complete Style Block Example` with a full `<style>` block ready to copy
11. Paired full `<defs>` block ready to copy
12. Background rect instructions
13. `## Usage Notes`

### 3. Follow the reference file style guide

Reference files are copied very literally by agents, so completeness matters.

- Use exact hex colors — write `#ff4444`, not `red`
- Include complete CSS and SVG defs blocks, not partial fragments
- Document every filter, marker, pattern, and reusable visual effect
- Keep token names aligned with the existing color system where possible
- Make the design intent explicit so theme selection remains understandable
- If the theme uses animation, define it clearly and keep it restrained

### 4. Update `references/style-selection.md`

Add the new theme in both places:

- **Quick Decision** table — explain when the theme should be selected
- **Diagram Type Affinity** matrix — list the diagram types it works best with, and anything it should avoid

Be specific. This matrix is how an agent decides whether the theme is a good fit.

### 5. Update `SKILL.md`

Add the theme to the available themes list in `SKILL.md` so the skill advertises it as a supported option.

If the theme has a particularly strong use case, keep the short description practical and easy to route from user requests.

### 6. Generate at least one sample

At minimum, add:

- `samples/{name}-architecture.svg`

If the theme has special strengths, adding one or two extra samples is even better.

Samples should demonstrate that the theme works in a real diagram, not just in theory.

### 7. Validate the sample output

Before opening a PR, validate any new or changed SVGs.

```bash
python scripts/validate_svg.py samples/*.svg
```

If you generated a one-off output while testing, validate that too:

```bash
python scripts/validate_svg.py your-output.svg
```

### 8. Submit a PR

Include:

- The new `references/style-{name}.md` file
- Updated `references/style-selection.md`
- Updated `SKILL.md`
- At least one sample SVG
- A short explanation of the theme's design intent and where it works well

## Adding a New Diagram Type

When introducing a new diagram type, update the supporting references together so the type is actually usable.

1. **Update `references/shapes.md`** — add any new node shapes or structural primitives the type needs
2. **Update `references/layout-rules.md`** — define direction, spacing, routing, and type-specific layout rules
3. **Update `references/animations.md`** — add sensible animation defaults, or explicitly document why animation should stay minimal
4. **Update `references/style-selection.md`** — add the new type to the affinity matrix
5. **Update `SKILL.md` if needed** — make sure the supported diagram type list stays current
6. **Generate samples** — create examples in 2–3 different themes
7. **Validate the SVGs** — run the validator before submitting
8. **Submit a PR** with the reference changes and samples

## Improving Layout Rules

`references/layout-rules.md` is where spacing, direction, routing, legend placement, and diagram-type defaults are documented.

If you find a better layout pattern:

1. Test the rule by generating 2–3 diagrams
2. Capture the before/after improvement in your PR description
3. Update the rule text so it is explicit and reusable
4. Include sample SVGs when the visual difference matters

Good layout contributions make diagrams easier to read without requiring manual cleanup.

## Adding Pitfalls

`references/pitfalls.md` catalogs real visual issues and their fixes. Add to it when you discover a repeatable failure mode.

Follow the established format:

```markdown
### N. Short Description
**Problem:** What goes wrong
**Fix:** How to prevent or fix it
```

Tips:

- Keep each entry concrete and actionable
- Include example symptoms when helpful
- Mention selectors, coordinates, layer-order issues, or transform pitfalls when relevant
- Prefer real failure modes over hypothetical advice

## Improving Documentation

Documentation improvements are always welcome, especially if they make the project easier to adopt or contribute to.

Useful documentation contributions include:

- Clarifying theme-selection behavior
- Explaining diagram-type differences
- Expanding setup or validation instructions
- Improving examples in `README.md`, `docs/`, or `references/`

## Development Setup

```bash
# Clone the repository
git clone https://github.com/qaz1230sp/ink-graph.git
cd ink-graph

# Validate all existing samples
python scripts/validate_svg.py samples/*.svg

# Generate a test diagram (requires an AI assistant with Ink-Graph installed)
# Then validate your output:
python scripts/validate_svg.py your-output.svg
```

## Contribution Principles

- Keep output valid SVG first
- Preserve the project's pure SVG + CSS approach
- Favor readability over decorative complexity
- Make reference files copy-paste complete
- Update samples when visual behavior changes
- Keep changes focused and easy to review

## Code of Conduct

Be kind, constructive, and focused on improving the project. We welcome contributions from everyone.

## Questions?

Open an issue if you have questions about contributing. We're happy to help.
