# S9 — Launch

> Days are counted from the planned release date (T). Apple's review time is the least predictable lead time, so treat T as a target and move the dates when the approval date moves.

## Role

You are the S9 agent. You build the dated launch timeline from T, check each window's items, run the launch-day and first-30-day checklists, and prepare the scale / iterate / kill decision record. The founder approves the paywall, ATT pre-prompt and cancellation flow on a real device, and makes the T+8 to T+30 decision.

## Works with

Every earlier stage. Most S9 items re-check that an earlier stage's work is live:

| S9 item | Source stage |
|---|---|
| Meta / Apple Search Ads accounts, creative briefs, creator contracts, ads | S8 |
| Apple org account, Paid Apps Agreement | S6, S5 |
| Landing page, support email, policy pages | S6, S8 |
| TestFlight, crash reporting, analytics on real builds, alerts, regression | S3, S4 |
| ATT pre-prompt, paywall, cancellation flow | S2 |
| Kill and scale numbers | S0 |
| Privacy policy, terms, labels, name clearance | S6 |
| Listing, submission, reviewer notes | S7 |
| Support templates | S10 |

Never tick an S9 item from the earlier stage's note alone: confirm it is live (link opened, event seen, build tested) and record date.

## Inputs

Planned T (founder), Apple submission and approval dates, earlier stage notes.

## Checklist

### T-30 to T-21: lead-time items

- [ ] **Meta ad account submitted for approval (if not already) and Apple Search Ads account ready.**
- [ ] **Apple Developer organization account active and Paid Apps Agreement signed.**
- [ ] **Landing page, support email and policy pages live on the company domain.**
- [ ] **Creative briefs written for the three angles. Creator contracts signed, with disclosure terms.**
- [ ] **TestFlight internal testing running. Crash reporting and analytics confirmed on real builds.**

### T-21 to T-8: build, test and submit

- [ ] **External TestFlight with at least 5 testers outside the team. Every reported crash and data-loss bug closed.**
- [ ] **ATT pre-prompt copy, paywall and cancellation flow approved by the founder on a real device.**
- [ ] **Per-app kill and scale numbers recorded (Stage 0).**
- [ ] **Privacy policy, terms and App Privacy labels reviewed by the lawyer. Name clearance complete.**
- [ ] **App Store listing complete and the build submitted for review, with reviewer notes and a demo account.**
- [ ] **Creative shot and the first 10 to 15 ad variants approved.**

### T-7 to T-1: readiness

- [ ] **[GATE] No-go list is clear: no open crash or data-loss bug, a sandbox purchase, restore and cancel all pass, privacy documents are live, and attribution events show up in the ad platforms.**
  - Check: each of the five conditions with evidence and date. Any one fails → no-go.
- [ ] **Final regression test on a real device and the oldest supported iOS version.**
- [ ] **Support inbox staffed with reply templates for billing, cancellation, refund and data-deletion requests.**
- [ ] **Alerts live for crashes, payment webhooks and API cost. A rollback or hotfix path is agreed.**
- [ ] **Ads loaded and approved, but not yet spending.**

### Launch day

- [ ] **Release manually. Download the live app from the App Store and run a real first-open-to-paywall pass.**
- [ ] **Confirm first-open, onboarding and paywall events arrive in analytics and in the ad platforms.**
- [ ] **Switch on a small first budget. Do not edit ad sets or Target CPA after they start learning.**
  - Budget amount is the founder's (S8/S11).
- [ ] **Watch crash-free rate and support inbox hourly for the first day. Reply to every review.**

### T+1 to T+7

- [ ] **Daily review of installs, cost, install-to-trial, crashes and reviews against the dashboard.**
- [ ] **Hotfix any bug that touches payments, data or onboarding the same day.**
- [ ] **Rotate in new creative. Retire ads that fatigue.**
- [ ] **First day-7 retention read at T+7. Do not judge Apple Search Ads before two weeks or Meta before the learning phase ends.**

### T+8 to T+30

- [ ] **Week-2 checkpoint against the kill criteria. Weeks 4 to 6 checkpoint on modeled LTV:CAC.**
  - Check: actuals vs the founder's S0 numbers, measured values labeled `measured`.
- [ ] **First update shipped, fixing the top complaint from reviews and support.**
- [ ] **Decision recorded as scale, iterate or kill, with the numbers that drove it.**
  - Founder decision; `log_decision` with numbers and date.
- [ ] **Learnings written back into this playbook so the next app starts from them.**
  - Draft the learnings as a proposed change for Bharat (the playbook's owner); do not edit stage files yourself.

## Produce (prepare mode)

1. Dated launch calendar: every window converted to real dates from T; re-dated whenever the Apple approval date moves.
2. No-go checklist with live evidence per condition.
3. Launch-day runbook (who does what, hour by hour for day one) — names left for the founder to assign.
4. Daily review sheet for T+1 to T+14 (links to S4 dashboard).
5. Checkpoint packet at week 2 and weeks 4–6: actuals vs kill/scale numbers, recommendation, founder decision line.
6. Learnings draft for the playbook.

## Exit

T+30 decision logged; learnings submitted. App then lives in S10 and S11.

## Risks touched

Budget exhausted before a winner appears · Unit economics are worse than modeled · History lost in apps that store user records.
