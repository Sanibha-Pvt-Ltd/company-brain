---
type: category-lens
category: fax
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:121]
---

# Fax apps — screenshot synthesis

Screens-only review of eight app capture PDFs (121 pages total). Sources display ₹ amounts and sometimes US/Canada fax-number options. The storefront is not independently verified; do not treat the displayed amounts as US prices. Category analysis PDF was not used as screenshot evidence; no market or review research was conducted.

## Per-app notes

- [[members/kushagra/apps/fax/fax-by-municorn]] — `Fax by municorn.pdf`, 12 pages.
- [[members/kushagra/apps/fax/faxer]] — `Faxer.pdf`, 13 pages.
- [[members/kushagra/apps/fax/tinyfax]] — `Tinyfax.pdf`, 16 pages.
- [[members/kushagra/apps/fax/genius-fax]] — `fax_genius.pdf`, 18 pages.
- [[members/kushagra/apps/fax/faxapp]] — `faxapp.pdf`, 11 pages; exact app-store identity unknown.
- [[members/kushagra/apps/fax/fax-plus-by-alohi]] — `faxplus by alohi.pdf`, 17 pages.
- [[members/kushagra/apps/fax/faxfree]] — `faxx.pdf`, 17 pages; visible app name FaxFree.
- [[members/kushagra/apps/fax/ifax]] — `ifax.pdf`, 17 pages.

## Pattern table

Still screenshots are not reliable clickstreams. Exact taps to first delivery, a numeric count of asks on one path, the number of taps for repeat use, and successful fax outcomes cannot be computed from these files. The table reports what the captures establish without treating page order as a proven transition.

| App | First win / taps | Visible asks before prepared document (screenshot evidence) | Concepts added beyond recipient + document | Paywall evidence | Repeat cost |
|---|---|---|---|---|---|
| Fax by Municorn | Prepared scan p.6; no delivery. Taps unknown. | Privacy/tracking/camera prompts p.1–4; sequence uncertain. | Sending vs receiving; separate area-code number; cover page; subscription cadence. | p.7, p.11; ₹949/week, ₹2,799/month, ₹23,900/year (storefront unverified); dismissibility unknown. | Unknown; sent list empty p.9. |
| Faxer | Prepared scan + recipient p.6; no delivery. | Tracking p.1; document-source choice p.4; in-compose rating p.6. | Cover page; scan threshold/brightness; international plans. | Main wall p.7; ₹99 special offer then ₹999/week renewal in p.8–9 capture sequence; trigger unknown. | Unknown; history empty p.3. |
| Tinyfax | Scan preview p.12/p.15; no delivery. | Sign-up/later p.1, plan walls p.2–3, email p.5, notifications p.6; order uncertain. | Send vs receive tiers; own number; scan modes; account/notification controls. | Separate send/receive plans p.2–3, p.9/p.16; ₹499/week send, ₹999/week receive in visible captures. | Unknown; no completed send. |
| Genius Fax | Document selection/scan p.13–15; no delivery. | Five intro/account-choice screens p.1–5, signup p.6, push p.7, credit/number purchase p.8–12. | Page credits, number rental, one credit per page, scan tools. | Credit cards p.9–10 (₹99/1 page, ₹699/10, ₹1,999/50) and separate number rental p.11–12. | Unknown; home says no sent faxes p.8. |
| Fax App (`faxapp`) | One-page prepared document p.8; “ready” p.9, but no send. | No early permission/account prompt visible; receiving wall p.4–5; send wall p.9. | Drafts, receive number, guest vs linked email, readiness state. | ₹199/week receive wall p.4–5 and ready-to-send wall p.9; close affordance not visible. | Unknown; draft state exists p.6. |
| Fax.Plus | File attached p.12–13; no delivery. | Source list p.11; plan/number sequence in pages 2–9, order not verified. | Premium/business/enterprise, page quotas, integrations, porting, teams, API, cover sheets. | Multiple plan sheets p.3–9; visible Premium ₹1,999/month and ₹17,900/year (storefront unverified). | Unknown; no successful send. |
| FaxFree (`faxx`) | Scan is attached p.11–12; no delivery. | Tracking p.2, intro p.3–6, wall p.7; camera ask p.9. | 90+ countries, unlimited tiers, JPG/PDF, draft folders, trial. | Repeated wall p.7, p.13, p.16; ₹999/week, ₹1,199/month, ₹3,999/year. Trial length unknown. | Unknown; one draft shown p.14. |
| iFax | Editable page p.8–9; no delivery. | Paywall/trial p.1–2, number selection p.3, another plan p.4, notifications p.6. | Multiple plan bundles, number selection, urgency fields, custom covers, folders, login providers. | ₹3,499/month after 7 days p.1–2/p.10; ₹1,999/month bundle p.4; ₹999/week native sheet p.11. Mixed offers unresolved. | Unknown; no sent fax shown. |

Across the set, none of the screenshot files proves that a fax was successfully delivered. The strongest visible progress state is a clean, editable, one-page document attached to an addressed fax (Faxer p.6; Fax App p.8; FaxFree p.12). The category’s largest visible friction is committing to a plan, number, credit system, account, or permission before any receipt of delivery has been shown. [OBSERVED]/[INFERRED]

## Our first five minutes

This is a proposal inferred from the recurring screen evidence above, not a claim that competitors support these exact flows.

1. **Start on Compose.** Two fields/actions only: recipient number and “Add document.” Offer Scan, Photos, Files, and share-sheet import in one chooser (Faxer p.4; Fax.Plus p.11; iFax p.8). No account, tracking, notification, or plan ask.
2. **Scan or import.** Detect page edges and show a crop/contrast preview with Save/Retake (FaxFree p.10–11; Tinyfax p.12; Genius Fax p.15). Request camera access only when Scan is selected, with one sentence explaining why.
3. **Review ready-to-send fax.** Show recipient, page count, thumbnail, and cover-page toggle off by default. This copies the evidence-bearing preview state that appears in Faxer p.6 and Fax App p.8. Use “Document ready to send,” not “Fax sent.”
4. **Price and send.** State the exact supported destination and price/free allowance before the final send action. If payment is required, present one plan relevant to the selected task, with total renewal amount, term, and cancel terms in the same view. Keep sending separate from renting a receiving number (Tinyfax p.2–3, p.8–10; Genius Fax p.13).
5. **Receipt and save.** Only after server confirmation show delivery status, timestamp, page count, and a retry/contact-support route. Offer optional account linking to preserve records after the outcome. Competitor captures show empty histories, drafts and status claims but no verified completion, leaving delivery transparency as a plausible gap [INFERRED]; validate with hands-on competitor tests and review mining.

Five minutes is an organizing target, not an observed duration. Static screenshots cannot validate it.

## Differentiators supported by screens

1. **Document-first honest send.** Prepare and inspect the document before subscription/credit choice (Fax App p.7–9 shows a prepared PDF; Genius Fax p.13 exposes zero-credit gating before send; FaxFree p.7 places a plan wall before compose in the capture set). This should reduce commitment before task understanding. [INFERRED]
2. **One visible cost model.** Make page count and sending cost explicit on the send screen. Genius Fax splits page credits (p.9, p.13) and number rental (p.11); iFax shows several different subscription offers (p.1–4, p.10–11). A single task-matched price is easier to compare. [INFERRED]
3. **Verified delivery receipt.** Distinguish “prepared,” “queued,” and “delivered” with a durable receipt. The supplied captures show empty histories, drafts, or marketing promises, but no successful delivery result across any app (Faxer p.3; Genius Fax p.8; Fax App p.6; FaxFree p.14; iFax p.5). This gap is visible in supplied evidence, but whether competitors provide receipts outside these captures is [UNKNOWN].

## Concepts we refuse to add

- **A made-up currency for a one-off send.** Genius Fax requires page credits and separately sells a fax number (p.9–13). Our price should map to actual pages and dollars. [INFERRED]
- **A number rental before a send request.** Number selection belongs to receive/rent-number intent, as the distinct receive flows in Tinyfax (p.8–10), Fax App (p.2, p.4), and Genius Fax (p.11) illustrate. [INFERRED]
- **Business tier taxonomy on the basic path.** Fax.Plus exposes Premium/Business/Enterprise with integrations and team features (p.3–9); keep those behind a business choice. [INFERRED]
- **Social proof, rating prompts, tracking, or notification pressure before delivery.** Faxer overlays a rating ask on compose (p.6), FaxFree opens with tracking (p.2), Tinyfax warns users they may miss updates (p.6). Ask only when the feature’s benefit is clear. [INFERRED]
- **Repeated or ambiguous trial walls.** Faxer’s ₹99 then ₹999/week offer (p.8–9), FaxFree’s repeated walls (p.7, p.13, p.16), and iFax’s different billing offers (p.1–4, p.10–11) argue for one consistent, legible plan per intent. [INFERRED]

## Unknowns and verification plan

- **Static flow vs actual flow:** Conduct hands-on captures for each competitor to establish which screenshots belong to one path, exact asks, tap counts, paywall escape, and whether a free route exists.
- **Delivered outcome:** Send test faxes to a controlled recipient and capture queued/sent/delivered states, failure handling, status timing and receipts. Never infer success from a blue Send button or ready screen.
- **US storefront economics:** Re-capture price sheets in US App Store accounts; amounts are shown in ₹; storefront is not independently verified and US prices are unknown.
- **Trial safety/clarity:** Inspect native subscription sheets for every offer, especially FaxFree “Try it for free!” (p.7/p.13) and iFax multiple products (p.1–4, p.10–11).
- **Repeat behavior:** After a successful send, count the actual taps needed to resend to a prior recipient, duplicate a document, and retrieve a sent fax.
- **Identity and compliance:** Verify who owns screenshots for Fax App, FaxFree, and Fax.Plus package/version/storefront; determine whether HIPAA claims apply to the actual selected plans and supported workflow.

## Verification record

Reviewed all 121 pages visually using contact sheets; enlarged the full-size onboarding, scan, pricing, and purchase screens noted in the per-app files. Rechecked all quoted prices and exact offer copy against source pages before writing. Category-analysis PDFs are treated as unverified commentary and do not support any screen claim. Web/review research intentionally out of scope for this screens-only pass.
