## Change / 变更

Describe the change and its evidence. Link the related recommendation, correction, or dispute.

## Record or policy impact / 记录或制度影响

Explain affected entries, status transitions, frozen rule versions, and any conflict or recusal. If this is an announcement, link public attestations of completed verification and written recipient confirmation.

## Checks / 检查

- [ ] English and Chinese text agree; candidate text does not announce an award.
- [ ] Unconfirmed recipient identities use placeholders in every file and commit; no private contact or payment details are included.
- [ ] Verification artifacts are externally archived with ID, SHA-256, and byte count.
- [ ] Published statements and frozen rules are preserved; replacements and revocations retain history.
- [ ] `python scripts/manage.py validate` and `python scripts/manage.py links` pass.
- [ ] `python scripts/manage.py build` has run and `python scripts/manage.py check` passes.
- [ ] Relevant validator tests pass; any limits or missing policy inputs are explained.

## Reviewer decision / 审查结论

Record substantive review and any required committee confirmation here. A green CI result checks structure; it is not mathematical verification or permission to pay.
