---
type: reference
updated: 2026-10-03
---

# Tech context

**Fixed**
- iOS apps only, for the US App Store.
- Small team; target ~6 weeks from final MVP to a first build.

**Engineering defaults (proposed, not yet ratified — confirm in [[company/open-questions]])**
- SwiftUI, StoreKit 2 for subscriptions, recent iOS minimum.
- Prefer on-device processing where the product allows (privacy, no server cost).
- Paywall/analytics/attribution SDK choices come from the build spec, informed by what competitors run.
- App Store review compliance (subscription disclosures, permission strings, privacy nutrition labels) is part of every spec's launch checklist.

**Tooling in use**
- Claude (claude.ai Pro for each member; Claude Code for Harshil).
- Mobbin MCP for UI references (design agents).
- Brain MCP on Cloudflare Workers + D1; vault in GitHub.
