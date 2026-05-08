# Ink-Graph

> AI Agent Skill —— 用自然语言生成精美的动画 SVG 技术图

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/ink-graph.svg)](https://www.npmjs.com/package/ink-graph)

[English](README.md) | [中文](README.zh.md)

Ink-Graph 是一个开源的 AI Agent Skill，能够将自然语言描述转化为精美的、可直接用于演示的 SVG 图表。它兼容所有支持 Skill/Prompt 加载的 AI 编程助手 —— 包括 GitHub Copilot CLI、Claude Code、Cursor 等。

无需 JavaScript 运行时，无需外部渲染引擎，纯 SVG + CSS 动画，在任何现代浏览器中都能完美呈现。

---

## 🎨 主题画廊

11 种专业主题，应用于同一架构图的效果：

<table>
<tr>
<td align="center"><strong>Modern Light</strong><br/><sub>现代明亮</sub><br/><img src="samples/modern-light-architecture.svg" width="260"/></td>
<td align="center"><strong>Dark Tech</strong><br/><sub>暗黑科技</sub><br/><img src="samples/dark-tech-architecture.svg" width="260"/></td>
<td align="center"><strong>Blueprint</strong><br/><sub>蓝图</sub><br/><img src="samples/ufo3-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>Warm Minimal</strong><br/><sub>暖色极简</sub><br/><img src="samples/warm-minimal-architecture.svg" width="260"/></td>
<td align="center"><strong>Monochrome</strong><br/><sub>黑白印刷</sub><br/><img src="samples/monochrome-architecture.svg" width="260"/></td>
<td align="center"><strong>Neon Cyber</strong><br/><sub>霓虹朋克</sub><br/><img src="samples/neon-cyber-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>Comic Pop</strong><br/><sub>漫画波普</sub><br/><img src="samples/comic-pop-architecture.svg" width="260"/></td>
<td align="center"><strong>Retro Terminal</strong><br/><sub>复古终端</sub><br/><img src="samples/retro-terminal-architecture.svg" width="260"/></td>
<td align="center"><strong>Paper Craft</strong><br/><sub>纸工艺</sub><br/><img src="samples/papercraft-architecture.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>HUD Hologram</strong><br/><sub>全息HUD</sub><br/><img src="samples/hud-hologram-architecture.svg" width="260"/></td>
<td align="center"><strong>Starfield</strong><br/><sub>星域</sub><br/><img src="samples/starfield-architecture.svg" width="260"/></td>
<td></td>
</tr>
</table>

## 📊 图表类型展示

不同类型的图表，搭配最适合的主题：

<table>
<tr>
<td align="center"><strong>流程图</strong><br/><sub>Paper Craft</sub><br/><img src="samples/papercraft-flowchart.svg" width="260"/></td>
<td align="center"><strong>数据流图</strong><br/><sub>Dark Tech</sub><br/><img src="samples/dark-tech-data-flow.svg" width="260"/></td>
<td align="center"><strong>时序图</strong><br/><sub>HUD Hologram</sub><br/><img src="samples/hud-hologram-sequence.svg" width="260"/></td>
</tr>
<tr>
<td align="center"><strong>思维导图</strong><br/><sub>Comic Pop</sub><br/><img src="samples/comic-pop-mindmap.svg" width="260"/></td>
<td align="center"><strong>依赖图</strong><br/><sub>Monochrome</sub><br/><img src="samples/monochrome-dependency.svg" width="260"/></td>
<td></td>
</tr>
</table>

## ✨ 特性

- **11 种专业主题** —— 从干净的商务风到科幻 HUD 风格
- **14 种图表类型** —— 架构图、流程图、数据流图、时序图、依赖图、思维导图、类图、ER 图、状态机、组件图、网络拓扑、时间线、对比图、用例图
- **CSS/SMIL 动画** —— 边线流动、悬停发光、入场动效、CRT 闪烁等
- **代码仓库分析** —— 直接从代码库生成架构图（v2 规划中）
- **零 JavaScript** —— 纯 SVG + CSS，任何浏览器都能渲染
- **SVG + PNG 输出** —— 可选通过 librsvg 导出 PNG

## 🚀 快速开始

### 安装

选择适合你 AI 工具的安装方式：

**npm 安装（推荐）**
```bash
npm install -g ink-graph
```

**GitHub Copilot CLI**
```bash
git clone https://github.com/qaz1230sp/ink-graph.git ~/.agents/skills/ink-graph
```

**Claude Code**
```bash
# 方式一：npm
npm install ink-graph
# 然后添加到 .claude/settings.json:
# { "permissions": { "allow": ["skill:ink-graph"] } }

# 方式二：git clone
git clone https://github.com/qaz1230sp/ink-graph.git ~/ink-graph
```

**Cursor**
```bash
git clone https://github.com/qaz1230sp/ink-graph.git ~/ink-graph
# 将 SKILL.md 路径添加到 Cursor 的自定义指令或规则中
```

**任意 AI 工具（手动）**
```
将 SKILL.md 的内容复制到你的 AI 助手的系统提示词、
自定义指令或知识库中。references/ 目录包含
AI 生成图表时会读取的主题定义。
```

### 第一张图

用自然语言描述你想要的：

```text
> 画一个微服务架构图，包含 API 网关、用户服务、订单服务和数据库
```

```text
> Draw an architecture diagram with: React frontend, Node.js API,
  PostgreSQL database, and Redis cache. Use dark-tech theme.
```

```text
> 画一个数据管道流程：Kafka → Flink → 数据仓库 → 可视化面板
```

```text
> 画一个用户注册流程图：注册 → 验证邮箱 → 创建账号 → 发送欢迎邮件
```

AI 会读取 SKILL.md，选择合适的主题，加载参考文件，生成完整的 SVG 文件。

### 从代码生成

将 AI 指向你的代码库，自动分析并生成图表：

```text
> 分析这个项目，生成架构图

> Analyze this project and generate an architecture diagram

> 对这个项目生成数据流图
```

## 🎭 主题一览

| 主题 | 风格 | 适用场景 |
|------|------|----------|
| **modern-light** | 清爽、均衡、高可读性 | 产品文档、演示文稿 |
| **dark-tech** | 暗色画布、荧光色调 | 平台架构图、AI/基础设施 |
| **blueprint** | 精确的工程图风格 | 技术规范、设计文档 |
| **warm-minimal** | 温暖配色、友好基调 | 博客配图、解说文档 |
| **monochrome** | 灰度、无动画 | 打印/PDF、合规文档 |
| **neon-cyber** | 高对比度未来感荧光 | 演示、展示、营销材料 |
| **comic-pop** | 粗描边、网点、漫画字体 | 黑客松、趣味演讲 |
| **retro-terminal** | CRT 绿磷光、扫描线 | 极客分享、CLI 工具文档 |
| **papercraft** | 纸片剪贴、手写字体 | 教学、轻松文档 |
| **hud-hologram** | 军事 HUD、战术青色 | 科幻演示、技术 Demo |
| **starfield** | 深空、星云、星光闪烁 | 高端展示、宇宙主题 |

## 📐 支持的图表类型

| 类型 | 描述 | 默认方向 |
|------|------|----------|
| **architecture** | 服务、层级、API、系统边界 | 自上而下 |
| **flowchart** | 步骤、判断、分支、结果 | 自上而下 |
| **data-flow** | 数据在生产者/消费者间的流动 | 从左到右 |
| **sequence** | 角色之间的有序交互 | 自上而下 |
| **dependency** | 模块间的静态依赖关系 | 自上而下 |
| **mind-map** | 层级化的概念分支 | 放射状 |
| **class-diagram** | UML 类图（属性/方法） | 自上而下 |
| **er-diagram** | 数据库 ER 关系图 | 从左到右 |
| **state-machine** | 状态与转换 | 从左到右 |
| **component** | 软件组件与接口 | 自上而下 |
| **network-topology** | 基础设施与连接 | 自由布局 |
| **timeline** | 沿时间轴排列的事件 | 从左到右 |
| **comparison** | 并排的功能/选项对比 | 网格 |
| **use-case** | 参与者与系统交互（UML） | 自由布局 |

## 📁 项目结构

```text
ink-graph/
├── SKILL.md                        # 核心 Skill —— AI 读取此文件生成图表
├── README.md                       # English 文档
├── README.zh.md                    # 中文文档
├── CONTRIBUTING.md                 # 贡献指南
├── LICENSE                         # MIT
├── package.json
├── references/
│   ├── style-*.md (11 个文件)      # 主题定义（配色、CSS、SVG defs）
│   ├── style-selection.md          # 主题推荐矩阵
│   ├── layout-rules.md             # 间距、路由、各类型布局指导
│   ├── shapes.md                   # 节点形状定义
│   ├── animations.md               # 各图表类型的动画默认值
│   └── pitfalls.md                 # 42+ 已知问题与修复方案
├── samples/                        # 示例 SVG（主题 × 图表类型）
├── scripts/
│   ├── validate_svg.py             # SVG 验证工具
│   ├── export_png.py               # PNG 导出工具（需要 librsvg）
│   └── layout.py                   # 基于 Graphviz 的自动布局
├── prompts/
│   └── code-analysis.md            # 代码仓库分析提示词（v2）
└── docs/
    └── getting-started.md          # 使用教程
```

## 🔧 环境要求

- 一个支持自定义 Skill/Prompt 的 AI 编程助手
- 现代浏览器（用于查看 SVG 输出）
- Python 3.10+（可选，用于 `scripts/layout.py` 自动布局）
- Graphviz（可选，用于大型图表的自动布局）
- librsvg / `rsvg-convert`（可选，用于 PNG 导出）

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)，了解如何：
- 添加新主题
- 添加新图表类型
- 改进布局规则和修复视觉 Bug
- 完善常见问题库

## 📄 许可证

MIT
