# Public roles / 公开职务档案

Store profiles as `<person-id>.yaml` under `recipients/`, `curators/`, or `verifiers/`. One person may have multiple role profiles with the same stable ID and display name. These directories start empty.

档案按角色存放为 `<person-id>.yaml`；同一人可用相同稳定 ID 和显示名称具有多个角色档案。当前目录为空。

Profiles contain a confirmed public display name, professional affiliation, role, public professional links, consent attestation and curator recusals. Recipient profiles require a public written-confirmation attestation before a name is recorded. Each recusal links an entry ID, date, a brief public explanation, and an optional public discussion URL. Do not include private contact, payment, or identity details. Record no recusals as an explicit empty list.

档案仅记录已确认公开名称、机构职务、公开职业链接、确认说明及 curator 的回避记录。获奖人姓名入库前须有书面确认的公开说明。回避须关联条目 ID、日期、简短公开说明及可选公开讨论链接；没有回避时明确写空列表。不得记录私人联系方式、支付或身份材料。

See the [person template](../docs/templates/person.yaml.example) and [schema](../data/schema/person.schema.json).
