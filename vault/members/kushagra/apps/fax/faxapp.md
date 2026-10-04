---
type: app
category: fax
app: Fax App (faxapp capture)
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:11]
---

# Fax App (faxapp capture) — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/faxapp.pdf` (11 pages). The name “Fax App” is the capture filename; exact App Store identity is [UNKNOWN]. Prices are shown in ₹; storefront is not independently verified.

## Screen map

| # | Stage | What user sees | Ask / copy / lever | Friction / evidence |
|---|---|---|---|---|
| 1 | Home | “Faxes,” All filter, empty “No faxes yet,” New, search | Start a fax | Empty but no account form or permission request visible. [OBSERVED] |
| 2 | Inbox | Incoming selected, “Receive faxes,” Get a Number | Purchase a number | Receiving is offered as a distinct task. [OBSERVED] |
| 3 | Loading | Blank dark screen with spinner | None visible | No user-facing information. [OBSERVED] |
| 4 | Receive paywall | “Receive Faxes / Turn your iPhone into a fax machine”; Personal number, Receive anywhere, No fax limits; Continue; “Only ₹199.00 per 1 week. Cancel anytime.” | Continue into weekly subscription | Restore and Terms/Privacy visible; no X visible in screenshot. [OBSERVED] |
| 5 | Native purchase | Apple sheet: Pro for one week; ₹199/week, auto-renew language | Confirm with Side Button | Renewal terms visible. Amount is displayed in ₹; storefront is not independently verified. [OBSERVED] |
| 6 | Home | Drafts filter; empty list | New | Loading has resolved to empty home. [OBSERVED] |
| 7 | New fax | Recipient filled; “No documents yet”; Add Attachment | Attach a document | Up arrow disabled before document. [OBSERVED] |
| 8 | New fax | Same with one scanned PDF, one page, ~40s display; Add Attachment disabled | Ready-state arrow appears at top | Concrete page preview, but ~40s is shown in interface and should not be treated as measured elapsed processing time. [OBSERVED] |
| 9 | “Fax is Ready” paywall | “Tap Continue to send it now”; highest priority, HIPAA compliant, no fax limits; Continue; “Only ₹199.00 per 1 week. Cancel anytime.” | Continue to send | Wall appears after document is prepared and before stated send action in the capture sequence; causality/accessibility unknown. [OBSERVED] |
| 10 | Settings | Guest Account / This device only, Link Email; incoming faxes Enable, notifications, business/terms/privacy/support | Link email or enable services | Guest account indicates some local-only use is possible. [OBSERVED] |
| 11 | Settings | Same with bottom of settings; Delete account | Settings actions | Account deletion is visible; no repeat-send evidence. [OBSERVED] |

## Eight lens dimensions

1. **First win:** The app prepares a one-page PDF and displays the “Your Fax is Ready” message (p.8–9), but no actual successful delivery is shown. This is a preparation milestone, not proof of benefit from transmission. Taps and first delivery are [UNKNOWN].
2. **Ask ledger:** no early asks visible in first home states (p.1–3); receive-number subscription appears p.4–5; a prepared document precedes “Tap Continue to send it now” subscription p.9; account linking is optional-looking in settings (p.10). Static order does not prove the entire interaction path.
3. **Abstractions:** Incoming vs outgoing fax filters, number service, drafts, attachment, document readiness (p.1–2, p.6–9), guest vs linked email (p.10). These labels mostly map to tasks/states; “fax ready” should not imply sent. [INFERRED]
4. **Feel-good:** One-page preview and clear ready state (p.8–9) create a concrete preparation milestone. “Highest priority / HIPAA compliant / No fax limits” is sales copy, not user progress (p.9).
5. **Feel-bad:** The ready state immediately leads to a subscription request before tapping to send in the displayed sequence (p.9); users could mistake readiness for successful delivery. No close affordance is visible on p.4/p.9, though may exist outside captured area.
6. **Paywall:** Receiving wall before number acquisition (p.4), then native ₹199/week purchase sheet (p.5); another similarly priced wall on ready-to-send (p.9). No trial text shown. ₹ is displayed; storefront is not independently verified. Hard/soft gating and dismissibility remain [UNKNOWN].
7. **Repeat cost:** [UNKNOWN]. Drafts filter and home tabs imply retrieval (p.1, p.6), but there is no sent history or second send. Capture return to draft and re-send.
8. **Feature map:** Table stakes: scan/import, recipient, draft, send-state clarity, receive option. Differentiator candidate: guest mode and draft support (p.6, p.10). Bloat/cost candidate: duplicate ₹199/week paywall moments and marketing claims at the send trigger (p.4, p.9). [INFERRED]

## Keep / Kill / Different

- **Keep:** Prepare and preview the document before asking for purchase (p.7–8); guest account with optional email linking (p.10).
- **Kill:** Avoid labeling a document “ready” if the next meaningful step is still blocked behind an unclear subscription gate (p.9). Don’t show identical weekly asks at both receive and send without explaining what each unlocks (p.4, p.9).
- **Different:** Use distinct, task-specific purchase moments: explain number rental only on Receive; disclose send charge/allowance beside recipient and page count. Name the p.9 state “Document ready to send,” then show an explicit send confirmation. [INFERRED]

## Verification and unknowns

Checked every page and enlarged p.4–5, p.7–9. Confirmed the displayed ₹199 per week and the text “Tap Continue to send it now.” The ~40s label is UI copy only, not verified processing duration. App identity, US prices, close behavior, send success, and repeat taps are [UNKNOWN].
