# Formal verification: evidence and review

Public verification records connect the original mathematical problem, formal statement, pinned proof source, reproduction evidence, and review conclusions. A formal statement alone is not a verified proof, and proof checking must also address whether the statement represents the intended problem.

Review the mathematical solution and register its solver candidate first. Only
then may Lean verification and Lean candidate registration proceed. A Lean
submission identifies the accepted mathematical solution, review evidence and
prior solver candidate record (or its subsequent award record). If a PR supplies
both contributions, maintain this order. Separate records and claims do not remove
the prerequisite of an existing solver registration.

Repository CI validates record structure and references. It does not run proof repositories, establish mathematical truth, decide awards, or authorize payments. A source link or successful build alone is not a completed verification record.

See the [record guide](records.md) for public evidence fields. Publish only evidence authorized for public release.

## Required Lean pre-submission check

Before opening a PR that submits a Lean proof, the contributor must run the
repository's [`lean-verify` skill](../skills/lean-verify/SKILL.md) on the exact
proof commit and obtain an overall **Verification passed (`验证通过`)** result.
This applies to initial submissions, replacement proofs and combined solver/Lean
submissions. Solver-only submissions and attribution-only corrections that
introduce no proof version do not require this check.

This is a contributor pre-submission self-check. Its declaration, report and logs
are submitter-provided evidence, not independent certification. Maintainers must
independently check statement correspondence and reproduce verification before
acceptance, following mathematical review and solver candidate registration as
described above. Passing this check does not approve attribution, priority, a
merge or an award.

### Run the skill before a PR exists

The complete skill is versioned under `skills/lean-verify/`, including its
references, target-manifest example, audit script and regression tests. Give your
coding agent the skill file and request the full workflow. If your agent supports
installed skills, copy the complete `lean-verify` directory into its skill
directory and invoke `$lean-verify`. Reading the instructions or running only
`scripts/audit.py` is not a completed verification.

Supply the JSP problem ID, catalog entry and original mathematical source,
plus the proof repository, branch, full 40-character commit SHA, project path and
target theorem names. A PR URL is not required for this direct-source check.
For example, replace the bracketed values in this request:

```text
Use the skill at skills/lean-verify/SKILL.md to perform a full pre-submission
verification of JSP-[number], catalog entry [path/link], against the original
problem at [source and exact location].
Proof repository: [URL]
Branch: [branch]
Commit: [full 40-character SHA]
Lean project and target theorem(s): [paths and fully qualified names]
No PR has been opened yet. Verify this exact commit, all original problem
requirements, the clean build and the proof's transitive axiom dependencies.
Write the report in English for public submission, with the final verdict,
actual verification levels, trust dependencies and supporting evidence paths.
```

The workflow checks statement correspondence and full coverage as well as actual
Lean execution. It must retain the pinned toolchain and dependencies, use an
isolated environment, and report any missing proof steps or extra assumptions.
Follow its instructions for kernel replay and independent checks, recording the
levels actually completed and any limitations. Preserve the full report and
underlying evidence locally for follow-up review. Publishing links to those
materials is recommended, not a prerequisite for opening the PR.

### Attach the result to the PR

Confirm the completed self-check in the PR checklist and complete the template's
**Pre-submission Lean verification** section with these required details:

- The exact proof repository and commit, matching the proof submission.
- The verification date and overall **Verification passed** conclusion.
- A short result summary for every submitted problem and proof version, including
  statement correspondence, full coverage, actual Lean checks, verification
  levels, trust dependencies and any limitations.

Recommended supporting material is optional: identify the awards repository
commit containing the skill used, and link the full report, target manifest,
build/axiom logs and any checker evidence. A short report may instead be pasted
directly into the PR body. A bare local filesystem path is not a public link.

To share longer evidence, first verify proof commit **A**, then save the report
and logs under `verification/` in your own proof repository in a later commit
**B**. Link the files at **B** and state clearly that they describe proof commit
**A**. Adding evidence does not require rechecking **A** if it remains the selected
proof version; selecting **B** or another proof commit does require a new check.

All submitted problems and proof versions must pass. Conditional pass, partial
coverage, failed or incomplete verification does not meet this pre-submission
requirement. Resolve the outstanding items and rerun the full workflow before
submitting. Rerun verification whenever the selected proof commit changes; an
older report cannot certify a newer commit.

The audit helper's exit code 0 means only that its listed mechanical checks
succeeded with the observed standard axioms. It does not establish original
problem correspondence or a complete solution. Repository CI likewise does not
certify the report or run the external proof. Maintainers independently examine
the original problem and proof and reproduce the checks; a checkbox, summary or
report alone cannot establish acceptance. They may request supporting logs when
resolving a verification issue.

Publish only authorized evidence, with private information and credentials
removed. When sharing full reports, logs or proof artifacts, use the external
proof repository or a stable public evidence archive and link them from the PR.
Short reports may stay in the PR body. Keep Lean proof
source, dependencies and build artifacts out of this repository. The bundled
skill and its synthetic regression fixtures are verification tooling maintained
by this repository, not submitted problem solutions.
