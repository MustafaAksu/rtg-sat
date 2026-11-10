# Addendum 1 (29 Oct 2026) to H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md (de619ee4…, preserved unchanged)

**Correction D-10 (sample counts, §2 "Locality test" and §2 "Evidence").** The script `g333_disc_locality.py` accepts `while got < 80` samples **per N ∈ {8, 10}**, not 60 per N for G(3,3,3) nor 80 per local-class multiset for G(3,1,3). Actual accepted samples: G(3,3,3) 80 + 80 = 160; G(3,1,3) 80 + 80 = 160 (multisets 49/31 at N = 8 and 28/39/12/1 at N = 10, the (0⁴,2⁶) class observed once); **320 in total**, not 120 + 480 = 600. The determinant classes reported are correct for the samples actually taken. Found by ChatGPT (`HCG_DISCRIMINANT_LOCALITY_CHATGPT_REVIEW_v0_1.md` §2); confirmed by Claude from the script text and from ChatGPT's independent recount replayed byte-identically.

**Status change.** The PROPOSED conjecture of §2 (HCG-CONJ-DISC-LOCAL) is superseded by ChatGPT's proof of the local determinant formula, reviewed in `H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` (CHECKED, two AIs). The sampling evidence no longer carries weight.

**W6/W7.** ChatGPT could not replay these two rows (root files absent on its side); `roots_W6.json` (ca4551c2…) and `roots_W7.json` (1b9e96aa…) are forwarded with the review.
