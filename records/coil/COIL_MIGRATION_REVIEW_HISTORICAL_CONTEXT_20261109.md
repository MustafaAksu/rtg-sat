# COIL migration reviews — historical context

**Date:** 2026-11-09. **Author:** ChatGPT, COIL co-owner.
**Status:** SESSION contextual note; not adoption or an active release validation.
**Purpose:** disposition support for item 5 of `pipes/COIL/20261109-SAT-maintenance-advisory.md`. This note supplements, and does not replace or rewrite, the original review record or its pinned scripts.

## Scope

PR #9 preserves historical review evidence. Its original five files at commit `46d5b702ab71879e8cf1a629bbd2163cf9ee9d38` concern the snapshots named in their records and code. They are **not active validators of `coil-v0.3` or successor releases**.

- `check_coil_migration.py` and `COIL_BATCHES_2_4_REVIEW_CHATGPT_20261109.md` preserve the migration checks and findings at the original PR #6/#7/#8 snapshots. The original record's statements about pending corrections and publication describe that review stage, not the present repository state.
- `check_coil_pr10_manifests.py` pins the pre-correction candidate `69a5516cfa9e39ec6477f243b553fb3ace9e061c` and the reference `878958641039364f5e71a6f1c1087080357eff06`. Its nonzero exit records findings in that historical candidate. It is not a failure of the subsequently corrected and adopted release.
- The two read-only workflows are restricted to the historical review branch and their named files. Their existence does not make them current-release CI gates.

## Subsequent disposition

The PR #7/#8 findings were subsequently corrected and accepted in reviews `5823577528` and `5823579799`. PR #10's reference corrections were accepted in review `5824774518`; its content and manifest commits are `3d0306058495121df91e900a6ea9454185402462` and `91c5c4fc961fac806300be85a7d82a2cf89b88ae`.

The later PI adoption and publication are governed by the adopted release records and annotated tags, not by this historical review. The verified `coil-v0.3` tag object is `ce6a77bf3c00c0cac369df0948d54e23dcba5d51`, targeting publication commit `69c98aadf587bab7c93fedb2afb53c9de0b7573d`; the governing record is `records/coil/COIL_v0.3_RELEASE_RECORD.md` at that tag.

The scripts' historical pins and original PASS/finding outcomes remain unchanged. A future active validator needs a separate declared target and validation scope; it must not silently repurpose this evidence.

## Decision boundary

The COIL co-owner recommendation is to retain PR #9 as historical review evidence with this note. This note records neither PI authorization to merge PR #9 nor adoption of COIL v0.4. No frozen source, adopted payload, original review body, script, workflow or existing tag is changed by adding it.
