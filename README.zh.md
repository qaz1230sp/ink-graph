<p align="center">
  <h1 align="center">🖋️ Ink-Graph</h1>
  <p align="center">
    <em>AI Agent Skill · 自然语言 → 动画 SVG 技术图</em>
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT 许可证"></a>
  <a href="https://www.npmjs.com/package/@qaz1230sp/ink-graph"><img src="https://img.shields.io/npm/v/@qaz1230sp/ink-graph.svg" alt="npm 版本"></a>
  <a href="https://www.npmjs.com/package/@qaz1230sp/ink-graph"><img src="https://img.shields.io/npm/dm/@qaz1230sp/ink-graph.svg" alt="npm 下载量"></a>
  <a href="https://github.com/qaz1230sp/ink-graph/stargazers"><img src="https://img.shields.io/github/stars/qaz1230sp/ink-graph.svg" alt="GitHub Star 数"></a>
  <a href="https://github.com/qaz1230sp/ink-graph/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="欢迎提交 PR"></a>
  <a href="https://github.com/qaz1230sp/ink-graph/issues"><img src="https://img.shields.io/github/issues/qaz1230sp/ink-graph.svg" alt="GitHub Issues"></a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@qaz1230sp/ink-graph"><b>📦 npm 包</b></a> &nbsp;|&nbsp;
  <a href="SKILL.md"><b>📄 SKILL.md</b></a> &nbsp;|&nbsp;
  <a href="CONTRIBUTING.md">🤝 参与贡献</a> &nbsp;|&nbsp;
  <a href="README.md">🇬🇧 English</a>
</p>

<details>
<summary>📋 目录</summary>

- [为什么选择 Ink-Graph？](#为什么选择-ink-graph)
- [主题画廊](#主题画廊)
- [快速开始](#快速开始)
- [图表类型展示](#图表类型展示)

- [特性列表](#特性列表)
- [主题参考表](#主题参考表)
- [支持的图表类型](#支持的图表类型)
- [项目结构](#项目结构)
- [环境要求](#环境要求)
- [参与贡献](#参与贡献)
- [贡献者](#贡献者)
- [许可证](#许可证)

</details>

## 为什么选择 Ink-Graph？

还在为 Mermaid、D2、PlantUML 这类 DSL 记语法吗？刚把架构图画完，代码一改、服务一拆、链路一变，图又立刻过时？很多技术图不是不会画，而是**太费脑、太费时间、太难维护**。

Ink-Graph 就是为这个痛点做的：你只要用自然语言描述系统、流程或关系，AI 就能直接生成一张完整的动画 SVG 技术图。没有 DSL 学习成本，没有额外渲染引擎，也不用手调一堆坐标。它天然适合 AI Agent 工作流，兼容 GitHub Copilot CLI、Claude Code、Cursor 等工具，还内置 **11 种专业主题**、**14 种图表类型**，输出是可以直接预览、分享、嵌入文档的**纯 SVG 动画**。

一句话：**少写语法，多讲结构；少画框线，多表达思路。**

## 主题画廊

同一张架构图，换个主题就是完全不同的气质：

<table>
<tr>
<td align="center"><strong>Modern Light（现代明亮）</strong><br/><img src="samples/modern-light-architecture.svg" width="260" alt="Modern Light 主题的现代明亮架构图"/></td>
<td align="center"><strong>Dark Tech（暗黑科技）</strong><br/><img src="samples/dark-tech-architecture.svg" width="260" alt="Dark Tech 主题的暗色科技架构图"/></td>
<td align="center"><strong>Blueprint（工程蓝图）</strong><br/><img src="samples/ufo3-architecture.svg" width="260" alt="Blueprint 主题的工程蓝图风架构图"/></td>
</tr>
<tr>
<td align="center"><strong>Warm Minimal（暖色极简）</strong><br/><img src="samples/warm-minimal-architecture.svg" width="260" alt="Warm Minimal 主题的暖色极简架构图"/></td>
<td align="center"><strong>Monochrome（黑白单色）</strong><br/><img src="samples/monochrome-architecture.svg" width="260" alt="Monochrome 主题的黑白单色架构图"/></td>
<td align="center"><strong>Neon Cyber（霓虹赛博）</strong><br/><img src="samples/neon-cyber-architecture.svg" width="260" alt="Neon Cyber 主题的霓虹赛博架构图"/></td>
</tr>
<tr>
<td align="center"><strong>Comic Pop（漫画波普）</strong><br/><img src="samples/comic-pop-architecture.svg" width="260" alt="Comic Pop 主题的漫画波普架构图"/></td>
<td align="center"><strong>Retro Terminal（复古终端）</strong><br/><img src="samples/retro-terminal-architecture.svg" width="260" alt="Retro Terminal 主题的复古终端架构图"/></td>
<td align="center"><strong>Papercraft（纸艺拼贴）</strong><br/><img src="samples/papercraft-architecture.svg" width="260" alt="Papercraft 主题的纸艺拼贴架构图"/></td>
</tr>
<tr>
<td align="center"><strong>HUD Hologram（全息 HUD）</strong><br/><img src="samples/hud-hologram-architecture.svg" width="260" alt="HUD Hologram 主题的全息 HUD 架构图"/></td>
<td align="center"><strong>Starfield（星空星云）</strong><br/><img src="samples/starfield-architecture.svg" width="260" alt="Starfield 主题的星空星云架构图"/></td>
<td></td>
</tr>
</table>

## 快速开始

### 安装

安装 skill：
```bash
npx skills add qaz1230sp/ink-graph
```

或手动将此目录放入 AI 工具的 skills 目录：

```
~/.claude/skills/ink-graph/
```

也可通过 Claude Code 技能管理界面安装。

### 第一张图

直接用自然语言描述就行：

```text
> 画一个 SaaS 平台架构图：Web App、API Gateway、Auth Service、PostgreSQL 和 Redis，风格用 modern-light
```

```text
> Draw a dark-tech data flow diagram for: Client → API → Kafka → Stream Processor → Data Warehouse → BI Dashboard
```

```text
> 帮我做一个用户注册流程图：进入注册页 → 填写信息 → 邮箱验证 → 创建账号 → 欢迎邮件
```

```text
> Visualize a sequence diagram for order payment: User, Checkout UI, Payment API, Stripe, Inventory Service
```

AI 会读取 `SKILL.md`，选择合适主题，加载参考文件，生成完整 SVG 文件。

## 图表类型展示

除了架构图，Ink-Graph 也很适合这些场景：

<table>
<tr>
<td align="center"><strong>Flowchart</strong><br/><sub>Papercraft</sub><br/><img src="samples/papercraft-flowchart.svg" width="260" alt="Papercraft 主题的流程图示例"/></td>
<td align="center"><strong>Data Flow</strong><br/><sub>Dark Tech</sub><br/><img src="samples/dark-tech-data-flow.svg" width="260" alt="Dark Tech 主题的数据流图示例"/></td>
<td align="center"><strong>Sequence</strong><br/><sub>HUD Hologram</sub><br/><img src="samples/hud-hologram-sequence.svg" width="260" alt="HUD Hologram 主题的时序图示例"/></td>
</tr>
<tr>
<td align="center"><strong>Mind Map</strong><br/><sub>Comic Pop</sub><br/><img src="samples/comic-pop-mindmap.svg" width="260" alt="Comic Pop 主题的思维导图示例"/></td>
<td align="center"><strong>Dependency</strong><br/><sub>Monochrome</sub><br/><img src="samples/monochrome-dependency.svg" width="260" alt="Monochrome 主题的依赖关系图示例"/></td>
<td></td>
</tr>
</table>

## 特性列表

- **11 种专业主题**：从清爽商务风到科幻 HUD，从严肃工程感到漫画感展示，都有现成风格可选。
- **14 种图表类型**：覆盖架构图、流程图、数据流图、时序图、依赖图、思维导图、类图、ER 图、状态机、组件图、网络拓扑、时间线、对比图、用例图。
- **CSS / SMIL 动画效果**：内置流光连线、入场动画、悬停发光、CRT 闪烁等细节，不只是“能看”，而是“有表现力”。
- **代码仓库分析** *(v2 规划中)*：后续会支持直接从仓库结构和代码关系生成图表。
- **零 JavaScript 运行时**：输出是纯 SVG + CSS，浏览器打开就能看，适合嵌入文档、博客、演示页。
- **SVG + PNG 输出**：默认生成 SVG，也可以配合 `librsvg` 导出 PNG。

## 主题参考表

| 主题 | 风格 | 适用场景 |
|------|------|----------|
| **modern-light** | 清爽、均衡、信息层次清楚 | 产品文档、方案汇报、通用架构图 |
| **dark-tech** | 深色背景、荧光线条、科技感强 | 云平台、AI 系统、基础设施图 |
| **blueprint** | 工程制图感、理性、精确 | 技术方案、设计说明、蓝图展示 |
| **warm-minimal** | 柔和配色、友好、轻量 | 博客配图、教程文档、知识分享 |
| **monochrome** | 黑白灰、克制、可打印 | 合规文档、审计材料、PDF 输出 |
| **neon-cyber** | 高对比霓虹、未来感、吸睛 | Demo 展示、营销页面、发布会素材 |
| **comic-pop** | 漫画描边、活泼、有趣 | 黑客松、分享会、轻松风格演示 |
| **retro-terminal** | 终端绿屏、扫描线、复古极客 | CLI 文档、开发者工具、技术彩蛋页 |
| **papercraft** | 手工拼贴、纸感纹理、亲和 | 教学图解、说明文档、非正式汇报 |
| **hud-hologram** | 战术 HUD、悬浮界面、科幻感 | 时序交互、控制台大屏、概念演示 |
| **starfield** | 深空背景、星云点缀、氛围感强 | 高级展示、宇宙主题、品牌视觉图 |

## 支持的图表类型

| 图表类型 | 描述 | 默认方向 |
|----------|------|----------|
| **architecture** | 展示系统服务、分层结构、API 与边界 | 自上而下 |
| **flowchart** | 展示步骤、判断、分支和结果流转 | 自上而下 |
| **data-flow** | 展示数据从生产到消费的传递路径 | 从左到右 |
| **sequence** | 展示角色或服务之间按时间顺序的交互 | 自上而下 |
| **dependency** | 展示模块、包或服务之间的依赖关系 | 自上而下 |
| **mind-map** | 展示主题向外发散的知识结构 | 放射状 |
| **class-diagram** | 展示类、属性、方法以及继承关系 | 自上而下 |
| **er-diagram** | 展示数据库实体、字段与关联关系 | 从左到右 |
| **state-machine** | 展示状态节点及其转换条件 | 从左到右 |
| **component** | 展示软件组件及接口协作关系 | 自上而下 |
| **network-topology** | 展示网络设备、节点和连接拓扑 | 自由布局 |
| **timeline** | 展示按时间推进的事件序列 | 从左到右 |
| **comparison** | 展示功能、方案或产品的并排对比 | 网格 |
| **use-case** | 展示参与者与系统功能之间的关系 | 自由布局 |

## 项目结构

```text
ink-graph/
├── SKILL.md                        # 核心 Skill，AI 会先读它再生成图表
├── README.md                       # 英文说明文档
├── README.zh.md                    # 中文说明文档
├── CONTRIBUTING.md                 # 贡献指南
├── LICENSE                         # MIT 许可证
├── package.json                    # npm 包定义
├── references/
│   ├── style-*.md (11 个文件)      # 11 种主题的样式定义
│   ├── style-selection.md          # 主题选择建议
│   ├── layout-rules.md             # 布局规则与排版约束
│   ├── shapes.md                   # 图形节点定义
│   ├── animations.md               # 动画效果规则
│   └── pitfalls.md                 # 常见坑位与修复建议
├── samples/                        # 已生成好的 SVG 示例
├── scripts/
│   ├── validate_svg.py             # SVG 校验脚本
│   ├── export_png.py               # PNG 导出脚本（依赖 librsvg）
│   └── layout.py                   # 基于 Graphviz 的自动布局脚本
└── prompts/
    └── code-analysis.md            # 代码仓库分析提示词（v2）
```

## 环境要求

### 必需

- 支持自定义 Skill、Prompt 或 Rules 的 AI 助手
- 现代浏览器（用于预览 SVG 输出）

### 可选（高级功能）

- **Python 3.10+**：用于 `scripts/layout.py` 自动布局
- **Graphviz**：用于较复杂图表的自动排版
- **librsvg / `rsvg-convert`**：用于将 SVG 导出为 PNG

## 参与贡献

欢迎一起把 Ink-Graph 做得更酷。无论是补新主题、加新图表类型、优化布局规则，还是修复 SVG 细节问题，都很有价值。具体方式可以看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 贡献者

<p align="center">
  <a href="https://github.com/qaz1230sp/ink-graph/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=qaz1230sp/ink-graph" alt="Ink-Graph 贡献者列表" />
  </a>
</p>

## 许可证

本项目基于 [MIT](LICENSE) 许可证开源。
