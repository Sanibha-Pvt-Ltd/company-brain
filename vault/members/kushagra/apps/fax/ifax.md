---
type: app
category: fax
app: iFax
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:17]
---

# iFax — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/ifax.pdf` (17 pages). Captures show ₹ pricing and India account locale; treat prices as India storefront, not US.

## Screen map

| # | Stage | What user sees | Ask / exact copy / lever | Friction / evidence |
|---|---|---|---|---|
| 1 | First paywall | “Send Unlimited Faxes”; rapid delivery/live updates/HIPAA; “Try for $0.00”; “Pay nothing for now! Free for 7 days, then only ₹3,499.00/month. Cancel anytime.” | Continue; close X; Restore | Trial duration and renewal price displayed. $0.00 headline conflicts visually with ₹ renewal locale; qualify as screenshot framing, not charge amount. [OBSERVED] |
| 2 | Apple sheet | “Send Only Monthly”; 1-week free trial, then ₹3,499/month; auto-renew terms | Confirm with Side Button | Native terms corroborate trial and renewal. [OBSERVED] |
| 3 | Select number | “Select your fax number”; US states and area codes; Continue with selected (205) 575-0915 | Choose a number | Number choice follows paywall in set; exact path unknown. [OBSERVED] |
| 4 | Send/receive paywall | “Send & Receive Unlimited Faxes”; email updates, HIPAA; Continue; free for 7 days then ₹1,999/month | Continue; close X | Different bundle/amount from p.1. Why the plan changed is unknown. [OBSERVED] |
| 5 | Home | iFax “START FREE / Send a Fax”; Get a Free Number; plus button; Recents/Folders/Settings | Get a free number or start task | Home is visible after paywall/number selection in set; no fax yet. [OBSERVED] |
| 6 | Notifications | iOS notification request over home | Allow / Don’t Allow | Timing after first paywall, before shown fax task. [OBSERVED] |
| 7 | New fax | Form template with recipient fax number, To, From, Subject, urgency checkboxes; Scan or Add Document | Enter recipient and sender/form details; add document | Template includes optional cover-page-like fields; no send button result. [OBSERVED] |
| 8 | Add document | Cover Page toggle; Scan Document, Blank Page; import Files, Gallery, Mail, Google Drive, Dropbox, Box, computer, URL | Choose source | Broad import choice; many options beyond core. [OBSERVED] |
| 9 | Document editor | Edit Document, scan preview, Filters / Adjust / Reorder | Adjust then confirm | Page preview appears, output quality not verified. [OBSERVED] |
| 10 | Send paywall | “Send Your Fax Now”; Rapid Delivery/Live Updates/HIPAA; Continue; “Pay nothing for now! Free for 7 days, then only ₹3,499.00/month.” | Continue; X/Restore | Same monthly trial wall immediately adjacent to send in supplied order. [OBSERVED] |
| 11 | Apple sheet | “Send Only Weekly”; ₹999/week; auto-renew terms | Confirm with Side Button | Weekly offer differs from monthly wall; trigger unknown. [OBSERVED] |
| 12 | Number selection | Select your fax number / area codes; continue with selected number | Choose number | Repeated number choice. [OBSERVED] |
| 13 | Folders | Empty Folders state, Create Folder | Create optional folder | Organizational feature before no fax shown. [OBSERVED] |
| 14 | Settings | Login; Touch ID; notifications; cover-page details; support; “Try Our Apps” | Login/settings | Login option, rather than mandatory signup, is visible. [OBSERVED] |
| 15 | Login sheet | Continue with Google/Apple/Microsoft or email; “iFax Account” | Sign in | Separate account path. [OBSERVED] |
| 16 | Cover page | Default template, sender name, company logo, instructions | Fill sender info / pick template | Can be customized; setup can add work for a one-off fax. [OBSERVED] |
| 17 | Template gallery | Several cover-page templates and no-cover option | Choose template | Optional selection adds choice; no fax content. [OBSERVED] |

## Eight lens dimensions

1. **First win:** A scanned/imported page can be edited (p.8–9), but no send receipt or successful outcome appears. First delivery/taps and whether it precedes payment are [UNKNOWN].
2. **Ask ledger:** subscription trial wall in first capture (p.1–2), number selection (p.3), a second send/receive wall (p.4), notifications (p.6), recipient/sender/document form (p.7–9), another paywall at send moment (p.10–11), account login or cover-page details if pursued (p.14–17). Sequence is screenshot order and not a verified single-user clickstream.
3. **Abstractions:** Separate send-only vs send/receive subscriptions, number selection, urgency flags, custom cover templates, folders, login providers, delivery claims (p.1–17). Recipient and document are core; template, folder, identity, and urgency concepts are optional or deferred. [INFERRED]
4. **Feel-good:** Broad document-source choice and editable page (p.8–9); transparent native trial terms p.2. “Send Your Fax Now” is an action cue, not delivery success (p.10).
5. **Feel-bad:** $0.00 headline followed by ₹3,499/month renewal (p.1) creates currency confusion in this India capture; below it, “Pay nothing for now!” makes trial salient while renewal appears smaller. A second send/receive wall is shown (p.4), followed by weekly Apple offer (p.11). The terms remain technically visible. [OBSERVED]
6. **Paywall:** trial offer at p.1 (7 days then ₹3,499/month), native confirmation p.2; send/receive bundle p.4 says ₹1,999/month after 7 days; send moment p.10 repeats ₹3,499/month; weekly purchase p.11 is ₹999/week. Differences may reflect distinct products/offers and cannot be reconciled from screenshots. X visible on in-app walls. India prices.
7. **Repeat cost:** [UNKNOWN]. Recents and folders imply document organization (p.5, p.13), but no delivered item or repeat send path appears. Capture return to a prior recipient/document.
8. **Feature map:** Table stakes: recipient, scan/import, cover page, send status. Differentiator candidate: many cloud/import routes and live delivery updates (p.8, p.10). Bloat/cost for a basic sender: pre-send folder creation, multiple cover choices, multi-provider login, and repeated plan/number choice (p.3–4, p.10–17). [INFERRED]

## Keep / Kill / Different

- **Keep:** Trial renewal terms appear in the Apple sheet (p.2); broad import options (p.8); editable scan before send (p.9); login is not presented on first home screenshot (p.5).
- **Kill:** Conflicting $0.00/₹ framing in an India storefront (p.1), duplicate paywalls and number-selection steps without clear differences (p.1–4, p.10–12), and early folder/template work (p.13, p.16–17).
- **Different:** Show one consistent storefront currency and one plan for the user’s chosen task; let them prepare the fax first, then present a single price/trial with renewal in the same visual hierarchy. Defer folder and cover-page customization behind an optional action. [INFERRED]

## Verification and unknowns

Checked all 17 pages and enlarged p.1–4, p.7–12, p.16–17. Confirmed both renewal amounts ₹3,499/month and ₹1,999/month, weekly ₹999 and free 7-day copy. The screenshot set contains mixed offers; do not collapse them into one price. Why plans differ, US pricing, number availability, paywall gates, delivery, and repeat taps are [UNKNOWN].
