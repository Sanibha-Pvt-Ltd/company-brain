---
type: app
category: fax
app: Faxer
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:13]
---

# Faxer — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/Faxer.pdf` (13 pages). The +91 field and ₹ amounts are visible; storefront is not independently verified and US prices are [UNKNOWN].

## Screen map

| # | Stage | What is visible | Ask / copy / lever | Friction |
|---|---|---|---|---|
| 1 | Launch | iOS tracking prompt | “Allow ‘Faxer’ to track your activity across other companies’ apps and websites?” | Tracking ask before demonstrated fax benefit. [OBSERVED] |
| 2 | New fax | Recipient number, “No files yet,” Add files & cover | Choose recipient and file; scan/import available per p.4. | Empty compose state. [OBSERVED] |
| 3 | History | “You haven’t sent any faxes yet” / Start new fax | Start New Fax. | No success yet. [OBSERVED] |
| 4 | Add file | Options: Cover page (recommended), Scan with camera, Import from gallery/files/other apps | Choose source. | Useful choice set; “recommended” cover page adds an optional step. [OBSERVED] |
| 5 | Scan editor | Black/white scan, brightness and threshold sliders, Save | Adjust and save. Banner: “We always use black and white to guarantee reception with any fax machine.” | Gives editing control but scan quality can require manual judgment. [OBSERVED] |
| 6 | Compose | Recipient populated; captured page; add files & cover; Send fax; transient five-star prompt overlays document | “Enjoying Faxer? Tap a star to rate it on the App Store.” Buttons include Not Now. | Rating request overlays the prepared fax before any send confirmation in this capture. [OBSERVED] |
| 7 | Paywall | “Fax With No Limits / International faxing”; 1-week, 1-month, 1-year | ₹999/week; ₹2,999/month (₹692.07/week); ₹24,900/year (₹478.84/week, “SAVE 52%”). Continue; “Then ₹999.00/week. Cancel anytime.” | Visible close X and Restore. No free trial shown. [OBSERVED] |
| 8 | Special offer | “Try for a full week just for ₹99.00”; Start 7-Day Access; then ₹999/week | Start 7-Day Access | Follow-on offer in capture sequence after main plans; not proof that closing p.7 triggers it. [OBSERVED] |
| 9 | Apple purchase sheet | 1 Week Lite, ₹99/week 1-week offer, then ₹999/week starting 9 Oct 2026; auto-renew terms | Confirm with Side Button | Native purchase confirmation clearly states renewal terms; ₹ is displayed; storefront is not independently verified. [OBSERVED] |
| 10 | Discard | “Discard draft? This action cannot be undone.” Cancel / Discard | Confirm destructive discard. | Clear confirmation reduces accidental loss. [OBSERVED] |
| 11 | Paywall | Same plans as p.7 | Continue; Restore; close X | Repeated in supplied set; trigger unknown. [OBSERVED] |
| 12 | Settings | Restore, share, FAQ, contact, themes, terms/privacy | Select a settings item | Settings breadth, no repeat shortcut evidence. [OBSERVED] |
| 13 | Theme setting | “Choose the appearance”: Light, Dark, System theme | Choose appearance | Optional preference, not required fax concept. [OBSERVED] |

## Eight lens dimensions

1. **First win:** A scan is edited/saved (p.5) and a page appears with recipient entered (p.6), but no completed transmission or receipt exists. First delivered fax and exact taps are [UNKNOWN].
2. **Ask ledger:** tracking permission (p.1); recipient/document source (p.2, p.4); camera permission timing is not shown, although camera source is offered (p.4); rating ask overlays compose (p.6); subscription (p.7), followed by a lower-price offer and Apple purchase sheet in the supplied pages (p.8–9). Page order alone cannot prove every transition.
3. **Abstractions:** International sending, unlimited plans, document/cover selection, scan threshold/brightness, theme selection (p.4–5, p.7, p.13). Scan editing serves legibility; theme choice can wait. [INFERRED]
4. **Feel-good:** Editable scan preview and explicit black-and-white rationale (p.5) are useful control. Five-star prompt and “no limits” pitch do not reflect completed progress. [OBSERVED]/[INFERRED]
5. **Feel-bad:** Rating prompt overlays the in-progress compose view (p.6). Close on primary wall is visible (p.7), but the supplied sequence also contains a ₹99 7-day offer then ₹999/week renewal (p.8–9); users need the renewal amount close to the offer. The screenshots do show it on p.8/p.9. [OBSERVED]
6. **Paywall:** Main wall shows three plans and no trial (p.7); a special offer and purchase sheet follow in the set (p.8–9), with the native sheet spelling out renewal. Displayed amounts are in ₹; storefront is not independently verified. The screenshot set does not establish whether the offer is a downsell after close.
7. **Repeat cost:** [UNKNOWN]. History is empty (p.3); no delivered fax or resend flow. Capture a completed send, then the shortest second-send path.
8. **Feature map:** Table stakes: recipient, import/scan, edit/preview, send, history. Differentiator candidate: scan contrast controls and global framing (p.5, p.7). Bloat/cost: early tracking and an in-compose rating prompt (p.1, p.6), plus theme choice outside core job (p.12–13). [INFERRED]

## Keep / Kill / Different

- **Keep:** Document-source chooser (p.4), simple brightness/threshold editing with preview (p.5), and irreversible discard confirmation (p.10).
- **Kill:** Tracking ask before value (p.1) and rating overlay on a draft (p.6). Do not make the user decode three plan cadences before proving delivery.
- **Different:** Place subscription after document + recipient are ready; state total renewal price and date on the offer itself, with a plainly visible dismiss action. Show the review prompt only after a confirmed successful send. [INFERRED]

## Verification and unknowns

Checked all 13 pages and full-size p.6–9. Confirmed amounts displayed in ₹ and exact labels in the main plans and Apple sheet. US pricing, paywall blocking behavior, offer trigger, delivery success, and repeat taps are [UNKNOWN].
