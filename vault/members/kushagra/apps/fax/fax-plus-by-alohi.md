---
type: app
category: fax
app: Fax.Plus by Alohi
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:17]
---

# Fax.Plus by Alohi — screens-only teardown

Source: `kushagra screenshots/FAX/screenshots/faxplus by alohi.pdf` (17 pages). Screens show an India country selector and US-number examples. Amounts are displayed in ₹; storefront is not independently verified.

## Screen map

| # | Stage | What user sees | Ask / copy / lever | Friction / evidence |
|---|---|---|---|---|
| 1 | Send Fax | Send screen, To, Add File, Add Page, Send | Add recipient/file | Compose-first; no modal visible. [OBSERVED] |
| 2 | Intro | “Send faxes worldwide, fast and secure”; Continue; example number | Continue | Marketing screen appears after compose in supplied order; exact path unknown. [OBSERVED] |
| 3 | Plans | Annual 23% off / Monthly; Premium, Business, Enterprise tiers and number/page/integration features | Choose plan / Subscribe | Dense capabilities and annual bill framing (e.g. ₹17,900 annual under Premium); more tiers below. [OBSERVED] |
| 4 | Plans | Business / Enterprise cards, high annual prices, integrations and security/compliance | Choose tier | Enterprise framing is irrelevant for single personal fax job. [INFERRED] |
| 5 | Number sheet | Country India, area code; “numbers from India are currently on backorder”; suggests US number; “Send faxes locally in India and internationally using a U.S. number at no extra cost. Reception rates apply as per U.S. rates.” | Choose country/area code or subscribe for US number | Material availability caveat appears in number-selection sheet. [OBSERVED] |
| 6 | Plans | Monthly selected; Premium / Business / Enterprise, ₹1,999 / ₹3,499 / ₹9,000 shown; annual bill details visible | Select tier / subscribe | Multiple business plans and features add choice burden. [OBSERVED] |
| 7 | Plans | Monthly selected; Premium highlighted; Your Number; Subscribe; ₹1,999 billed monthly | Subscribe | Number and price shown together. [OBSERVED] |
| 8 | Plans | Business / Enterprise options and selected number | Subscribe | Enterprise monthly option visible; number below. [OBSERVED] |
| 9 | Plans | Annual selected; Business / Enterprise; ₹17,900 billed annually under selected offer | Subscribe | Annual prepayment and per-month equivalent both shown. [OBSERVED] |
| 10 | Document viewer | Fax.Plus sample PDF viewer, sign/reply/forward/share tools | Use document actions | Sample document shown; not evidence of own fax. [OBSERVED] |
| 11 | Send Fax | Add File / Add Page; source picker Scan, Photos, Files, Google; more sources below | Choose source | Systematic import list; no permission ask shown. [OBSERVED] |
| 12 | Compose | One file attached; 91 KB | Add recipient / send | Document attachment is visible before send. [OBSERVED] |
| 13 | Compose | Same attached file | Send | No recipient or send success shown. [OBSERVED] |
| 14 | Contacts | Empty recents / Add Contact | Add contact | Contact feature, not necessary for one-off send. [OBSERVED] |
| 15 | Settings | My Info, My Fax, Email to Fax, Notifications, Sign-in, Integrations, Language, credit/payment history, free fax pages | Select settings item | Enterprise feature surface is large. [OBSERVED] |
| 16 | My Info | First/last name, phone, regulatory documents | Fill profile | Profile detail request; necessity for first send is unknown. [OBSERVED] |
| 17 | My Info | Same profile fields | Fill or edit details | Duplicate capture. [OBSERVED] |

## Eight lens dimensions

1. **First win:** Attached document appears on compose (p.12–13); no fax sent, delivery status or recipient is shown. First successful outcome and taps are [UNKNOWN].
2. **Ask ledger:** The screenshot set starts on compose (p.1); introduction and plan choices follow in p.2–9, plus number selection and business profile surfaces. This does not establish path order, whether signup is required, or which actions gate a send. No exact ask count is supportable.
3. **Abstractions:** Premium/Business/Enterprise, annual vs monthly, monthly page quota, fax number, porting, switch-off reception, Slack integration, team setup, fax API, cover sheets, regulatory documents and credit (p.3–9, p.15–17). Many concepts are business-tier features outside simple faxing. [INFERRED]
4. **Feel-good:** Importing from Files, Photos, Scan or Google supports document readiness (p.11–13). The main shown emphasis is features/tiers rather than a confirmed delivery moment.
5. **Feel-bad:** India-number backorder is disclosed in number selector (p.5), which is useful but may arrive after plan exploration. Dense tier comparisons add work for an individual sender (p.3–9). No dark pattern is established from the captures.
6. **Paywall:** Several plan-selection captures (p.3–9) with annual/monthly toggle, plan matrix, monthly prices and annual billing. The visible selected premium monthly amount is ₹1,999/month; annual detail ₹17,900/year (p.7); other visible monthly amounts are ₹3,499 and ₹9,000 (p.6, p.8). All amounts are displayed in ₹; storefront is not verified. Close X appears; trial terms not shown.
7. **Repeat cost:** [UNKNOWN]. Contacts and recents exist (p.14), but no successful send or repeat-send state appears. Need hands-on send test to count recipient reuse and document steps.
8. **Feature map:** Table stakes: document import, recipient, send, cover sheet. Differentiators for business segment: team, integrations, number porting, API, regulatory/compliance tools (p.3–5, p.15–16). Bloat for a one-off user: exposure to all business tiers and profile detail before proven first fax. [INFERRED]

## Keep / Kill / Different

- **Keep:** Broad source chooser (p.11), document attached state (p.12–13), upfront number availability caveat (p.5).
- **Kill:** Do not place Business/Enterprise taxonomy and integration matrix in front of an individual who wants one fax (p.3–9). Avoid delaying the India number caveat until after plan comparison (p.5).
- **Different:** Start on compose, ask for recipient and document, then show the exact send/receive price and supported-number availability relevant to that request. Keep team and API plans behind a business path. [INFERRED]

## Verification and unknowns

Reviewed all 17 pages and full-size plan/number screens p.2–9. Confirmed ₹1,999/month Premium, ₹17,900 annual detail, ₹3,499 and ₹9,000 monthly options, and the displayed India-number backorder wording. US pricing, plan gating, completed send, and repeat taps are [UNKNOWN].
