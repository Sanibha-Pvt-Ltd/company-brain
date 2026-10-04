---
type: app
category: fax
app: FaxFree (faxx capture)
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:17]
---

# FaxFree — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/faxx.pdf` (17 pages). The PDF filename is “faxx”; visible app name is FaxFree. Storefront uses ₹; these are not US prices.

## Screen map

| # | Stage | What user sees | Ask / exact copy / lever | Friction / evidence |
|---|---|---|---|---|
| 1 | Launch | Fax icon/loading | None visible | No value yet. [OBSERVED] |
| 2 | Tracking | iOS tracking prompt over welcome | “Allow ‘FaxFree’ to track your activity across other companies’ apps and websites?” | Before app benefit. [OBSERVED] |
| 3 | Welcome | “Create, edit, and send unlimited faxes and save your fax in JPG or PDF formats.” | Continue; terms/privacy | Benefit statement, no task yet. [OBSERVED] |
| 4 | Onboarding | “Get Access to Unlimited Faxes”; review quote and 1.7M+ users trust us | Continue | Social proof; no first fax shown. [OBSERVED] |
| 5 | Onboarding | “Get Secure and Cheap Fax for Your Device”; sends documents worldwide | Continue | Generic benefit claim. [OBSERVED] |
| 6 | Onboarding | “Create Finest Scans and Fax on the Go”; send high-quality scans; convert to PDF/JPG | Continue | Scan/export value. [OBSERVED] |
| 7 | Subscription | “Choose Your Plan”; Receive faxes, unlimited faxes to 90+ countries, no ads, fax delivery tracking; yearly ₹3,999/year, monthly ₹1,199/month, weekly ₹999/week; “Not sure yet? Try it for free!” | Continue; close X; selected annual; trial-toggle wording | Trial terms/length not shown. Prices are displayed in ₹; storefront is not independently verified. [OBSERVED] |
| 8 | Compose | Send Fax, recipient +91, sender details, Add Document | Enter recipient / add document | First usable task appears after onboarding/paywall in supplied sequence; order is not guaranteed. [OBSERVED] |
| 9 | Camera prompt | iOS camera permission over compose | “Allow ‘FaxFree’ to access your camera” | Permission tied to scan. [OBSERVED] |
| 10 | Scan | “Automatic border detection”; camera view | Capture page | Useful automatic aid; no output yet. [OBSERVED] |
| 11 | Scan editor | Crop/resize, adjust brightness/contrast; one page; save/check | Confirm scan | Concrete document preview. [OBSERVED] |
| 12 | Compose | “1 page added”; recipient field populated; Send Fax | Send | Prepared doc, no delivery status. [OBSERVED] |
| 13 | Paywall | “Unlock Full Access”; same yearly/monthly/weekly prices; “Not sure yet? Try it for free!” | Continue; close X | Appears again in supplied pages; trigger and trial terms unknown. [OBSERVED] |
| 14 | Documents | My Documents, Sent / Inbox, one Draft | Search draft/name | Supports draft list. [OBSERVED] |
| 15 | Notifications | iOS “Would Like to Send You Notifications” | Allow / Don’t Allow | Appears over documents; reason text not visible. [OBSERVED] |
| 16 | Paywall | Repeat full access plans | Continue / close | Duplicate in capture; trigger unknown. [OBSERVED] |
| 17 | Settings | Signed in with Apple, sender name/phone, upgrade, app PIN, start screen, rating, FAQ | Configure settings | Account is visible after task pages; no delivery confirmation. [OBSERVED] |

## Eight lens dimensions

1. **First win:** The scan can be cropped/adjusted and attached as one page (p.10–12). No transmitted fax or delivery update is shown. Exact taps/first-win time and access before payment are [UNKNOWN].
2. **Ask ledger:** tracking prompt (p.2), four welcome/value pages (p.3–6), plan choice (p.7), recipient/document (p.8), camera (p.9), possible repeated plan ask (p.13, p.16), notifications (p.15). These are the screenshot pages, not a verified clickstream. The first concrete output is scan preview/attachment p.11–12.
3. **Abstractions:** Unlimited plan, fax to 90+ countries, trial offer, export format JPG/PDF, scan adjustments, draft/document folders (p.3–7, p.11, p.14). JPG/PDF is a sensible user choice; global coverage and tier language can be deferred until use case requires it. [INFERRED]
4. **Feel-good:** Automatic border detection and editable crop/brightness (p.10–11) give useful control; one-page-added banner confirms preparation (p.12). Review quote and 1.7M+ users are social proof (p.4), not achieved progress.
5. **Feel-bad:** Tracking before value (p.2), repeated plan screens in set (p.7, p.13, p.16), and vague “Try it for free!” with no visible trial duration or renewal detail on those walls (p.7, p.13, p.16). The native purchase contract is absent, so do not infer a hidden trial.
6. **Paywall:** Wall at p.7 and repeated at p.13/p.16; close X visible. prices displayed in ₹: yearly ₹3,999, monthly ₹1,199, weekly ₹999. Annual is selected on p.7. Trial toggle exists but length/renewal terms are [UNKNOWN].
7. **Repeat cost:** [UNKNOWN]. Draft/Sent/Inbox labels and one Draft appear (p.14); no successful fax/re-send evidence. Count only after hands-on path.
8. **Feature map:** Table stakes: scan/import, recipient, document queue, send/status, saved draft. Differentiators: auto border detection and delivery tracking/export to JPG/PDF claims (p.3, p.6, p.10–11). Bloat/cost: tracking permission before benefit, four intro screens and duplicated paywalls (p.2–7, p.13, p.16). [INFERRED]

## Keep / Kill / Different

- **Keep:** Auto border detection, adjustable scan, and one-page-added confirmation (p.10–12); drafts (p.14).
- **Kill:** Early tracking prompt (p.2), redundant onboarding before getting to compose (p.3–6), and repeated generic plan walls without new context (p.7, p.13, p.16). Do not say “try it for free” without visible trial length and renewal amount.
- **Different:** Show one optional concise benefit page, then start compose; let the user prepare a scan before an honest price/trial decision that states the duration and post-trial price beside the CTA. [INFERRED]

## Verification and unknowns

Reviewed all 17 pages and full-size p.2, p.7–8, p.11, p.13, p.15. Confirmed visible plan amounts, “Try it for free!”, 1.7M+ claim, and scan controls. The 1.7M figure and review are app claims, not verified data. Trial terms, whether wall is dismissible in all states, US pricing, delivery, and repeat taps remain [UNKNOWN].
