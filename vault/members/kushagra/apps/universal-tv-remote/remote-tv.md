---
type: app
category: universal-tv-remote
app: Universal Remote Control
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:9]
---

# Universal Remote Control — screenshot teardown

**Scope.** Screens-only review of team capture `remotetv.pdf` (PDF created 2026-10-03; 9 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | TV discovery list refresh state. | Wait for discovered device. | [OBSERVED] TV discovery list refresh state. | `“Connect your TV.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to wait for discovered device. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 1 |
| 2 | Universal remote layout with TV-not-connected status. | Tap remote controls; success unknown. | [OBSERVED] Universal remote layout with TV-not-connected status. | `“TV is not connected.”` (representative copy visible in this span) | pairing progress | [INFERRED] Asks user to tap remote controls; success unknown. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 2 |
| 3 | Screen-mirroring and cast-media promotions. | Open mirroring or cast. | [OBSERVED] Screen-mirroring and cast-media promotions. | `“Cast media.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to open mirroring or cast. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 3 |
| 4–5 | Repeated TV discovery/refresh screens. | Wait for devices or troubleshoot. | [OBSERVED] Repeated TV discovery/refresh screens. | `“Refreshing…”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to wait for devices or troubleshoot. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 4–5 |
| 6–8 | Full-TV-control premium offer repeated; feature claims. | Trial toggle, annual plan and continue. | [OBSERVED] Full-TV-control premium offer repeated; feature claims. | `“Unlock Full TV Control.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to trial toggle, annual plan and continue. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 6–8 |
| 9 | My Apps listing with common streaming services. | Choose service; pairing/launching unknown. | [OBSERVED] My Apps listing with common streaming services. | `“My Apps.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to choose service; pairing/launching unknown. Still images cannot establish timing, hard gating or action success. | `remotetv.pdf`, pp. 9 |

## Eight screen lenses

1. **First win.** Capture begins on a refreshing connect list p. 1, then shows a remote marked TV not connected p. 2. [OBSERVED] First successful control unknown.
2. **Ask ledger.** Device discovery p. 1, remote/app list p. 2, casting promo p. 3, repeated refresh p. 4–5, premium offer p. 6/8, apps list p. 7/9.
3. **Abstractions.** Universal remote controls, screen mirroring, cast media and app shortcuts. [OBSERVED] [INFERRED] Pairing/connect is essential; mirroring/cast are separate jobs.
4. **Feel-good moments.** App list p. 7 names familiar services; remote mockup p. 2 presents a broad set of controls. [OBSERVED] No earned success state.
5. **Feel-bad moments.** Discovery appears in a persistent refreshing state and TV-not-connected status (p. 1–2, 4–5). [OBSERVED] Whether this is temporary or a failure is unknown.
6. **Paywall.** Paywall p. 6/8 checked at full size: free trial toggle visibly on; 3-day trial then ₹699/week; 12 months ₹2,499/year (₹48.06/week); continue CTA. [OBSERVED] India storefront, captured 2026-10-03. Close delay/hard paywall unknown.
7. **Repeat cost.** No paired session, so repeat action cost is [UNKNOWN]. App list and remote tabs are visible p. 2/7.
8. **Feature map.** [INFERRED] Table stakes: reliable discovery and connected state. Differentiator: per-app shortcut list. Bloat: mirroring/casting upsell before pairing is verified.

## Keep / Kill / Different

- **Keep.** [OBSERVED] Keep the visible per-service app list and full remote layout (pp. 2, 7).
- **Kill.** Remove the premium offer while discovery remains in a refresh/not-connected state (pp. 1, 4–6). [INFERRED]
- **Different.** Make pairing status actionable with retry/manual entry and verify command success before trial. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 9 pages of `remotetv.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
