# Phase 6 — Art Direction

> Only now do we generate visuals. The register, in one sentence:
>
> **Shot by Apple. Built by Foster + Partners. Lived in by Hyderabad.**
>
> Every image must satisfy: globally recognizable quality · locally recognizable Hyderabad identity · premium editorial photography · believable architecture · cinematic composition. It should look at home in an Apple keynote, an Architectural Digest feature, or a Foster + Partners concept presentation.

---

## 6.1 Palette — "Granite & Pearl"

Dark-first (a city at blue hour). Warm dark, never pure black; warm white, never clinical.

| Token | Hex | Role | Share of pixels |
|---|---|---|---|
| **Golconda Noir** | `#0B0B0E` | Ground; the void of the first heartbeat | ~55% |
| **Granite 800/700** | `#16161A` / `#1E1D22` | Surfaces, cards, masonry | ~20% |
| **Pearl** | `#F4EFE6` | Primary text & light; warm like pearl, never `#FFF` | ~15% |
| **Mortar** | `#E9E1D2` | Light theme ground (Charminar lime) | light theme |
| **Koh-i-Noor Brass** | `#C2A25C` | Hairlines, focus rings, ceremony accents | ≤3% |
| **Laad Lacquer** | `#8E2B3F` | Community warmth, alerts-of-joy, festival weeks | ≤2% |
| **Deccan Lapis** | `#33518C` | Links, informational states (from Deccani miniatures) | ≤1% |
| **Pearl Iridescence** | gradient `#F4EFE6 → #D8C9E8 → #C9D8E4` | **AI-at-work only** (see 6.4) | ≤2%, always animated |
| **Jali Shadow** | `#000000 @ 18%` | Depth via lattice shadow, not drop shadows | — |

Rules: no pure black (`#000`), no pure white (`#FFF`); brass never fills large areas; saturation above 60% is allowed **only** in the Bazaar and festival themes; the "AI purple gradient" is banned outright — our AI tell is *pearl iridescence*, which reads as material, not neon.

## 6.2 Typography

| Role | Face class | Usage rules |
|---|---|---|
| Display / editorial | High-contrast serif (Canela-class; open: **Fraunces**, **Instrument Serif**) | Extreme scale contrast (72–200px vs 16px); negative tracking at display sizes (Vercel law) |
| UI / wayfinding | Precise grotesk (Geist/Inter class) | Weights 400/500/600 only; hierarchy by size + tracking + air |
| Agent output / data | Mono (Geist Mono / JetBrains Mono class) | Tabular numerals everywhere; the voice of machines |
| Ceremonial Telugu | **Noto Serif Telugu / Ramabhadra** | Chatta Bazaar rule: ceremony only (certificates, dedications) |
| Ceremonial Urdu | **Nastaliq (Noto Nastaliq Urdu)** | Same rule; the diagonal cascade is reserved for invitations and the founding charter |

The wordmark: set in the display serif, with the arch itself replacing the counter of the "A" in *Hyderabad* at large sizes. No glyph-level India stereotypes.

## 6.3 Geometry — one idea at every scale

**The Qutb Shahi arch** (a pointed, slightly ogee arch) is the platform's single geometric idea:

- **Cursor → icon:** arch as focus ring and active-tab indicator
- **Card → imagery:** every photograph in the product is masked by an arch (imagery lives *inside* arches, like niches in a wall)
- **Section → view:** view transitions are **arch-irises** (the new scene opens through an arch, 500–700ms, once per navigation)
- **District → city:** the four gates; the Gateway itself

Supporting motifs (each with a job): **jali lattice** (skeleton loaders, privacy veils — you can see through, but it filters), **kangura crenellation** (timeline ticks, progress edges), **the 10° tilt** (data-viz baselines rotate 10° — an heirloom only designers will find).

Radii: small and architectural (4–12px) everywhere except arch-masks. No pills on primary buttons.

## 6.4 Material system — honesty as a feature

| Material | Meaning | Where |
|---|---|---|
| Matte Deccan granite | Human-made, permanent | Grounds, walls, plinths, chrome surfaces |
| Lime plaster (warm white) | Human care | Light surfaces, light theme, interiors |
| **Bidri** (blackened metal, silver inlay) | The UI chrome itself — Hyderabad's own craft | Borders (silver hairlines), controls, app frame |
| **Pearl iridescence** | **AI at work — the only shimmering material** | Agent runs, generated artifacts, the Oracle, model thinking |
| Glass | Imported / external / third-party | Integration cards, external links — deliberately cooler |
| Brass | Ceremony | Focus rings, seals, lamp glows, statue details |

**The Iridescence Law:** if it shimmers, a machine is making it *right now*. Finished AI artifacts settle into matte surfaces with a small pearl hallmark. Users learn to read provenance at a glance — and the shimmer is the platform's most screenshot-able signature.

## 6.5 Light & time — the city keeps IST

- **Dawn (05:45–08:00):** pearl-and-rose over the lake; dum-build unveilings; birdsong-light ambience.
- **Day (08:00–17:00):** crisp, editorial, low drama; working light; sharp jali shadows.
- **Blue hour (17:45–19:15):** the canonical brand state; the reveal happens here by default; brass and pearl dominate.
- **Night (19:15–05:45):** windows glow (presence), the Cyber Mile turns electric, the Bazaar peaks; Ramzan night market opens.
- **Monsoon days:** mist layers, slower ambient motion, reading-room traffic up. **Festivals:** full-city lighting overrides.
- First visit always lands at blue hour. (The reveal deserves the best light in the world.)

## 6.6 Motion

| Layer | Law |
|---|---|
| UI motion | ≤300ms, transform/opacity only, one easing family (`cubic-bezier(0.22, 1, 0.36, 1)`) |
| Scene motion | 600–1200ms documentary camera moves: dolly (drill-in), crane (reveal), pan (stroll) — only at scene changes |
| The Golconda ripple | Notifications propagate as light along real architectural paths; respects Do Not Disturb (the ripple stops at your gate) |
| Ambient life | 8s breathing parallax, drifting mist, window lights toggling — the city moves even when idle |
| Presence | Other citizens are gentle light and drifting lanterns (Journey's wordless multiplayer; never avatar legs) |
| Prohibition | Nothing bounces, wiggles, or begs for attention. Tehzeeb. |

Sound (sparse, dignified): the **clap** (Golconda) for city-wide announcements you follow; a soft *pour* for chai hour; dusk temple bell at exactly 18:00 IST on festival days only; everything else silent by default.

## 6.7 Photography & rendering rules

1. **Believable architecture** — gravity-aware, material-correct; Foster-grade geometry with Deccan materials. No impossible floating stone.
2. **Editorial register** — medium-format look, blue-hour or dawn light, volumetric monsoon mist for depth, long-exposure light trails only where agents/people move.
3. **Scale through tiny silhouettes** — never faces in close-up (privacy + timelessness); people are points of light at distance.
4. **One idea per frame** — every image is a keynote slide; if two things compete, two images.
5. **Hyderabad enters through geometry and material** — arch proportions, heart-shaped lake, granite ramparts, jali shadows — never through literal postcard landmarks pasted into scenes.
6. **No text inside imagery** (except ceremonial artifacts); type is a product layer, not baked into photos.

## 6.8 The launch image set (Phase 6 outputs)

All images in [`visuals/`](visuals/). Shared style DNA across the set: matte Deccan granite, pearl-white lime plaster, warm brass light, pearl iridescence reserved for AI elements, volumetric mist, blue-hour/dawn light, medium-format cinematic architectural photography, Foster + Partners concept-presentation quality.

| # | File | Brief |
|---|---|---|
| 01 | `01-first-frame.jpg` | **Second 0–5.** The dome in the void — abstract, keynote-grade, nowhere-specific |
| 02 | `02-the-reveal.jpg` | **Second 5–15.** The pull-back: dome on a heart-shaped lake, four arches beyond, ramparts, supertalls at the edge |
| 03 | `03-gateway.jpg` | Charminar Plaza — the community heart, four arches, jali light, citizens as drifting light |
| 04 | `04-signal-citadel.jpg` | Golconda — a notification as light rippling along granite ramparts; the diamond vault glinting below |
| 05 | `05-the-heart.jpg` | Hussain Sagar at dawn — the Oracle monolith, heart-shaped shoreline, necklace of lights |
| 06 | `06-the-bazaar.jpg` | Laad Bazaar as marketplace — arch arcade, hanging bangle-rings of light, festival warmth |
| 07 | `07-materials.jpg` | The material board — granite, lime plaster, Bidri, brass, pearl, lacquer, jali |
| 08 | `08-the-product.jpg` | The product itself — UI applying the entire system (arch cards, Bidri chrome, iridescent agent run) |

Each image doubles as the art-direction proof for its district: if the set reads as one city, the system works.
