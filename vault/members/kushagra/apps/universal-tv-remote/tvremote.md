---
type: app
category: universal-tv-remote
app: TV Remote (screenshot capture name unknown)
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:9]
---

# TV Remote (screenshot capture name unknown) — screenshot teardown

**Scope.** Screens-only review of team capture `Tvremote.pdf` (PDF created 2026-10-03; 9 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | TV discovery/search screen. | Wait/search for TV; close and help icons visible. | No real-TV action outcome can be concluded from stills. | `“Searching…”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 1 |
| 2 | Full-access subscription offer. | Start trial, choose yearly/lifetime, or close/restore. | No real-TV action outcome can be concluded from stills. | `“Unlock Full Access.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 2 |
| 3 | Remote control with navigation, playback, volume and branded app buttons. | Tap remote controls; connection state not provable from still. | No real-TV action outcome can be concluded from stills. | `“TV Remote.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 3 |
| 4–5 | Repeated subscription offer screens. | Trial/yearly/lifetime plan choices. | No real-TV action outcome can be concluded from stills. | `“Unlock Full Access.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 4–5 |
| 6 | Apps screen stating TV not connected. | Connect TV. | No real-TV action outcome can be concluded from stills. | `“TV Not Connected.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 6 |
| 7 | Cast feature tiles: photo, video, IPTV, browser, mirroring and chatbot. | Select a cast category. | No real-TV action outcome can be concluded from stills. | `“Cast All Media to TV.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 7 |
| 8–9 | Settings, feature links, ad-supported bottom navigation. | Upgrade/restore/settings actions. | No real-TV action outcome can be concluded from stills. | `“Upgrade to Premium.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `Tvremote.pdf`, pp. 8–9 |

## Eight screen lenses

1. **First win.** An initial scan p. 1 is followed immediately by a paywall p. 2; a remote appears p. 3, while Apps says “TV Not Connected” p. 6. [OBSERVED] No successful command/first-win taps are proven.
2. **Ask ledger.** Wait/search p. 1; trial/plan/payment prompt p. 2; remote controls p. 3; repeated offers p. 4–5; connect prompt p. 6; cast choices p. 7; upgrade/settings p. 8–9.
3. **Abstractions.** Pairing, remote controls, channels, casting, IPTV, browser and chatbot all appear. [OBSERVED] [INFERRED] Pairing + basic buttons are necessary; the rest is a separate media toolbox.
4. **Feel-good moments.** Familiar purple directional pad and branded app shortcuts p. 3 reduce learning. [OBSERVED] This does not prove an action worked.
5. **Feel-bad moments.** Paywall screens repeat p. 2, 4, 5; empty disconnected state p. 6. [OBSERVED] Close X is visible p. 2; hard gating or delay is [UNKNOWN].
6. **Paywall.** P. 2: 3-day trial then ₹699/week, yearly ₹1,799, lifetime ₹4,999. [OBSERVED] India storefront, capture 2026-10-03; no payment outcome.
7. **Repeat cost.** Core control surface p. 3; cast p. 7; repeated ad banner visible on app screens. [OBSERVED] Repeat taps/TV response [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: connect status + directional/power/volume/playback. Differentiator: channel shortcuts. Bloat: chatbot, browser/IPTV and repeated upsells.

## Keep / Kill / Different

- **Keep.** Familiar purple directional pad and branded app shortcuts p. 3 reduce learning. [OBSERVED] This does not prove an action worked.
- **Kill.** Paywall screens repeat p. 2, 4, 5; empty disconnected state p. 6. [OBSERVED] Close X is visible p. 2; hard gating or delay is [UNKNOWN]. [INFERRED] Remove steps or claims here that precede a verified result/command; test the precise step against a fresh install before shipping a similar flow.
- **Different.** An initial scan p. 1 is followed immediately by a paywall p. 2; a remote appears p. 3, while Apps says “TV Not Connected” p. 6. [OBSERVED] No successful command/first-win taps are proven. [INFERRED] Make the first successful sleep report/TV command visible, identify whether it is measured or a preview, and put optional permissions/account/payment after that first outcome.

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 9 pages of `Tvremote.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
