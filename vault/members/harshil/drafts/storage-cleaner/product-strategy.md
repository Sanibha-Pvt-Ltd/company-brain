---
type: category-product-strategy
category: storage-cleaner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:52 across 6 apps, knowledge base, Apple docs]
---

# Storage Cleaner — final recommendations (v1)

Reasoning and evidence: [[members/harshil/drafts/storage-cleaner/product-strategy-evidence]]. Built on [[research/categories/storage-cleaner/context]].

## Positioning

- **Line:** Make space. Keep what matters.
- **Hook:** See what's really filling your iPhone.
- **Promise:** Real numbers. Biggest wins first. Nothing deleted without your OK.
- **For:** iPhone owners who just hit "storage full" and are afraid of deleting the wrong photo or getting charged.
- **Name:** KeepSpace (placeholder until cleared).
- **App Store screenshots 1–3:** Measure → Choose → Done.
  1. Real storage bar + "Your biggest videos"
  2. A similar-photo group with the reason for the suggestion
  3. Review tray + "moved to Recently Deleted" result
- **Store numbers:** taken from a real demo phone and labelled as such.
- **Ads:** storage-full (control), deletion-anxiety (differentiator), "one iPhone, six cleaners" truth test (challenger).
- **Never claim:** "% full" we didn't measure, "free up to N%", speed/boost/junk/cache cleaning, iCloud cleaning, "freed" at delete time, user counts or ratings.

## UI/UX

**Principles**
1. Every number is measured, or marked "≈".
2. Give before you ask: no permission or payment before the user sees something real.
3. Biggest win first.
4. Every suggestion shows a one-line reason; the user decides.
5. Say when the space comes back.
6. Max four categories on home, one idea per screen.
7. Calm, not alarm: red only on the Delete button.

**Structure**
- Two tabs: **Clean** (home) and **History**. Settings behind a gear.
- Home: true storage line, then Videos, Similar, Screenshots & utility, Duplicates, ordered by GB.
- Review tray as a persistent bottom bar.

**First five minutes**
1. Welcome: device's real used/free storage → "Scan my photos"
2. Pre-prompt: "Analysed on this iPhone · nothing uploaded · nothing deleted without your OK"
3. iOS Photos permission
4. Progressive scan, videos appear first
5. Home, categories by GB
6. Large videos: size, duration, tap to play
7. Review tray → "Moves to Recently Deleted for 30 days" → Delete
8. **Result (first win, 7 taps):** "X GB moved to Recently Deleted" + how to empty it now
9. Soft paywall

**Permissions**
- Photos: after our pre-prompt; limited access handled with a banner; denied still shows true storage.
- Notifications: opt-in toggle on the result screen only.
- No tracking (ATT) prompt at launch.

**Paywall**
- Soft, after the first cleanup and when the free daily allowance runs out.
- Close (X) visible immediately.
- Plans to test: annual + monthly vs annual + lifetime. No weekly at launch.
- Dated charge timeline for any trial; no "trial enabled!" screen; no pre-selected plan tricks.
- Free keeps: full scan, all sizes, all previews, deletes up to a daily allowance, History.

**Visual & voice**
- Light-led, calm, one accent colour, neutral bars; real photos large; no decorative "AI" art.
- Plain, specific copy: "Nothing is deleted until you tap Delete." · "These look alike. We suggest keeping the sharpest one. You decide."
- Dynamic Type, VoiceOver on every thumbnail and group, AA contrast, Reduced Motion.

## v1 product features

| # | Feature | Free / paid |
|---|---|---|
| 1 | True storage overview | Free |
| 2 | On-device, progressive, resumable scan | Free |
| 3 | Large videos by size + full preview | Free view; delete within allowance |
| 4 | Similar photos: compare + reason, user picks | Within allowance |
| 5 | Exact duplicates | Within allowance |
| 6 | Screenshots & utility images by age | Within allowance |
| 7 | Protected favourites (never auto-selected) | Free |
| 8 | Review tray + one batched delete | Free |
| 9 | Honest result + Recently Deleted guide + History | Free |
| 10 | Video compression, one preset (first cut if late) | Paid |
| 11 | "New since last clean" + optional weekly reminder | Reminder free; weekly bulk paid |
| 12 | StoreKit 2 paywall + free daily allowance | — |

**Paid unlocks:** unlimited cleanup, video compression, weekly review.

**Later (v1.1+):** swipe mode, widget, screenshot topics, Live Photo → still, contacts merge, weekly plan (only if payback fails).

**Not building:** email cleaning, contacts/calendar, vault, iCloud cleaning, boost/speed/junk/cache, "AI categories", health score.

## New recommendations

1. "One iPhone, six cleaners" truth test as launch PR and challenger ad.
2. Lead with videos, not duplicates, everywhere: onboarding, home, store shot 1.
3. Recently Deleted as the day-2 return reason.
4. Week-1 on-device spike on file-size measurement (exact sizes need iOS 27; older iOS gets "≈").
5. "How we measured" sheet behind every number.
6. Launch without the tracking prompt.

## Before build

- Ganesh captures competitors' permission, scan, delete and result screens, plus US paywalls.
- Run brand-designer, ux-designer and s1-spec on this note.
