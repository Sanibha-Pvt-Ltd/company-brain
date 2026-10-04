---
type: app
category: sleep-tracker
app: Remly
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:13]
---

# Remly — screenshot teardown

**Scope.** Screens-only review of team capture `sleeptracker_remly.pdf` (PDF metadata creation date 2026-10-03; screenshot capture date unknown; 13 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | App Tracking Transparency prompt appears on launch. | Allow or ask app not to track. | [OBSERVED] App Tracking Transparency prompt appears on launch. | `System prompt: “Allow ‘Remly’ to track your activity across other companies’ apps and websites?”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to allow or ask app not to track. Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 1 |
| 2–4 | Home screen with a seven-night tracker countdown; sleep-recorder explanation and tonight plan. | Continue to recorder or choose “Not now”; home suggests paper journal and bedtime actions. | [OBSERVED] Home screen with a seven-night tracker countdown; sleep-recorder explanation and tonight plan. | `“Welcome to unique patented Sleep Recorder!”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue to recorder or choose “Not now”; home suggests paper journal and bedtime actions. Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 2–4 |
| 5–8 | Sleep-help content and sound library. | Browse sleep tips, sounds and dream tools. | [OBSERVED] Sleep-help content and sound library. | `“Sleeping Tip of the Day.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to browse sleep tips, sounds and dream tools. Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 5–8 |
| 9 | Apple Health permission how-to. | Go to Apple Health or select “Not now.” | [OBSERVED] Apple Health permission how-to. | `“Grant access to Health App!”` (representative copy visible in this span) | permission cost | [INFERRED] Asks user to go to Apple Health or select “Not now.” Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 9 |
| 10–12 | Profile with no collected data, sleep goal/reminder controls, and heart/breathing settings. | Log in/sign up or enable trackers/reminders. | [OBSERVED] Profile with no collected data, sleep goal/reminder controls, and heart/breathing settings. | `“No data has been collected yet.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to log in/sign up or enable trackers/reminders. Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 10–12 |
| 13 | Remly Pro personalized plan and trial offer. | Continue into trial; trial toggle is selected in the screenshot. | [OBSERVED] Remly Pro personalized plan and trial offer. | `“Better Sleep in 7 Days.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to continue into trial; trial toggle is selected in the screenshot. Still images cannot establish timing, hard gating or action success. | `sleeptracker_remly.pdf`, pp. 13 |

## Eight screen lenses

1. **First win.** Home p. 2 offers a “Track” flow and seven-night progress frame, but no measured sleep appears. [OBSERVED] First verified result/taps [UNKNOWN]; premium appears p. 13.
2. **Ask ledger.** ATT prompt p. 1; choose recorder or “Not now” p. 3; Health walkthrough p. 9; optional account p. 10; tracker/reminder toggles p. 11–12; trial p. 13.
3. **Abstractions.** “Sleep Toolkit,” bedtime plan, “Dreamboat,” and “Focus areas” are shown on p. 2–7, 13. [OBSERVED] [INFERRED] These are secondary to setting a bedtime and recording one night.
4. **Feel-good moments.** Nightly plan checklist p. 4 and a sleep tip p. 5 imply small actions. [OBSERVED] A completed action or sleep result is not shown.
5. **Feel-bad moments.** ATT prompt opens before the app’s purpose is explained (p. 1). [OBSERVED] Seven-night countdown framing appears before any result (p. 2); no guilt language can be confirmed.
6. **Paywall.** P. 13: 7 days free, then ₹999 on Oct. 10, 2026; auto-renewal/cancel-anytime visible. Trial is visibly enabled on this screen. [OBSERVED] INR is displayed; US pricing is unknown. PDF metadata creation date is 2026-10-03; screenshot capture date is unknown. Whether enabled by default in flow is [UNKNOWN].
7. **Repeat cost.** Home offers a central track action (p. 2–4); 7 nights are framed before score. [OBSERVED] Exact action count and post-night report are not captured.
8. **Feature map.** [INFERRED] Table stakes: one-tap start, bedtime/reminder and morning summary. Differentiator: “Tonight’s Plan” checklist. Bloat risk: dream analysis and focus-area taxonomy before proven recording value.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the Tonight’s Plan checklist and single central Track action (pp. 2–4).
- **Kill.** Remove the ATT prompt before the product introduction and the seven-night countdown before any measured report (pp. 1–2). [INFERRED]
- **Different.** Explain recording, ask permissions only when required, and show the first night result before the Remly Pro trial. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 13 pages of `sleeptracker_remly.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and are displayed in INR; US pricing is unknown.
