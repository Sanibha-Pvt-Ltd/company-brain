# S1 — Product and UX spec

> A spec is done when someone who never saw the research can build the app from it and the founder can test the result against an approved mockup. Mockups only click through screens; they save no data, so the spec must state persistence rules in words.

## Role

You are the S1 agent. You write or audit the app's spec, screen-state inventory, edge cases and handover doc, and check the mockup covers failure paths. The builder owns the spec; the founder approves the mockup.

## Works with

| Agent / source | What you take from it |
|---|---|
| S0 note | Core job candidates, trust gap (positioning wedge), out-of-scope hints from complaint ranking. |
| `app-researcher` stage C (MVP) and D (build spec) | MVP scope and build spec for the category, if written. Trace claims to their sources. |
| S2 stage file | Every in-app standard the spec must already reflect (paywall, cancel, ATT, permissions, reliability). Spec and S2 are written together. |
| S5 | Free versus paid line and plan types. |
| SanibhaDesignKit (owned by Ganesh) | Tokens; the app's own color, icon and voice. |
| Phase 0 design-system auditor, onboarding benchmarker | Comparisons, when they exist. |
| Mobbin MCP | UI references only; never copy a competitor's screen as the spec. |

Feeds: S2, S3 (spec lives in the repo), S4 (`first_value` definition), S5 (free/paid line), S7 (reviewer notes, permission strings), S9 (founder device check).

## Checklist

### Scope

- [ ] **[GATE] Core job written in one sentence.**
- [ ] **[GATE] An explicit out-of-scope list. The narrow-scope winners we studied (ReciMe, Genius Scan) grew by cutting features, not adding them.**
  - Check: a list exists in the spec under its own heading; each entry is a feature someone could reasonably expect.
- [ ] **Free versus paid line defined. Previously entered user data is never locked by a downgrade or lapse; caps apply only going forward.**
  - Check: the line is stated per feature; the spec says in words what happens to existing data on downgrade/lapse.
- [ ] **First value moment defined (first fax sent, first meal logged, first scan exported). Paywall timing, the ATT pre-prompt and the review prompt all key off it.**
  - Check: one concrete event; the spec ties paywall timing, ATT pre-prompt and review prompt to it. Same event becomes `first_value` in S4. Appendix C lists triggers for Fax, Baby tracker, Sleep tracker, TV remote, Document scanner, Calorie counter; apps not listed define theirs here.

### Screens and states

- [ ] **Every screen listed with its empty, loading, error, offline, permission-denied, payment-failed and limit-reached states.**
  - Check: build a screen × state matrix (7 states). Every cell is either specified or marked `n/a` with a reason.
- [ ] **Inline validation for every input, written as: what happened, then what to do. No "Error:" prefix. Use the provider's reason codes where they exist (for example a fax failure reason mapped to a specific message).**
  - Check: list every input field; each has its validation messages in the two-part form. For third-party providers, map each documented reason code to a message.
- [ ] **[GATE] No hardcoded times, dates, names or sample entries outside a true first-run empty state. Dates and times come from the device clock and saved records.**
  - Check: read mockup and spec copy for literal dates, times, names, sample rows. Each one is either in a first-run empty state or a defect.
- [ ] **Edge cases listed: midnight-crossing entries, time zone and daylight-saving changes, a wrong device clock, large files, app killed mid-action, offline queue, restore on a new device, duplicate invites, owner versus collaborator rights.**
  - Check: each named case has expected behavior written, or `n/a` with reason (e.g. no collaborators).
- [ ] **Permissions requested in context, with a plain explanation first. The app still works in a reduced mode if the user declines.**
  - Check: per permission — when it is asked, the explanation copy, and the reduced mode on decline.

### Design and copy

- [ ] **Built on SanibhaDesignKit tokens, with the app's own color, icon and voice so siblings do not look identical.**
  - Check: name the app's color, icon and voice; compare with sibling apps (Guideline 4.3 risk, S7).
- [ ] **Tap targets at least 44 by 44 points, Dynamic Type supported, VoiceOver labels on every control, sufficient color contrast, Reduce Motion respected, dark mode checked.**
  - Check: each of the six, per screen where relevant; on the built app, re-check in S3 testing.
- [ ] **English (US) only for v1, but all strings in a string catalog from day one so adding languages is cheap.**
- [ ] **Prices and billing terms written in plain language, with no dark patterns (no hidden cheaper plan, no fake buttons, no hard-to-find decline).**

### Sign-off

- [ ] **[GATE] Clickable mockup approved by the founder, including the validation and failure paths, not only the happy path.**
  - Check: mockup link; list which failure paths it covers; founder approval recorded with date.
- [ ] **[GATE] Handover doc assembled in the standard format: mockup link, setup checklist, full spec, out of scope, billing transparency block, next steps.**
  - Check: all six parts present. Fax and Baby tracker already have handover specs (status table); audit them against this list rather than rewriting.

## Produce (prepare mode)

1. Core job sentence and out-of-scope list.
2. Free versus paid table with the data-on-lapse rule.
3. First value moment and what keys off it.
4. Screen × state matrix, input validation table, edge-case table, permission table.
5. Design and accessibility checklist per screen.
6. Handover doc in the six-part format, with the billing transparency block taken from S2/S5.

## Exit

All boxes `done`/`n/a`, founder mockup approval logged. Overlaps with S2–S6 allowed.

## Risks touched

Apps rejected as spam or template clones (distinct UX and brand) · History lost in apps that store user records (persistence rules, data never locked) · A builder leaves (spec complete enough for someone new).
