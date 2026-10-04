---
type: category-lens
category: universal-tv-remote
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:7 PDFs / 66 pages]
---

# Universal TV remote — screens synthesis

**Scope.** Screens-only comparison of seven team screenshot PDFs, 66 pages total. Source PDFs have 2026-10-03 creation metadata; screenshot capture dates are unknown unless a screen itself shows a date. Any shown prices are INR and do not represent US pricing. Companion `TV_Remote_App_Analysis.pdf` was not used as evidence.

## Pattern table

| App | First visible control / value | Visible asks before it | Concepts | Paywall placement | Repeat cost evidence |
|---|---|---|---|---|---|
| TV Remote (`Tvremote.pdf`) | Search p. 1; remote UI p. 3; Apps says disconnected p. 6. No command success. | Search then offer p. 2; later repeated offers p. 4–5. | Pairing, remote, channels, casting, IPTV/browser/chatbot. | p. 2 before captured remote; repeated p. 4–5. p. 2 shows 3-day trial then ₹699/week, yearly ₹1,799, lifetime ₹4,999. | Buttons visible p. 3; connection and response unknown. [[members/kushagra/apps/universal-tv-remote/tvremote]] |
| Remote (`remote.pdf`) | Remote layout p. 1 but it says TV is not connected. | Premium appears in settings p. 3–4; connection search p. 5. | Touchpad, mobile power, forgotten devices, apps. | p. 4 and p. 6. p. 4 displays ₹1,999/year or 3-day trial then ₹499/week. | No connected TV. [[members/kushagra/apps/universal-tv-remote/remote]] |
| iMote (`remoteControl.pdf`) | Pairing instructions pp. 3–4; scan p. 5; remote modes pp. 6–9 still ask to connect. | Local network p. 2, two setup cards, repeated connect CTA; offer p. 7. | Local network, pairing confirmation, touchpad/keypad modes, cast. | p. 7 shows ₹0 3-Day Full Access selected, ₹76.90/week for yearly access, and a separate ₹999/week auto-renewable line. | Not connected in captured screens. [[members/kushagra/apps/universal-tv-remote/imote]] |
| Universal Remote Control (`remotetv.pdf`) | Search p. 1; disconnected remote p. 2. | Repeated refresh pp. 4–5; offer p. 6. | Remote, cast, mirror, app shortcuts. | p. 6; toggle appears on, 3-day trial then ₹699/week or 12 months at ₹2,499/year. | No successful command. [[members/kushagra/apps/universal-tv-remote/remote-tv]] |
| TV Remote by Kraftwerk (`tvremote by kraftwerk.pdf`) | Search p. 1 and p. 7; no device found. | Four feature cards pp. 2–5; paywall p. 6. | Touchpad, keyboard, compatibility, remote modes. | p. 6; 3-day trial with ₹3,499/year or ₹299/week. | No remote screen. [[members/kushagra/apps/universal-tv-remote/kraftwerk]] |
| TV Remote (`tvremote by.pdf`) | “Device found” p. 5 and remote p. 7; later “No TV Found” p. 9. Pairing is contradictory. | Brand choice p. 1; wait p. 2; feedback pp. 3–4; offers pp. 5–8. | Brand list, feedback, control, screen mirroring/cast. | p. 5: trial toggle off; ₹9,900/year (₹190.38/week display), ₹999/week. p. 8: “95% off,” ₹599/week. | Remote p. 7/10 but disconnected p. 9. [[members/kushagra/apps/universal-tv-remote/tvremote-by]] |
| TV Remote (`tvremoteapp.pdf`) | No picker/control; capture ends in purchase screens. [OBSERVED] | ATT p. 1; four promo cards pp. 2–5; purchase/plan p. 6–7. | Search, touchpad, keyboard, customization. | p. 6 shows three-day trial then ₹999/week; p. 7 lists that trial option, ₹1,999/month and ₹4,999/year. | Not captured. [[members/kushagra/apps/universal-tv-remote/tvremoteapp]] |

Page order and ask counts above describe the PDFs, not verified linear tap flows. A remote UI is not a first win unless a command reaches a real TV; none of these stills proves that outcome. [OBSERVED]

## Our first five minutes

1. **Explain the requirement:** phone and TV must be on the same Wi-Fi when required; explain local network access before opening the OS prompt. [INFERRED]
2. **Find the TV:** show detected devices, brand/model, and a manual retry/help route. Never leave a spinner without next steps. [INFERRED]
3. **Pair:** explain any on-TV confirmation/code in one concise step. Keep a visible back/retry action. [INFERRED]
4. **Prove control:** expose power, arrows/OK, volume and home. Confirm each action state or report that the TV did not respond. [INFERRED]
5. **After success:** offer keyboard/touchpad as optional quality-of-life features; explain a single plan and renewal terms after one command works. [INFERRED]

## Up to three differentiators

1. **Pairing that tells the truth.** One capture moves from “Device found” p. 5 to “No TV Found” p. 9; four other captures remain searching/disconnected. [OBSERVED] A persistent, accurate connection state with clear retry can stand out. [INFERRED]
2. **One command before the offer.** Several apps show premium screens before any proven successful control (TV Remote p. 2; TV Remote by Kraftwerk p. 6; TV Remote app pp. 5–7). [OBSERVED] Let users test power/navigation first. [INFERRED]
3. **Control first, cast second.** Cast/mirroring, IPTV, browser, chatbot and tool bundles appear alongside basic remote controls (Tvremote pp. 7–9; iMote pp. 10–14; `tvremote by.pdf` pp. 11–14). [OBSERVED] Keep the main remote uncluttered and make casting a separate destination. [INFERRED]

## Concepts we refuse to add

- A toolbox bundle (IPTV, browser, chatbot, scanner and unrelated tools) in the main remote flow; these appear in `Tvremote.pdf` pp. 7–9 and settings surfaces in other captures. [OBSERVED]
- Repeated sale prompts before a first working command; repeated trial/sale pages appear in `Tvremote.pdf` pp. 2, 4–5 and `tvremote by.pdf` pp. 5–8. [OBSERVED]
- Brand compatibility claims without a visible working pairing outcome. Several screenshots show only search or disconnected states. [OBSERVED]

## Open questions and what would change the call

- [UNKNOWN] Which TV brands/models, network conditions and pairing methods are supported; actual connection latency, command reliability, IR hardware limits, permission requirements and recovery success.
- [UNKNOWN] Whether the paid plans gate basic controls, live close/dismiss behavior, trial default state, renewal and checkout behavior, US storefront prices, and real repeat cost. Confirm with hands-on tests on multiple TV brands.
- [UNKNOWN] Demand for casting/mirroring vs remote-only control. Review mining and a working prototype would change feature priority; this pass establishes neither market demand nor business performance.

## Source map

All sources are in `kushagra screenshots/Universal TV Remote/screenshots/`; all pages in each PDF were visually inspected. The analysis PDF was excluded.

| Teardown | Screenshot source | Pages |
|---|---|---:|
| [[members/kushagra/apps/universal-tv-remote/tvremote]] | `Tvremote.pdf` | 9 |
| [[members/kushagra/apps/universal-tv-remote/remote]] | `remote.pdf` | 6 |
| [[members/kushagra/apps/universal-tv-remote/imote]] | `remoteControl.pdf` | 14 |
| [[members/kushagra/apps/universal-tv-remote/remote-tv]] | `remotetv.pdf` | 9 |
| [[members/kushagra/apps/universal-tv-remote/kraftwerk]] | `tvremote by kraftwerk.pdf` | 7 |
| [[members/kushagra/apps/universal-tv-remote/tvremote-by]] | `tvremote by.pdf` | 14 |
| [[members/kushagra/apps/universal-tv-remote/tvremoteapp]] | `tvremoteapp.pdf` | 7 |

**Count check:** 9 + 6 + 14 + 9 + 7 + 14 + 7 = 66 screenshot pages across 7 apps. [OBSERVED]
