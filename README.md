# Ink-Graph

> AI Agent Skill for generating beautiful, animated SVG technical diagrams

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/ink-graph.svg)](https://www.npmjs.com/package/ink-graph)

[English](README.md) | [中文](README.zh.md)

Ink-Graph is an open-source AI Agent Skill that turns natural language descriptions into polished, presentation-ready SVG diagrams. It works with any AI coding assistant that supports skill/prompt loading — including GitHub Copilot CLI, Claude Code, Cursor, and more.

No JavaScript runtime. No external rendering engine. Just pure SVG + CSS animation that works in any modern browser.

---

## 🎨 Theme Gallery

All 11 themes applied to the same architecture diagram:

<table>
<tr>
<td align="center"><strong>Modern Light</strong><br/><img src="samples/modern-light-architecture.svg" width="260"/></td>
<td align="center"><strong>Dark Tech</strong><br/><img src="samples/dark-tech-architecture.svg" width="260"/></td>
<td align="center"><strong>Blueprint</strong><br/><img src="samples/ufo3-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>Warm Minimal</strong><br/><img src="samples/warm-minimal-architecture.svg" width="260"/></td>
<td align="center"><strong>Monochrome</strong><br/><img src="samples/monochrome-architecture.svg" width="260"/></td>
<td align="center"><strong>Neon Cyber</strong><br/><img src="samples/neon-cyber-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>Comic Pop</strong><br/><img src="samples/comic-pop-architecture.svg" width="260"/></td>
<td align="center"><strong>Retro Terminal</strong><br/><img src="samples/retro-terminal-architecture.svg" width="260"/></td>
<td align="center"><strong>Paper Craft</strong><br/><img src="samples/papercraft-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>HUD Hologram</strong><br/><img src="samples/hud-hologram-architecture.svg" width="260"/></td>
<td align="center"><strong>Starfield</strong><br/><img src="samples/starfield-architecture.svg" width="260"/></td>
<td></td>
</tr>
</table>

## 📊 Diagram Types

Different diagram types, each with a theme that best suits it:

<table>
<tr>
<td align="center"><strong>Flowchart</strong><br/><sub>Paper Craft</sub><br/><img src="samples/papercraft-flowchart.svg" width="260"/></td>
<td align="center"><strong>Data Flow</strong><br/><sub>Dark Tech</sub><br/><img src="samples/dark-tech-data-flow.svg" width="260"/></td>
<td align="center"><strong>Sequence</strong><br/><sub>HUD Hologram</sub><br/><img src="samples/hud-hologram-sequence.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>Mind Map</strong><br/><sub>Comic Pop</sub><br/><img src="samples/comic-pop-mindmap.svg" width="260"/></td>
<td align="center"><strong>Dependency</strong><br/><sub>Monochrome</sub><br/><img src="samples/monochrome-dependency.svg" width="260"/></td>
<td></td>
</tr>
</table>

## ✨ Features

- **11 professional themes** — from clean corporate to sci-fi HUD
- **14 diagram types** — architecture, flowchart, data-flow, sequence, dependency, mind-map, class, ER, state-machine, component, network-topology, timeline, comparison, use-case
- **CSS/SMIL animation** — edge flow, hover glow, entrance effects, CRT flicker
- **Code repository analysis** — generate diagrams directly from your codebase (v2)
- **Zero JavaScript** — pure SVG + CSS, works in any browser
- **SVG + PNG output** — with optional PNG export via librsvg

## 🚀 Quick Start

### Installation

Choose the method that matches your AI tool:

**npm (Recommended)**
```bash
npm install -g ink-graph
```

**GitHub Copilot CLI**
```bash
git clone https://github.com/qaz1230sp/ink-graph.git ~/.agents/skills/ink-graph
```

**Claude Code**
```bash
# Option 1: npm
npm install ink-graph
# Then add to .claude/settings.json:
# { "permissions": { "allow": ["skill:ink-graph"] } }

# Option 2: git clone
git clone https://github.com/qaz1230sp/ink-graph.git ~/ink-graph
```

**Cursor**
```bash
git clone https://github.com/qaz1230sp/ink-graph.git ~/ink-graph
# Add the SKILL.md path to Cursor's custom instructions or rules
```

**Any AI Tool (Manual)**
```
Copy the contents of SKILL.md into your AI assistant's system prompt,
custom instructions, or knowledge base. The references/ directory
contains theme definitions the AI will read when generating diagrams.
```

### Your First Diagram

Just describe what you want in natural language:

```text
> Draw an architecture diagram with: React frontend, Node.js API,
  PostgreSQL database, and Redis cache. Use dark-tech theme.
```

```text
> 画一个微服务架构图，包含API网关、用户服务、订单服务和数据库
```

```text
> Visualize this data pipeline: Kafka → Flink → Data Warehouse → Dashboard
```

```text
> Draw a flowchart for user registration: signup → validate email →
  create account → send welcome email
```

The AI reads SKILL.md, selects a theme, loads reference files, and generates a complete SVG file.

### Generate from Code

Point the AI at your codebase for automatic analysis:

```text
> Analyze this project and generate an architecture diagram

> 对这个项目生成数据流图
```

## 🎭 Themes

| Theme | Style | Best For |
|-------|-------|----------|
| **modern-light** | Clean, balanced, strong readability | Product docs, presentations |
| **dark-tech** | Dark canvas, luminous accents | Platform diagrams, AI/infra systems |
| **blueprint** | Precise engineering-document look | Technical specs, design docs |
| **warm-minimal** | Soft palette, friendly tone | Blog visuals, explainer docs |
| **monochrome** | Grayscale, zero animation | Print/PDF, compliance, archival |
| **neon-cyber** | High-contrast futuristic glow | Demos, showcases, marketing |
| **comic-pop** | Bold outlines, halftone dots, comic font | Hackathons, fun presentations |
| **retro-terminal** | CRT green phosphor, scanlines | Geek talks, CLI tool docs |
| **papercraft** | Paper cutout, handwritten font | Teaching, casual docs |
| **hud-hologram** | Military HUD, tactical cyan | Sci-fi presentations, tech demos |
| **starfield** | Deep space, nebula, star twinkle | Elegant showcases, cosmic themes |

## 📐 Supported Diagram Types

| Type | Description | Default Direction |
|------|-------------|-------------------|
| **architecture** | Services, layers, APIs, system boundaries | Top-down |
| **flowchart** | Steps, decisions, branches, outcomes | Top-down |
| **data-flow** | Data movement between producers/consumers | Left-right |
| **sequence** | Ordered interactions between actors | Top-down |
| **dependency** | Static relationships between modules | Top-down |
| **mind-map** | Hierarchical concept branching | Radial |
| **class-diagram** | UML classes with attributes/methods | Top-down |
| **er-diagram** | Entity-relationship for databases | Left-right |
| **state-machine** | States and transitions | Left-right |
| **component** | Software components and interfaces | Top-down |
| **network-topology** | Infrastructure and connectivity | Free-form |
| **timeline** | Events along a time axis | Left-right |
| **comparison** | Side-by-side feature/option comparison | Grid |
| **use-case** | Actors and system interactions (UML) | Free-form |

## 📁 Project Structure

```text
ink-graph/
├── SKILL.md                        # Core skill — AI reads this to generate diagrams
├── README.md                       # English docs
├── README.zh.md                    # 中文文档
├── CONTRIBUTING.md                 # Contributing guide
├── LICENSE                         # MIT
├── package.json
├── references/
│   ├── style-*.md (11 files)       # Theme definitions (colors, CSS, SVG defs)
│   ├── style-selection.md          # Theme recommendation matrix
│   ├── layout-rules.md             # Spacing, routing, per-type layout guidance
│   ├── shapes.md                   # Node shape definitions
│   ├── animations.md               # Animation defaults per diagram type
│   └── pitfalls.md                 # 42+ known issues and fixes
├── samples/                        # Example SVGs (themes × diagram types)
├── scripts/
│   ├── validate_svg.py             # SVG validation helper
│   ├── export_png.py               # PNG export helper (requires librsvg)
│   └── layout.py                   # Graphviz-based auto-layout
├── prompts/
│   └── code-analysis.md            # Repository analysis prompt (v2)
└── docs/
    └── getting-started.md          # Usage tutorial
```

## 🔧 Requirements

- An AI coding assistant that supports custom skills/prompts
- A modern browser (for viewing SVG output)
- Python 3.10+ (optional, for `scripts/layout.py` auto-layout)
- Graphviz (optional, for auto-layout of large diagrams)
- librsvg / `rsvg-convert` (optional, for PNG export)

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new themes
- Adding new diagram types
- Improving layout rules and fixing visual bugs
- Strengthening the pitfalls database

## License

MIT
