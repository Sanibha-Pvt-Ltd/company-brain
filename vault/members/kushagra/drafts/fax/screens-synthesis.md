---
type: category-screens
category: fax
member: kushagra
updated: 2026-10-04
status: draft
scope: screens-only
sources: [screenshots:121]
---

# Fax apps: screen synthesis

Eight supplied in-app capture PDFs, 121 pages total. This is a screen audit, not a market or review study. The source filenames and app-note links below are the evidence map. `Fax_category analysis.pdf` is secondary commentary, not evidence here. Visible `₹` values are reported as displayed INR; storefront was not independently verified, capture date is unknown, and US prices are unknown. A screenshot sequence is not a verified clickstream: no exact tap counts, session times, or path order are inferred. Recommendations below are proposals `[INFERRED]`, not observed product facts.

**Strongest finding [OBSERVED]:** these captures repeatedly take a user from document preparation toward a send decision, but none reaches evidence of delivery. A populated compose screen, “ready” label, or blue send control proves readiness at most. It says nothing about whether a fax left the device, reached a provider, or was accepted by its destination. That evidence boundary is product-relevant: the most meaningful post-send screen is absent from this sample, not necessarily from the products.

## App evidence map

- [[members/kushagra/apps/fax/fax-by-municorn]] — `Fax by municorn.pdf` (12 pages).
- [[members/kushagra/apps/fax/faxer]] — `Faxer.pdf` (13 pages).
- [[members/kushagra/apps/fax/tinyfax]] — `Tinyfax.pdf` (16 pages).
- [[members/kushagra/apps/fax/genius-fax]] — `fax_genius.pdf` (18 pages).
- [[members/kushagra/apps/fax/faxapp]] — `faxapp.pdf` (11 pages; exact product identity unresolved).
- [[members/kushagra/apps/fax/fax-plus-by-alohi]] — `faxplus by alohi.pdf` (17 pages).
- [[members/kushagra/apps/fax/faxfree]] — `faxx.pdf` (17 pages; visible name FaxFree).
- [[members/kushagra/apps/fax/ifax]] — `ifax.pdf` (17 pages).

## Cross-app evidence table

“First visible value” is the clearest useful state pictured, not proof of a completed job. “Actual outcome” means a delivery receipt/status evidenced in these supplied pages. Asks are named rather than counted because captures do not establish that they occur on one mandatory path. Absence here means “not shown,” never “the app lacks it.”

| App | First visible value → evidenced outcome | Asks / abstractions visible in supplied pages | Monetization evidence | Repeat cost shown |
|---|---|---|---|---|
| Municorn | Prepared scan p.6; compose screen populated p.8 → no delivery evidence. | Privacy/tracking and camera prompts p.1–4; sending vs receiving, number area code, cover page. | Walls p.7, p.11: ₹949/week, ₹2,799/month, ₹23,900/year. Dismissal and trigger unknown. | Sent list empty p.9; repeat path unknown. |
| Faxer | Document plus recipient ready in compose p.6 → no delivery receipt. | Tracking prompt p.1; source choice p.4; rating prompt overlays compose p.6; cover page and scan controls. | p.7–9 show a ₹99 offer and ₹999/week renewal language/native sheet; exact trigger/path unknown. | History empty p.3; repeat path unknown. |
| Tinyfax | Scan preview p.12 and p.15 → no delivery evidence. | Account/later choice p.1, send/receive split, email p.5, notifications p.6, own number and scan modes. | Separate send/receive offers p.2–3 and p.9/p.16; visible weekly values include ₹499 send and ₹999 receive. Terms/path not reconciled. | No completed send; unknown. |
| Genius Fax | Page-credit model and compose p.9–10/p.13; scan p.14–15 → no delivery evidence. | Intro/account choice p.1–6, push p.7, credits, rental number and one-credit-per-page concept. | Credits p.9–10: ₹99/1, ₹699/10, ₹1,999/50; number rental p.11–12 separately. | Home says no sent faxes p.8; unknown. |
| Fax App (`faxapp`) | One-page document p.8; “Your Fax is Ready” p.9 → no send result. | Receive-number offer p.4–5; guest/email choice p.10–11; draft. | ₹199/week receive offer p.4–5 and another wall at ready state p.9. Close affordance not established. | Draft visible p.6; resending behavior unknown. |
| Fax.Plus | File attached p.12–13; compose available p.1 → no delivery evidence. | File source p.11; subscription/business tiers, quotas, integrations, teams, number porting and cover sheet. | Several plan pages p.3–9; Premium shows ₹1,999/month and ₹17,900/year (visible amounts only). | No successful send or resend flow in captures. |
| FaxFree (`faxx`) | Scan ready/attached p.11–12 → no delivery evidence. | Tracking p.2, intro p.3–6, camera p.9; JPG/PDF and draft concepts. | Wall p.7 and repeated p.13/p.16; ₹999/week, ₹1,199/month, ₹3,999/year. “Try it for free!” terms unclear. | Draft p.14; repeat behavior unknown. |
| iFax | Editable page p.8–9 → no delivery evidence. | Paywall p.1–2, number selection p.3, another bundle p.4, notifications p.6; urgency, cover and folders. | Different captured offers: ₹3,499/month after 7 days p.1–2/p.10; ₹1,999/month p.4; ₹999/week native sheet p.11. Not merged into one offer. | No sent fax shown p.5; unknown. |

## Patterns and implications

1. **Document preparation is tangible progress; delivery is a distinct, unobserved outcome.** Faxer p.6 has a recipient and document in compose, Fax App p.8–9 labels an attached file ready, FaxFree p.12 shows a scan ready, and Genius Fax p.13 ties pages to credits. These are useful review points before transmission. The counterexample to a simple “prepare first, charge later” rule is Genius Fax: page credits and number rental are explicit parts of its visible model (p.9–13), while other captures show subscription walls at different stages. Build implication [INFERRED]: state the document’s readiness, then show destination, page count, and charge before the send action; do not imply delivery until a provider response confirms it.

2. **Pricing models map to different jobs, not one clean category-wide offer.** Genius Fax separates page credits from number rental (p.9–12); Tinyfax visibly separates sending and receiving plans (p.2–3); Fax.Plus exposes individual/business/enterprise plans (p.3–9); iFax shows multiple billing presentations (p.1–4, p.10–11). These differences may reflect genuine product scope, capture branches, or offer states; screenshots cannot decide which. Build implication [INFERRED]: ask whether the user is sending once, sending repeatedly, or renting a number, then price that selected job in one legible unit. Do not make a one-off sender learn a receive-number abstraction.

3. **Account and permission asks appear alongside core progress, but path order is uncertain.** Municorn includes privacy/tracking/camera prompts (p.1–4), Faxer tracking (p.1), Tinyfax sign-up/later and notifications (p.1, p.5–6), and FaxFree tracking (p.2). Conversely, Fax App has a guest/email choice only in p.10–11, after its ready state at p.9. This counterexample means “all apps require accounts before value” is not supported. Build implication [INFERRED]: defer optional identity, notification, and tracking asks until the user requests their benefit; camera access belongs at the moment Scan is chosen.

4. **Receiving a number is a separate commitment from sending a document.** Tinyfax has different send/receive walls (p.2–3, p.8–10), Fax App’s receive-number wall (p.4–5), and Genius Fax number rental (p.11–12) make the separation visible. Municorn’s area-code/number concept (p.7) is another visible receiving affordance. Counterexample: some captures do not make receive a prominent first-run step, and Fax.Plus’s enterprise needs may legitimately bundle numbers. Build implication [INFERRED]: make “Send a fax” and “Get a fax number” separate entry intents, with bundle options only for users choosing business workflows.

5. **Plan consistency and trial comprehension are unresolved risks, not proven dark patterns.** Faxer’s p.8–9 offer/native-sheet sequence contains ₹99 and ₹999/week language; FaxFree repeats plan pages p.7, p.13, p.16; iFax shows distinct monthly/weekly presentations p.1–4 and p.10–11. These may be separate products or paths. Static captures cannot prove a hidden close, actual charge, trial eligibility, or that one person encountered all offers. Build implication [INFERRED]: maintain one canonical offer per selected action and mirror term, renewal amount and period through the native purchase step; verify hands-on before making claims about competitor behavior.

6. **The repeat loop cannot be evaluated from these pages.** Empty history in Municorn p.9, Faxer p.3, Genius Fax p.8 and iFax p.5, plus a draft in Fax App p.6 and FaxFree p.14, establish only the displayed states. They do not show retrieval after success, repeat sending, failure recovery, or receipt retention. Build implication [INFERRED]: treat durable status and a searchable receipt as core follow-through, then test the actual repeated task before optimizing convenience.

## Working hypothesis verdicts (proposed in this synthesis; INFERRED)

| Working hypothesis | Verdict from these pages | Reason and limit |
|---|---|---|
| A sender should understand cost before committing to transmit. | **Supported as a design principle; not validated behavior.** | Credit/page and plan walls appear in several products, but screenshots do not show user comprehension or conversion. The relevant page-level evidence is Genius Fax p.9–13, Tinyfax p.2–3 and iFax p.1–4. |
| A prepared document should be distinguished from a sent or delivered fax. | **Strongly supported by evidence boundary.** | Ready/compose/scan states are visible (Faxer p.6, Fax App p.8–9, FaxFree p.12); no supplied capture proves delivery. This is a terminology and state-design requirement, not proof competitors omit receipts elsewhere. |
| Sending and receiving should be separate entry intents. | **Plausible, supported by visible model separation.** | Tinyfax p.2–3/p.8–10 and Genius Fax p.11–13 separate the offers; Fax.Plus business cases may need bundling. Test with actual task paths. |
| Minimal onboarding is always better for fax. | **Unresolved.** | Some prompts and account screens precede visible document work, but path order and necessity cannot be derived reliably; Fax App’s guest choice appears late (p.10–11). |
| The biggest friction is a hard paywall before send. | **Unresolved.** | Walls are visible at differing stages, but dismissibility, free alternatives, selected path and gating behavior are not established by still captures. |

## Proposed first five minutes

The time label is a planning frame only, not a claim about observed completion time. This is original proposed copy, not competitor text. No invented success guarantee or unverified free allowance is assumed.

| Proposed screen | Ask | Gives | Original proposed copy / behavior | Why, with screenshot evidence |
|---|---|---|---|---|
| Compose entry | None. User selects send or receive. | A clear job choice. | “Send a fax” · “Get a fax number” | Receiving is a distinct paid concept in Tinyfax p.2–3/p.8–10 and Genius Fax p.11–12. |
| Send details | Recipient number; may skip cover page. | Destination is explicit. | “Who should receive this fax?” | Compose is already visible in Faxer p.6 and Fax.Plus p.1; keep recipient and document together. |
| Add document | Choose Files/Photos or Scan; request camera only after Scan. | Preview with page count and crop controls. | “Add pages” / “Scan a page” | Source choices in Faxer p.4 and Fax.Plus p.11; scan previews in Tinyfax p.12/p.15, FaxFree p.10–12. |
| Review | No new ask. | Editable destination, pages, cover choice and task status “Ready to send.” | “Review [page count] pages. Nothing has been sent yet.” | Prepared states in Fax App p.8–9 and Faxer p.6 are useful but are not delivery evidence. |
| Price then transmit | Confirm purchase only if the chosen job requires it; show total and billing period. | A task-matched charge before sending. | “Send [page count] pages · [price shown before confirmation]” | Credit purchase pages (Genius Fax p.9–10/p.13) and subscription offers (iFax p.1–4) show that a price model is needed; exact product pricing remains a business decision. |
| Status / receipt | Optional save/account after status exists. | Provider-confirmed status and a durable record; report uncertainty/failure honestly. | “Submitted” only after provider acceptance; “Delivered” only if the provider returns that state. | No successful delivery is evidenced across the files. This proposal explicitly separates local preparation from external outcome. |

## Differentiators to test (maximum three)

1. **Truthful transmission states.** Source: Fax App “Your Fax is Ready” p.9, Faxer compose p.6 and FaxFree attached scan p.12, with no supplied receipt. Tradeoff: extra status vocabulary can confuse if the provider returns only “submitted.” Falsifier: hands-on testing shows competitors already expose clearer confirmed receipts in routine flows and users understand them without confusion.
2. **Task-matched, legible pricing.** Source: Genius Fax page-credit vs number-rental pages 9–13; Tinyfax send/receive split p.2–3; iFax varied offers p.1–4/p.10–11. Tradeoff: separate intents add a choice and may make bundles less discoverable. Falsifier: user tests show the audience largely wants ongoing bundled sending/receiving and can accurately compare the existing model.
3. **Document review before commitment.** Source: prepared-document states Faxer p.6, Fax App p.8–9, FaxFree p.11–12; Genius Fax p.9–10 displays credit purchase options, but does not by itself establish mandatory gating. Tradeoff: preparing a document before revealing unavoidable cost may create sunk effort; expose the price before final send and test whether users prefer earlier disclosure. Falsifier: observed usability shows users need pricing first to decide whether to scan at all.

## Concepts we would refuse in the basic send path

| Refused concept | Evidence / rationale |
|---|---|
| Separate receive-number rental before a send task | Tinyfax p.8–10, Fax App p.4–5, Genius Fax p.11–12 show number rental as its own offer. Offer it only after receive intent. |
| Page-credit currency without a clear page-to-cost mapping | Genius Fax p.9–10/p.13 makes credits explicit; if used, show the actual pages consumed and remaining value at decision time. Whether a credit model is commercially necessary is unknown. |
| Business tiers and integrations on a one-off send path | Fax.Plus p.3–9 shows the business taxonomy; keep advanced team/API controls behind a business choice. |
| Rating/notification/tracking ask over document review | Faxer rating prompt p.6, Tinyfax notifications p.6, tracking prompts Faxer p.1/FaxFree p.2. Delay until there is a clear user benefit. |
| “Ready” or “sent” language before a matching state exists | Fax App p.9 uses “Ready” and “Tap Continue to send it now”; preserve that distinction rather than collapsing preparation and delivery. |
| Repeated or contradictory offer presentation | FaxFree p.7/p.13/p.16 and iFax p.1–4/p.10–11 show differing offer pages. Their path relation is unknown; our own offer must remain consistent. |

## Open questions, ordered by decision impact

1. **Does the fax reach a recipient, and what status can the provider certify?** Hands-on: on controlled accounts, send a known test document to a controlled fax endpoint; capture client state, provider response, recipient receipt, failures and retries. Decision: status vocabulary, receipt design, and whether “delivered” is supportable.
2. **Where is payment required on each actual path?** Clean-install screen recording for every app, both send and receive intents; record dismiss/skip routes and native purchase terms. Decision: whether a document-first sequence is a real differentiator and how to disclose price.
3. **What is the actual canonical offer and its renewal?** Select each visible plan and inspect native sheet, trial eligibility, total charge, billing period, cancellation and alternate offer states. Decision: competitor price comparison only; current US pricing cannot be supplied by these captures.
4. **Can guest users send, and what persists?** Test guest vs account, close/reopen, delivery record and reinstall. Decision: account timing and receipt retention.
5. **What does repeat use cost?** After one confirmed send, resend to prior recipient, duplicate/edit a document and retrieve receipt; record actual taps and interruption recovery. Decision: repeat-path design and where to put address book/templates.
6. **Resolve source identity.** Match Fax App, FaxFree, and Fax.Plus captures to product/build/store listing and capture context. Decision: confidence in app-level comparisons and labels; until then the exact Fax App identity remains unknown.

## What would change this call

If hands-on capture finds a dependable, user-visible delivery receipt in several products, “receipt transparency” becomes a baseline expectation rather than a differentiator. If most users select receive-number rental or recurring business bundles first, separate intent-first pricing should become a secondary route rather than the default. If payment is consistently required before users can inspect a page, the proposed sequence must disclose price earlier. These are decision rules for new evidence, not claims about the present capture set.

**Next stage:** hands-on flow capture for the six questions above, then decide which product model to prototype. This note does not authorize or imply market/review research.

## Verification and correction record

All 121 pages were visually inventoried; high-resolution source pages for the stated offers, prepared-document states, and empty histories were rechecked in the PDFs. The per-app links preserve detailed screen-by-screen evidence. Important limits carried forward: Fax App product identity unresolved; FaxFree shown as `faxx.pdf`; iFax offers differ across pages and are not reconciled; fax number options do not prove a particular storefront; currency does not establish storefront; static readiness never establishes transmission or delivery. No screenshots are treated as missing-feature proof. No web, review, or market data used.
