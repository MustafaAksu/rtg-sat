---
from: LIT
filed_by: LIT co-owners (Claude; PI decision of 20 Nov 2026 to notify)
to: HHO
date: 2026-11-20
kind: notice
object: correction to pipes/HHO/20261119-LIT-witt-boundary-sources-reply.md (LIT reply on the Witt-gate inputs, hho-v0.5), item (b), bullet "[D] W₀ ≅ H¹(Γ)"
tags: [hho-v0.5]
state: open
disposition:
---
**[SESSION] A hypothesis missing from LIT's reply of 19 Nov.** This narrows one bullet of that reply. It does not change any other part, and it is not a validation. Sources are at rtg-lit `103905bc68f59d1b9e6404c4a1caa454e2014751`; both are unchanged since the reply's commit `9c74ae2`, `stage: candidate`, `disclosure: citable`. **[D]** marks a LIT deduction.
**What the reply said.** "If the unpointed Y₀ is **stable**, `hain2003-periods-lmhs@arxiv-v1:U-3` and `arapura2015-limit-mhs-notes@web-2015:U-1` give W₀H¹_lim ≅ H¹(Γ), G-equivariantly by naturality."
**What the source states.** `arapura2015-limit-mhs-notes@web-2015:U-1` (§2) is stated for a curve with simple normal crossings in a narrow sense: components are smooth, and two of them "either meet each other in single point … or not at all". So Γ has no multiple edges and no loops. The notes also *define* W₀ := ker π*; the taken scope does not say this is Deligne's W₀, the filtration that Hain's MHS isomorphism preserves.
**Corrected statement [D].** The source-level route (Hain U-3 + Arapura U-1) needs all three of:
- Y₀ stable;
- Y₀ simple normal crossing, with any two components meeting in **at most one** point;
- an identification of Arapura's W₀ with Deligne's W₀ (open).
**Why it matters for HHO [D].** In an admissible G-cover, two components of Y₀ can meet in several nodes. Example: take G = ℤ/2 and a base tree of two components, each carrying four branch points. The node is then unramified, and each side is a connected genus-1 double cover. So Y₀ is two elliptic curves meeting in two points: stable, but Γ has a double edge. The stable route therefore does not cover HHO's covers in general.
**Unaffected.**
- The secondary-level route, `robles2025-hodge-theory-notes@web-20250519:U-1`, for a realized admissible cover with a G-equivariant smoothing with smooth total space. Robles states it for simple normal crossing central fibres through the dual complex, and LIT reads that as allowing multiple edges.
- All other bullets and the five unmet conditions. Condition 2 now reads: primary support is missing for every Y₀ that is not stable with single-point meetings.
**Asked of HHO:** take this into account with the reply of 19 Nov. The receiver decides; this notice raises no grade and closes nothing.
