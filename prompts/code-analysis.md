# Code Repository Analysis → Diagram Structure

## When to Use

When the user asks to:
- "visualize this codebase"
- "generate architecture diagram from code"
- "show me the module dependencies"
- "draw data flow for this project"
- "画出这个项目的架构"
- "可视化代码结构"
- "对这个项目生成架构图"

## Scanning Strategy

### Phase 1: Quick Orientation (≤30 seconds)

Read these first to understand project shape:
1. **Root files**: README.md, package.json, pyproject.toml, go.mod, Cargo.toml, pom.xml
2. **Directory listing**: top-level + one level deep (`ls -la`, `tree -L 2`)
3. **Config files**: docker-compose.yml, .env.example, Makefile, tsconfig.json

This gives you: language, framework, entry points, rough module count.

### Phase 2: Structural Scan (≤2 minutes)

Based on Phase 1 findings:
1. **Entry points**: main/index files, app bootstrap, route definitions
2. **Module boundaries**: directories with their own index/init files, package.json workspaces
3. **Data layer**: database schemas, ORM models, migration files
4. **External integrations**: API clients, SDK imports, webhook handlers
5. **Config/infra**: CI/CD files, Dockerfile, infrastructure-as-code

### Phase 3: Relationship Discovery

For each identified module:
1. **Imports/requires**: what does it depend on?
2. **Exports/public API**: what does it expose?
3. **Communication patterns**: HTTP calls, events, shared state, file I/O

**Stop scanning when you have 6-15 significant nodes.** Do not exhaustively map every file.

## Complexity Management

| Repository Size | Strategy |
|----------------|----------|
| Small (≤20 files) | Map all significant modules directly |
| Medium (20-100 files) | Group by directory/domain, 1 node per domain area |
| Large (100+ files) | Focus on top-level architecture only; each major subsystem = 1 node |
| Monorepo | Each package/workspace = 1 node; show inter-package dependencies |

**Collapse rules:**
- Multiple files in same directory serving same purpose → 1 node
- Utility/helper files → omit unless architecturally significant
- Test files → omit
- Generated files → omit
- Config variants (dev/staging/prod) → 1 node labeled "Config"

## Instructions for Analysis

Analyze the repository and identify:

### 1. Entry Points & Boundaries
- Main entry files (index.ts, main.py, App.tsx, etc.)
- Package/module boundaries
- Public API surfaces

### 2. Components & Nodes
For each significant component, determine:
- **id**: kebab-case identifier
- **label**: human-readable name (short, ≤20 chars)
- **type**: one of: service, database, queue, gateway, external, file, user, process
- **layer**: logical layer (presentation, api, business, data, infrastructure, external)

### 3. Relationships & Edges
For each relationship, determine:
- **source**: source node id
- **target**: target node id
- **label**: brief description of the relationship (optional, ≤15 chars)
- **type**: one of: data, control, dependency, async

### 4. Groupings
Identify logical groups:
- **id**: group identifier
- **label**: group name
- **members**: list of node ids in this group

## Node Type Mapping

| Code Pattern | Node Type |
|-------------|-----------|
| Source files, modules, classes | process |
| Database connections, ORMs, models | database |
| API endpoints, routers, controllers | gateway |
| External services, third-party APIs | external |
| Config files, environment, secrets | file |
| Message queues, event buses, pub/sub | queue |
| UI components, views | process |
| Users, actors mentioned in comments/docs | user |

## Edge Type Mapping

| Code Pattern | Edge Type |
|-------------|-----------|
| import/require statements | dependency |
| Function calls, method invocations | control |
| HTTP requests, API calls, data queries | data |
| Event emitters, message publishing, callbacks | async |

## Output Format

Output a single JSON object as an **internal intermediate artifact**. Do not return it to the user unless explicitly asked — continue into the normal CodeGraph SVG generation workflow (step 2: theme selection).

```json
{
  "title": "Project Name — Architecture",
  "type": "architecture",
  "direction": "TD",
  "nodes": [
    { "id": "api-gateway", "label": "API Gateway", "type": "gateway", "layer": "api" },
    { "id": "user-service", "label": "User Service", "type": "service", "layer": "business" },
    { "id": "postgres", "label": "PostgreSQL", "type": "database", "layer": "data" },
    { "id": "redis", "label": "Redis Cache", "type": "queue", "layer": "data" },
    { "id": "auth0", "label": "Auth0", "type": "external", "layer": "external" }
  ],
  "edges": [
    { "source": "api-gateway", "target": "user-service", "label": "REST", "type": "data" },
    { "source": "user-service", "target": "postgres", "label": "queries", "type": "data" },
    { "source": "user-service", "target": "redis", "label": "cache", "type": "data" },
    { "source": "api-gateway", "target": "auth0", "label": "verify", "type": "control" }
  ],
  "groups": [
    { "id": "backend", "label": "Backend Services", "members": ["api-gateway", "user-service"] },
    { "id": "storage", "label": "Storage Layer", "members": ["postgres", "redis"] }
  ]
}
```

## Analysis Guidelines

- **Keep it high-level.** Don't map every file — focus on architecturally significant components.
- **Target 6-15 nodes** for readability. Collapse similar files into one logical node.
- **Prefer fewer edges** that show important relationships over exhaustive import mapping.
- **Use layers** to suggest vertical positioning (presentation at top, data at bottom).
- **Group by domain** not by technical type (e.g., group "Auth" together, not "all databases").

## Diagram Type Selection

Based on what the user asks for:
- "architecture" / "架构" → type: "architecture", direction: "TD"
- "data flow" / "数据流" → type: "data-flow", direction: "LR"
- "dependencies" / "依赖" → type: "dependency", direction: "TD"
- "module structure" → type: "dependency", direction: "TD"
- "flowchart" / "流程" → type: "flowchart", direction: "TD"
- "sequence" / "时序" → type: "sequence", direction: "TD"

**If user says "visualize" without specifying type:**
- Projects with clear layers (frontend/backend/DB) → architecture
- Libraries/packages with import trees → dependency
- Event-driven or pipeline projects → data-flow

## Per-Type Analysis Examples

### Architecture (from a typical web project)

Focus on: services, layers, external integrations, databases.

```json
{
  "title": "E-Commerce Platform — Architecture",
  "type": "architecture",
  "direction": "TD",
  "nodes": [
    { "id": "web-app", "label": "React App", "type": "process", "layer": "presentation" },
    { "id": "api-gw", "label": "API Gateway", "type": "gateway", "layer": "api" },
    { "id": "auth-svc", "label": "Auth Service", "type": "service", "layer": "business" },
    { "id": "order-svc", "label": "Order Service", "type": "service", "layer": "business" },
    { "id": "postgres", "label": "PostgreSQL", "type": "database", "layer": "data" },
    { "id": "redis", "label": "Redis", "type": "queue", "layer": "data" },
    { "id": "stripe", "label": "Stripe", "type": "external", "layer": "external" }
  ],
  "edges": [
    { "source": "web-app", "target": "api-gw", "label": "HTTP", "type": "data" },
    { "source": "api-gw", "target": "auth-svc", "label": "verify", "type": "control" },
    { "source": "api-gw", "target": "order-svc", "label": "REST", "type": "data" },
    { "source": "order-svc", "target": "postgres", "label": "queries", "type": "data" },
    { "source": "auth-svc", "target": "redis", "label": "sessions", "type": "data" },
    { "source": "order-svc", "target": "stripe", "label": "payments", "type": "data" }
  ],
  "groups": [
    { "id": "services", "label": "Backend", "members": ["auth-svc", "order-svc"] },
    { "id": "storage", "label": "Data Layer", "members": ["postgres", "redis"] }
  ]
}
```

### Dependency (from a library/package project)

Focus on: module imports, package relationships, coupling.

```json
{
  "title": "CLI Tool — Module Dependencies",
  "type": "dependency",
  "direction": "TD",
  "nodes": [
    { "id": "cli", "label": "CLI Entry", "type": "process", "layer": "presentation" },
    { "id": "commands", "label": "Commands", "type": "process", "layer": "api" },
    { "id": "config", "label": "Config", "type": "file", "layer": "business" },
    { "id": "renderer", "label": "Renderer", "type": "process", "layer": "business" },
    { "id": "validator", "label": "Validator", "type": "process", "layer": "business" },
    { "id": "fs-utils", "label": "FS Utils", "type": "file", "layer": "infrastructure" }
  ],
  "edges": [
    { "source": "cli", "target": "commands", "type": "dependency" },
    { "source": "commands", "target": "config", "type": "dependency" },
    { "source": "commands", "target": "renderer", "type": "dependency" },
    { "source": "commands", "target": "validator", "type": "dependency" },
    { "source": "renderer", "target": "fs-utils", "type": "dependency" },
    { "source": "validator", "target": "config", "type": "dependency" }
  ],
  "groups": [
    { "id": "core", "label": "Core Modules", "members": ["config", "renderer", "validator"] }
  ]
}
```

### Data-Flow (from a pipeline/event-driven project)

Focus on: data producers, processors, storage, consumers.

```json
{
  "title": "Analytics Pipeline — Data Flow",
  "type": "data-flow",
  "direction": "LR",
  "nodes": [
    { "id": "events", "label": "Event Stream", "type": "queue", "layer": "presentation" },
    { "id": "ingester", "label": "Ingester", "type": "process", "layer": "api" },
    { "id": "transformer", "label": "Transformer", "type": "process", "layer": "business" },
    { "id": "warehouse", "label": "Data Warehouse", "type": "database", "layer": "data" },
    { "id": "dashboard", "label": "Dashboard", "type": "process", "layer": "presentation" }
  ],
  "edges": [
    { "source": "events", "target": "ingester", "label": "raw events", "type": "async" },
    { "source": "ingester", "target": "transformer", "label": "batched", "type": "data" },
    { "source": "transformer", "target": "warehouse", "label": "enriched", "type": "data" },
    { "source": "warehouse", "target": "dashboard", "label": "queries", "type": "data" }
  ],
  "groups": [
    { "id": "processing", "label": "Processing", "members": ["ingester", "transformer"] }
  ]
}
```

## After Analysis

Once you have the JSON structure, proceed with the normal CodeGraph workflow:
1. Select theme (dark-tech recommended for code-generated diagrams, unless user specifies)
2. If >8 nodes: call `python3 scripts/layout.py --direction {dir}` with the JSON
3. If ≤8 nodes: plan layout manually per `references/layout-rules.md`
4. Generate SVG following SKILL.md instructions
5. Validate with `python scripts/validate_svg.py`
