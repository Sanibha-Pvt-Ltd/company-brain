# Stage D — Build spec

Run only when `mvp.md` has `status: final` (team reviewed, Bharat signed off, decision logged). If not final, stop and say so.

Output: `research/categories/<cat>/build-spec.md` and `products/<app-name>.md` (links to mvp, market, spec; status, owner, next step).

Turn the MVP into a hand-off for designers and iOS engineers:

1. **Screen inventory** — per screen: purpose, components, states (empty/loading/error/success), draft copy (use 5★ review language, honor the trust pledges).
2. **User stories** with acceptance criteria, ordered by build priority; mark what must ship in the first 2 weeks.
3. **iOS technical notes** — frameworks (SwiftUI, StoreKit 2, PhotoKit/etc. as relevant), permissions + Info.plist usage strings, on-device vs cloud data, minimum iOS version, third-party SDKs (paywall, analytics, attribution) and why, versus competitor stacks.
4. **StoreKit products** — ids, durations, trials, intro offers; paywall variants to A/B test.
5. **Analytics** — events and funnel that prove each differentiator works.
6. **Launch** — App Store review risks, privacy nutrition label, ASO asset brief, first ad-creative brief.
7. **Open decisions** for the design and iOS owners.
