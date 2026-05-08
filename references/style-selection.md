# Style Selection Matrix

## Quick Decision

| User Context | Recommended Style |
|-------------|-------------------|
| No preference stated | modern-light |
| Technical audience / engineering | dark-tech |
| Formal document / print / PDF | monochrome |
| Blog / explainer / product docs | warm-minimal |
| Engineering spec / design doc | blueprint |
| Creative / marketing / demo | neon-cyber |
| Fun / hackathon / comic / playful | comic-pop |
| Geek / CLI tool / hacker aesthetic | retro-terminal |
| Teaching / casual / handmade feel | papercraft |
| Sci-fi / tactical / military HUD | hud-hologram |
| Cosmic / elegant / space theme | starfield |
| User says "dark" or mentions dark mode | dark-tech |
| User says "简洁" / "clean" / "minimal" | modern-light |
| User says "正式" / "formal" / "print" | monochrome |
| User says "cool" / "酷" / "炫" | neon-cyber |
| User says "漫画" / "comic" / "fun" / "pop" | comic-pop |
| User says "终端" / "terminal" / "hacker" | retro-terminal |
| User says "手工" / "craft" / "手绘" | papercraft |
| User says "HUD" / "全息" / "hologram" / "tactical" | hud-hologram |
| User says "星空" / "space" / "cosmic" / "star" | starfield |

## Diagram Type Affinity

| Diagram Type | Best Styles | Avoid |
|-------------|-------------|-------|
| architecture | dark-tech, modern-light, blueprint, hud-hologram, starfield | — |
| flowchart | modern-light, warm-minimal, papercraft | blueprint (too rigid for decisions) |
| data-flow | dark-tech, warm-minimal, retro-terminal | monochrome (loses flow emphasis) |
| sequence | modern-light, blueprint | neon-cyber (distracting for ordered messages) |
| dependency | modern-light, monochrome, hud-hologram | neon-cyber, warm-minimal |
| mind-map | warm-minimal, neon-cyber, comic-pop, papercraft, modern-light | monochrome (needs color for branches) |
| timeline | blueprint, modern-light, dark-tech, starfield | — |
| network-topology | dark-tech, blueprint, hud-hologram, retro-terminal | warm-minimal (too soft for infra) |
| comparison | modern-light, monochrome | neon-cyber (grid needs clarity) |
| class-diagram | modern-light, blueprint, monochrome | neon-cyber (UML needs precision) |
| er-diagram | blueprint, modern-light | neon-cyber |
| use-case | modern-light, warm-minimal | dark-tech (actors hard to see) |
| state-machine | dark-tech, modern-light, blueprint | — |
| component | blueprint, dark-tech | warm-minimal |

## Override Rules

1. If user explicitly names a style → use it regardless of matrix
2. If user says "no animation" → use monochrome
3. If target is print/PDF → use monochrome
4. If user's description contains Chinese and no style hint → default modern-light
5. If the diagram has >12 nodes → prefer styles with less animation (modern-light, blueprint, monochrome)
