# 🇯🇵 Japan UNSC — MUN Research Hub

> **Model United Nations | Security Council | Strait of Hormuz Crisis**  
> A complete, interactive preparation toolkit for delegates representing **Japan** at a UNSC simulation.

---

## 📋 Overview

This repository contains a fully self-contained, browser-based research and strategy hub built for a Model United Nations conference. The simulation places delegates in the **United Nations Security Council**, debating the **Strait of Hormuz crisis** — a high-stakes geopolitical scenario involving freedom of navigation, energy security, and great-power competition.

Japan is a non-permanent member in this simulation and relies on the Strait of Hormuz for **~90% of its oil imports**, making this agenda item existential for its delegation.

---

## 🗂️ Repository Structure

```
MUN/
├── index.html                    # 🌐 Japan Strategy & MUN Prep — Unified Hub (main file)
├── unsc_complete_guide.html      # 📘 UNSC Procedural Complete Guide
├── MUN Handbook.pdf              # 📄 Official MUN conference handbook
├── MUN study guide.pdf           # 📄 General MUN study guide
├── COUNTRY MATRIX-1.xlsx         # 📊 Country alignment matrix spreadsheet
├── Helping material/             # 📁 Additional prep scripts and merged HTML files
│   ├── japan_country_strategy_hormuz.html
│   ├── japan_unsc_hormuz_mun_prep.html
│   ├── japan_unsc_merged_hub.html
│   ├── japan_unsc_strategy.html
│   ├── build_merged.py
│   ├── build_merged_v2.py
│   └── merge_html.py
└── Prep material/                # 📁 Position papers
    └── position_paper_Turkiye.docx
```

---

## 🌐 Main Files

### `index.html` — Japan UNSC Master Hub

The primary interactive dashboard. Open this file in any modern browser — **no server or installation required**.

**Two top-level sections:**

#### 🌍 Strategy & Room Control
Real-time delegation strategy for Japan's position at the UNSC:

| Tab | Contents |
|-----|----------|
| 🗺 **Room Map** | Visual grid of all 24 delegations, colour-coded by alignment (Ally / Swing / Threat / Neutral) |
| 🟢 **Allies** | Detailed profiles for S. Korea, India, Germany, France, UK, Oman, Qatar, UAE, Jordan, Kuwait |
| 🟡 **Swing States** | Persuasion playbooks for Saudi Arabia, China, Turkey, Pakistan, Egypt, Indonesia |
| 🔴 **Threats** | Counter-strategy for Iran, Russia, Syria, Iraq |
| ⚔️ **Rebuttals** | Pre-built rebuttals to likely attacks on Japan's position |
| 🗳 **Vote Math** | Real-time vote counting: 9 votes needed, P5 veto scenarios, best/worst case |
| 🏆 **Win Plan** | 4-phase session strategy (Opening → Bloc Building → Resolution Drafting → Voting) |

#### 📚 MUN Prep & Speeches
Prepared content for the debate floor:

| Tab | Contents |
|-----|----------|
| 🎙 **Speeches** | Opening statement + moderated caucus speeches on key subtopics |
| 📋 **Clauses** | Draft preambulatory and operative clauses for Japan's working paper |
| 🤝 **Negotiation** | Bloc-by-bloc deal frameworks and red lines |
| 🧠 **Cheat Sheet** | Quick-reference card for the entire session |

---

### `unsc_complete_guide.html` — UNSC Process Guide

A standalone, comprehensive reference on **how the Security Council actually works** — both in real life and in simulation. Fully interactive with tabbed navigation.

**Sections covered:**

| Tab | Topic |
|-----|-------|
| 🏛 **Overview** | What the UNSC is, its mandate, and how it differs from the General Assembly |
| 👥 **Composition** | P5 permanent members (veto holders), E10 elected members, the rotating Presidency |
| 🔄 **Full Flow** | 11-step session flow from Opening Roll Call → Resolution Adopted/Vetoed |
| 📋 **All Motions** | Every procedural motion with exact wording (Moderated Caucus, Unmoderated Caucus, Close Debate, etc.) |
| ✋ **Points** | Point of Order, Point of Inquiry, Point of Information, Right of Reply, Point of Personal Privilege |
| 🎙 **Debate Types** | GSL, Moderated Caucus, Unmoderated Caucus — strategy tips for each |
| 📄 **Documents** | Position Paper → Working Paper → Draft Resolution → Resolution → Amendment pipeline |
| 🗳 **Voting** | The 9-vote threshold, P5 veto mechanics, Roll Call vs. Placard vote, Present vs. Present and Voting |
| 🚫 **The Veto** | Article 27(3) deep-dive, substantive vs. procedural matters, double veto, historical usage |
| ⚖️ **UNSC vs GA** | Comparison table: binding vs. recommendatory, membership, quorum, veto, voting thresholds |
| ⚡ **Cheat Sheet** | One-page quick reference for every key procedure |

---

## 🎯 Japan's Strategic Position

**Committee:** United Nations Security Council (UNSC)  
**Agenda Item:** Security and Freedom of Navigation in the Strait of Hormuz  
**Japan's Role:** Non-permanent member — energy-dependent Pacific nation

### Core Pillars
1. **Rule of Law** — Uphold UNCLOS and international maritime law
2. **De-escalation** — Oppose military solutions; push for multilateral dialogue
3. **Energy Security** — Protect the free flow of oil through the Strait (~90% of Japan's imports transit here)
4. **No Veto Risk** — Draft language that avoids triggering Russia/China vetoes

### Alliance Targets
- **Lock in:** South Korea, India, Germany, France, UK
- **Flip:** China (JCPOA clause trade-off), Saudi Arabia (tanker seizure condemnation), Turkey (neutral mediator role)
- **Neutralize:** Russia (Chapter VI framing, no enforcement triggers), Iran (economic off-ramp language)

### Voting Math
- Need: **9 affirmative votes** + **0 P5 negative votes**
- Confirmed allies: ~7 votes locked
- Swing targets: need 2-3 from Saudi, China, Turkey, Pakistan, Egypt, Indonesia

---

## 🛠️ How to Use

### Opening the Hub
```bash
# Simply open in a browser — no server needed
xdg-open index.html           # Linux
open index.html               # macOS
start index.html              # Windows
```

Or drag and drop `index.html` into any modern browser (Chrome, Firefox, Edge, Safari).

### Recommended Prep Flow
1. **Read** `unsc_complete_guide.html` → understand UNSC rules of procedure
2. **Review** `MUN Handbook.pdf` → familiarise yourself with conference-specific rules
3. **Study** `COUNTRY MATRIX-1.xlsx` → understand each delegation's alignment
4. **Use** `index.html` → strategy, speeches, negotiation playbooks during session

---

## 📐 Technical Details

Both HTML files are:
- **100% self-contained** — no external dependencies beyond Google Fonts (loaded via CDN)
- **Offline-compatible** — work without internet (fonts fall back gracefully)
- **Mobile-responsive** — adapted layouts for phones and tablets
- **Zero-dependency** — pure HTML, CSS, and vanilla JavaScript

### Design System
- **Fonts:** Syne (headings), IBM Plex Mono (code/labels), Inter (body)
- **Color Palette:** Dark mode (`#080c14` base) with semantic accent colors
  - 🟢 Ally: `#00c87a`
  - 🟡 Swing: `#f59e0b`
  - 🔴 Threat: `#f04f4f`
  - 🔵 Accent: `#3b82f6`
  - 🔴 Japan: `#bc002d`

---

## 📚 Source Material & References

| Resource | Description |
|----------|-------------|
| UN Charter (Chapter V–VII) | Legal basis for UNSC authority and veto power |
| UNCLOS (Articles 17–19, 38) | Freedom of navigation and innocent passage law |
| JCPOA (2015 Iran Nuclear Deal) | Background on Iran sanctions and diplomatic context |
| UN Security Council Rules of Procedure | Official procedural reference |
| Japan Ministry of Foreign Affairs | Japan's stated policy positions on Hormuz and maritime security |
| IEA Energy Reports | Japan's oil import dependency statistics |

---

## 👤 Author

**Nauman Ahmad**  
Research prepared for a Model United Nations UNSC simulation, 2026.  
Repository: [NaumanAhmad2005/Research-Page-from-japan-pov](https://github.com/NaumanAhmad2005/Research-Page-from-japan-pov)

---

*"The delegation of Japan firmly believes that the free and safe passage of vessels through the Strait of Hormuz is not merely an economic interest — it is the foundation upon which the international rules-based order stands."*
