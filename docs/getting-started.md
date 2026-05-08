# Getting Started with CodeGraph

## What is CodeGraph?

CodeGraph is an open-source AI Agent Skill that turns natural language prompts into polished SVG technical diagrams. It supports 11 visual themes and 14 diagram types, so you can go from “draw this system” to a browser-ready diagram with one prompt.

## Prerequisites

- An AI coding assistant such as GitHub Copilot CLI, Claude Code, Cursor, or any tool that supports custom prompts or skills
- A modern web browser such as Chrome, Firefox, Edge, or Safari for viewing SVG output

## Installation

### GitHub Copilot CLI

Clone the repository into your skills directory:

```bash
git clone https://github.com/anthropics/codegraph.git ~/.agents/skills/codegraph
```

Then ask Copilot to generate a diagram with the CodeGraph skill enabled.

### Claude Code

Clone the repository:

```bash
git clone https://github.com/anthropics/codegraph.git ~/codegraph-skill
```

Allow the skill in your Claude settings:

```json
{
  "permissions": {
    "allow": ["skill:codegraph"]
  }
}
```

Make sure Claude can access the repository files so it can read `SKILL.md` and the `references/` directory.

### Cursor

Clone the repository:

```bash
git clone https://github.com/anthropics/codegraph.git ~/codegraph-skill
```

Add `SKILL.md` to Cursor custom instructions or project rules, and make sure the `references/` directory is available to the assistant during generation.

### Any AI Tool (Manual)

Copy the contents of `SKILL.md` into your AI assistant's system prompt, custom instructions, or equivalent prompt template.

Also make sure the assistant can read the `references/` directory, because CodeGraph uses those files for theme selection, layout, shapes, animation, and output rules.

## Tutorial 1: Your First Diagram

Start with a simple architecture prompt:

```text
Draw an architecture diagram with a web frontend, API server, and database.
```

What happens behind the scenes:

1. The AI reads `SKILL.md`
2. It identifies the diagram type and constraints
3. It selects a theme
4. It reads the matching style reference
5. It generates a complete SVG

Expected result: a clean SVG file saved in your current working directory.

## Tutorial 2: Choosing a Theme

You can let CodeGraph choose automatically, or name a theme directly.

```text
Draw an architecture diagram with a web frontend, API server, and database. Use dark-tech theme.
```

```text
Draw an architecture diagram with a web frontend, API server, and database. Use blueprint theme.
```

```text
画一个前端、API 服务和数据库的架构图，用简洁风格。
```

Theme selection tips:

- No preference: `modern-light` is the default
- Technical audience: `dark-tech` or `blueprint`
- Print or PDF: `monochrome`
- Fun or creative diagrams: `comic-pop` or `papercraft`

For the full theme list, see the [README](../README.md).

## Tutorial 3: Different Diagram Types

Try the same workflow with different prompts:

### Flowchart

```text
Draw a flowchart for user registration: signup → validate email → create account → send welcome email.
```

Best for step-by-step processes, decisions, and approval flows.

### Data Flow

```text
Visualize this data pipeline: Kafka → Processor → Database → Dashboard.
```

Best for pipelines, ETL, streams, and producer/consumer systems.

### Sequence

```text
Draw a sequence diagram for OAuth2 login flow.
```

Best for ordered interactions between users, services, and APIs.

### Mind Map

```text
Create a mind map of machine learning concepts.
```

Best for brainstorming, hierarchies, and topic exploration.

### Dependency

```text
Show the module dependency graph for this project.
```

Best for static relationships between modules, packages, or components.

## Tutorial 4: Generating Diagrams from Code

CodeGraph v2 can generate diagrams from a real repository, not just a written description.

```text
Analyze this project and generate an architecture diagram.
```

```text
对这个代码仓库生成数据流图。
```

How it works:

1. The AI scans the codebase
2. It extracts components, boundaries, and relationships
3. It generates a diagram based on the inferred structure

This requires your AI tool to have access to the code files it should analyze.

## Tutorial 5: Customizing Output

You can refine the output just by extending the prompt.

### Canvas Size

```text
Draw an architecture diagram for this system and use a wider canvas.
```

```text
Draw a flowchart for checkout with a 1600x900 canvas.
```

### Animation

```text
Draw a data-flow diagram with no animation.
```

```text
Use dark-tech theme without animation.
```

Tip: `no animation` automatically maps well to the `monochrome` style.

### Direction

```text
Draw a left-to-right sequence diagram for OAuth login.
```

```text
Draw a top-down architecture diagram for these services.
```

### PNG Export

If `librsvg` is installed, the AI can also export PNG automatically after generating the SVG.

## Tips & Tricks

- Be specific about node names and relationships
- Name the theme directly when you want consistent results
- Chinese prompts work naturally alongside English prompts
- Iterate in follow-up prompts, for example:

```text
Move the database to the right.
```

```text
Change the theme to neon-cyber.
```

## FAQ

**Why SVG instead of PNG?**  
SVG is scalable, animatable, editable, and works natively in modern browsers with no quality loss at any zoom level.

**Can I edit the output?**  
Yes. The output is standard SVG, so you can open it in a text editor or an SVG tool such as Inkscape or Figma.

**How do I add a custom theme?**  
See `CONTRIBUTING.md` for the theme authoring guide.

**Which AI tools are supported?**  
Any AI assistant that can load custom prompts or skills. CodeGraph is tested with GitHub Copilot CLI, Claude Code, and Cursor.

**Does it need internet?**  
No. Everything runs locally. The AI generates the SVG from the skill instructions and reference files.
