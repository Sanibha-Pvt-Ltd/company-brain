---
type: app
category: fax
app: Genius Fax
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:18]
---

# Genius Fax — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/fax_genius.pdf` (18 pages). Captures display ₹ amounts; storefront is not independently verified.

## Screen map

| # | Stage | What user sees | Ask / exact copy / lever | Friction / evidence |
|---|---|---|---|---|
| 1 | Onboarding | “No need to go to the Fax Center anymore. Send and receive faxes from wherever you are!” | New user / existing account choice | Explains benefit before form. [OBSERVED] |
| 2 | Onboarding | “With Genius Fax and Genius Scan, you can scan documents to fax them.” | Same choice | Introduces paired product concept. [OBSERVED] |
| 3 | Onboarding | “You can also select your documents from any other app.” | Same choice | Import capability described. [OBSERVED] |
| 4 | Onboarding | “Save money! Genius Fax is cheaper than the copy store. Domestic and international faxes all cost the same.” | Same choice | Savings claim, not quantified here. [OBSERVED] |
| 5 | Onboarding | “Sign up to use Genius Fax. This allows us to update you on the status of your faxes and send you push notifications to confirm success!” | I’m new to Genius Fax / I already have an account | Account is framed as required for use; push tied to delivery status. [OBSERVED] |
| 6 | Signup | Email, confirm email, password (at least 6 characters), Sign up | Create account | Signup appears before any task or prepared fax. [OBSERVED] |
| 7 | Home | iOS notification request over “My Faxes,” no fax number, 0 page credits | Push permission | Copy/title says “Genius Fax Would Like to Send You Notifications.” [OBSERVED] |
| 8 | Empty state | “You have not sent any faxes yet”; 0 page credits, Get Number | New fax / add credits / get number | No first send yet. [OBSERVED] |
| 9 | Credits | 1 page ₹99, 10 pages ₹699, 50 pages ₹1,999; never expire; sending and receiving credits | Choose credit pack | Pay-per-page packs, no subscription term visible on these cards. [OBSERVED] |
| 10 | Credits | Same 10- and 50-page options, 50-page card highlighted | Choose credit pack | No visible trial. [OBSERVED] |
| 11 | Fax number | US/Canada number for 1 month ₹399, 3 months ₹999 (lower option partly cut off) | Choose a number term | Text: expires, no auto-renew; “You have to purchase credits to receive faxes.” [OBSERVED] |
| 12 | Fax number | 3 months ₹999; 6-month option begins below viewport | Choose a term | More number pricing is cut off; do not estimate. [OBSERVED] |
| 13 | New fax | Country India, recipient number, optional cover page, pick document; “Required 0 page credits / You have 0 page credits”; one page costs one credit | Enter recipient / select document; send | Explicit credit requirement appears before sending. [OBSERVED] |
| 14 | Document source | Scan from camera / Photos / Files / Cancel | Choose source | No capture permission prompt shown. [OBSERVED] |
| 15 | Scan editor | Captured paper/document, filters, distortion, recrop, rotate | Adjust and confirm | Editing tools prior to a prepared fax. [OBSERVED] |
| 16 | Settings/help | Help, contact, follow/recommend/rate, about, log out | Optional support/rating actions | Product asks for rating in settings, not over compose. [OBSERVED] |
| 17 | Settings/help | Same list, help and feedback copy | Optional action | Duplicate/overlapping settings capture; no new core step. [OBSERVED] |
| 18 | Account settings | Name, fax number “Get Number,” change email, delete account | Set identity or number | Sender details can be completed after signup. [OBSERVED] |

## Eight lens dimensions

1. **First win:** Onboarding explains remote sending/receiving and scan/import (p.1–4); first tangible task appears at new fax/document selection (p.13–15). No sent confirmation appears. Delivered first fax, taps, and paywall ordering vs success are [UNKNOWN].
2. **Ask ledger:** repeated new/existing-account choice across five intro screens (p.1–5); signup email/confirm/password (p.6); push permission (p.7); credits/number purchase shown at empty home (p.8–12); recipient/document choice (p.13–15). Exact taps and mandatory status beyond p.5 copy are not verified.
3. **Abstractions:** Page credits and exchange rate (one fax page = one credit), separate number rental, US/Canada number, scan modes, optional cover page (p.9–15). Credits are an extra unit users must understand; page-based billing already maps to document length. [INFERRED]
4. **Feel-good:** Scan filters/recrop/rotate (p.15) give control. “Confirm success” push proposition (p.5) can reassure, but the app asks permission early. No delivered success is shown.
5. **Feel-bad:** Account required statement and full account form precede task evidence (p.5–6). User is at zero credits and must understand separate credit packs and number terms (p.8–13). No trial is apparent in the observed credit/number cards.
6. **Paywall:** Pay-as-you-go credit sheet (p.9–10) and separate number rental (p.11–12), shown before any sent-fax evidence in the supplied set. Displayed amounts are in ₹; storefront is not independently verified;  lower number option is cut off. Not a conventional subscription wall on the visible cards.
7. **Repeat cost:** [UNKNOWN]. Home has Add Credits / Get Number (p.8); no completed send or second-send screenshot. Determine whether recipient/doc details persist on return.
8. **Feature map:** Table stakes: recipient, scan/import, cover, credits/send, fax-number support. Differentiator candidate: non-expiring page packs and explicit page cost (p.9, p.13). Bloat/cost: mandatory-looking signup and the mental credit currency plus a separate number currency (p.5–6, p.9–12). [INFERRED]

## Keep / Kill / Different

- **Keep:** Per-page cost and “Never expires” are legible terms (p.9); show page credits required beside the send action (p.13); scan tools offer practical correction (p.15).
- **Kill:** Signup before the user can prepare a fax (p.5–6), and any needless credit abstraction that hides actual dollars per page. Avoid requesting push permission before the user has a fax whose delivery they want to track (p.7).
- **Different:** Let users prepare a fax as guest, then quote a single price in dollars based on page count and explain whether receiving needs a number. Offer account creation after a successful or saved draft. [INFERRED]

## Verification and unknowns

Checked all 18 pages, plus full-size p.5–6, p.9–11, p.13–15. Confirmed visible ₹99/₹699/₹1,999 page-credit packs, ₹399/₹999 number terms, and “You have to purchase credits to receive faxes.” The 6-month number price is partly clipped and left unreported. US prices, account bypass, first delivery, and repeat taps are [UNKNOWN].
