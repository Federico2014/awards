# GitHub platform setup

[中文](zh/platform-setup.md)

This is a setup handoff based on the supplied framework. These settings have **not** been applied by this repository initialization. The current checkout belongs to `Federico2014/awards`; creating an organization, transferring it, changing visibility, inviting owners, and enabling Pages are separate platform actions.

- Intended organization: `JustinSunPrize`; display name: `Justin Sun Prize · 孙宇晨奖`; repository: public `awards`; default branch: `main`.
- Confirm at least two organization owners before recording awards. Use an organizational public email and the correct legal entity. Confirm public commit identity and a suitable GitHub noreply address before committing.
- Enable Issues and Discussions; disable Projects and Wiki if following the framework. Pin the [Discussions notice](discussions-notice.md) when Discussions is enabled.
- Protect `main`: require PRs and at least one approval, require `Schema validation`, `Markdown links`, and `Data consistency`, block force pushes and branch deletion, and apply the rules without administrator bypass. Run the workflows first so these check names are available in GitHub.
- Configure Pages separately when a renderer exists. This initialization provides content and data but no website build or deployment. Confirm the organization's actual Pages URL after its final name is chosen; the two organization/domain spellings in the supplied framework differ.
- Keep payments outside the information site and repository. Store large artifacts externally with permanent IDs and checksums.

The full grading policy, candidate source records, permanent public-submission responsibility, confidential conduct reporting contact, owner list and custom domain remain setup inputs. For now, the framework assigns public submission handling to the curatorial committee. Code uses MIT and content/data use CC BY 4.0 in this initial implementation, following the framework's recommendations; third-party material retains its original license.
