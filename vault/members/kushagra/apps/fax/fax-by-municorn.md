---
type: app
category: fax
app: Fax by Municorn
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:12]
---

# Fax by Municorn — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/Fax by municorn.pdf` (12 pages). The captures show a +91 number field and prices in ₹; storefront is not independently verified. All claims refer only to the supplied screenshots.

## Screen map

| # | Stage | What user sees / gives | Asks, exact copy, and lever | Friction / evidence |
|---|---|---|---|---|
| 1 | Consent | Privacy Settings sheet, buttons “Deny” / “Accept All” | Consent to third-party technologies; copy says data provides services and may be used for future changes. | Consent precedes visible fax value. [OBSERVED] p.1 |
| 2 | New fax / tracking | Compose screen dimmed behind iOS tracking request | “Allow ‘Fax’ to track your activity across other companies’ apps and websites?” | Tracking prompt arrives before a document is shown. [OBSERVED] p.2 |
| 3 | Compose | Blank recipient (+91), Add Cover page, Add image or document, Send disabled | Adds document; recipient field visible. | Empty form; no benefit yet. [OBSERVED] p.3 |
| 4 | Camera | Camera interface behind permission dialog | “Allow ‘Fax’ to access your camera”; explanation says camera takes pictures of documents to be sent. | Permission is relevant to scan path; timing before any shown document. [OBSERVED] p.4 |
| 5 | Scan | Live camera image with Retake / Keep | Keep or retake capture; no textual benefit claim. | No success confirmation or page quality output shown. [OBSERVED] p.5 |
| 6 | Compose | Recipient still empty; captured Picture1.jpg appears as one page; Add image or document | Send remains disabled while recipient is blank. | A prepared page is visible before the number is entered. [OBSERVED] p.6 |
| 7 | Subscription | “Send and Receive Unlimited Faxes / All over the world”; weekly, monthly, yearly options; Subscribe | ₹949/week, ₹2,799/month (₹632.03/week), ₹23,900/year (₹458.36/week; “SAVE 52%”). “Over 200,000 people rated us / Our average rating is 4.8.” | Paywall has Restore, but no visible close control in this capture. No trial terms shown. Price is displayed in ₹; storefront is not independently verified. [OBSERVED] p.7 |
| 8 | Compose | Number populated (+91 8858502558), one page attached, Send active | Tap Send is implied by button label; no delivery outcome shown. | Screenshot order places this after paywall, but does not prove the transition or whether purchase was required. [OBSERVED] p.8 |
| 9 | Sent | Empty state “No sent faxes” | Search field; tab navigation. | Does not confirm a sent fax. [OBSERVED] p.9 |
| 10 | Number selection | “Choose area code”; US +1 selector, search and city list | Choose/search an area code; “Random phone number.” | Number selection adds a separate task for receiving. [OBSERVED] p.10 |
| 11 | Subscription | Same subscription options and prices displayed in ₹ as p.7 | Subscribe; Restore. | Appears again in supplied sequence; trigger is unknown. [OBSERVED] p.11 |
| 12 | Info/settings | Buy Subscription, FAQ, online faxing for business, support, privacy, terms, delete account | Purchase is one of several settings actions. | No repeat-send shortcut evidenced. [OBSERVED] p.12 |

## Eight lens dimensions

1. **First win:** The earliest tangible preparation shown is a captured page on the compose form (p.6). No completed transmission, delivery receipt, or “sent” state is shown; first-win screens/taps and paywall relationship are therefore [UNKNOWN]. The active Send button on p.8 is not proof of delivery.
2. **Ask ledger:** privacy choice (p.1), tracking consent (p.2), camera permission (p.4), document and recipient entry (p.3, p.6, p.8), then subscription choice in the supplied sequence (p.7, p.11). The screenshots do not establish the exact tap sequence or what was received before each ask; the scanned page is visible by p.6.
3. **Abstractions:** Recipient number, optional cover page, sending versus receiving, area code/virtual number, and subscription plans (p.3, p.7, p.10). Sending a document requires recipient and document; separate receiving-number purchase is a product boundary, not an obvious prerequisite to sending. [INFERRED]
4. **Feel-good:** The page preview in compose (p.6) gives concrete evidence that a document is prepared. The 4.8 average rating / 200,000 raters is social proof on the paywall, not user progress. [OBSERVED]/[INFERRED]
5. **Feel-bad:** The prompt stack asks privacy, tracking, and camera access before a completed fax is evidenced (p.1–4). The paywall has no visible close button in p.7/p.11; whether it is hard or dismissible cannot be established. Exact copy “Send and Receive Unlimited Faxes” suggests broad value while only the screen supports a subscription ask. [OBSERVED]
6. **Paywall:** Subscription screen appears between prepared capture and populated send form in the supplied page order (p.6–8); causality and whether access is blocked are [UNKNOWN]. US prices are [UNKNOWN]; storefront is not independently verified. Weekly is selected in p.7; annual is marked “SAVE 52%.” No trial or downsell is visible.
7. **Repeat cost:** [UNKNOWN]. Screens show New Fax, Sent, Inbox, and Info tabs (p.9, p.12), but no successful first send or repeat flow. Capture a completed send and return-send path to count taps.
8. **Feature map:** Table stakes: recipient, document attachment/scanning, cover page, send status/history. Differentiator candidate: receiving number and area-code selection. Bloat/cost candidate: account-area upsell and tracking consent before demonstrated value. This classification is [INFERRED] from p.1–12.

## Keep / Kill / Different

- **Keep:** Inline one-page preview before sending (p.6); it makes the fax payload inspectable. Keep separate sending and receiving labels (p.7, p.9–10) if both jobs are supported.
- **Kill:** Do not require tracking consent to reach the compose form (p.2). Avoid asking for camera before showing import alternatives (p.4; p.3 offers images/documents). Do not repeat a subscription screen without a visible value explanation (p.7, p.11).
- **Different:** Let a user import or scan, inspect the page, enter recipient, and see a clear send price or free allowance before asking for a subscription. If receiving-number service is paid, present that price only when the user chooses “Receive.” [INFERRED]

## Verification and unknowns

Re-opened the complete 12-page source, contact sheet, and full-size p.7 pricing screen. Confirmed ₹949/week, ₹2,799/month, ₹23,900/year, displayed weekly equivalents, and verbatim “SAVE 52%” / rating copy. US pricing, paywall dismissibility, exact interaction order, first delivered fax, and repeat-send tap count remain [UNKNOWN].
