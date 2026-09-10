# 记录维护指南

[English](../records.md) · [首页](../../README.zh.md)

目录和字段依据项目负责人提供的《孙宇晨奖-GitHub仓库框架-修订版》（2026-08-27 修订）建立。该框架不替代完整的评级、归属和核验制度。尚未提供 12 项正式候选、3 项观察候选及完整 v0.8 制度，因此真实记录目录保持为空。

## 目录与生命周期

```text
awards/<YYYY-MM>/batch.yaml
awards/<YYYY-MM>/<award-id>/
candidates/verified-pending/<entry-id>/
candidates/observation/<entry-id>/
    award.yaml
    citation.md
    recipients.md
    verification/record.yaml
    verification/statement.yaml        # 主张形式化通道时必填
    verification/statements/<id>.yaml  # 仅在保留作废陈述时增加
```

上面的条目文件结构适用于三个位置。稳定 ID 只能出现一次。`observation` 和 `verified-pending` 是候选池目录名，不是状态枚举；后者表示进入核验，不表示核验通过。等待获奖人书面确认的条目仍留在候选池。

| 位置 | 状态 |
| --- | --- |
| 观察候选 | `draft`、`under-verification`、`pending-recipient-confirmation` |
| 正式候选 | `under-verification`、`pending-recipient-confirmation` |
| 已确认授奖 | `announced`、`disputed`、`paid`、`revoked` |

仅在真实成果完成核验、获奖人书面确认并公示后创建授奖批次。撤销时在原批次保留记录，追加含理由、证据及核验失效点的 `revocation`，原评分、获奖归属和核验证据保持不变。现行制度下不设置未解决题目的挂榜或定价目录。

## 源文件

| 文件 | 用途 |
| --- | --- |
| `award.yaml` | 题目、冻结规则、四维评分、等级与上调、受奖组、拨付金额、贡献、核验引用、冲突、状态及撤销。 |
| `citation.md` | 中英文授奖理由，或明确标为候选的审查说明。 |
| `recipients.md` | 中英文归属；确认前使用占位符。 |
| `verification/record.yaml` | 固定源码、工具链及库、公理审计、陈述比对、独立检查器、环境、隔离、归属和外部归档指针。证据尚未形成时可为 `null`，但不能据此取得形式化评分。 |
| `verification/statement.yaml` | 版本化钦定陈述、定义审查、冻结数学库、集体署名、事后撰写流程及形式化 B4 资格。 |

两份 Markdown 均须具有非空 `## English` 和 `## 中文` 段落。[模板目录](../templates/)包含示例；高级模板中的尖括号占位符有意不通过校验。草稿模板须替换为真实已解决题目，不能把合成示例发布为真实候选。

[授奖 Schema](../../data/schema/award.schema.json)、[核验 Schema](../../data/schema/verification-record.schema.json)及[陈述 Schema](../../data/schema/statement.schema.json)定义准确字段结构。对象拒绝未知字段；YAML 别名、重复键、错放的 YAML 和记录符号链接会被拒绝。

## 框架中需显式表示的细节

- `verification.formal.counts_for_c` 表示是否将形式化计为 C 维通道，使框架判定式可被程序读取。
- 获奖人 `confirmation`、人员档案 `publication_consent` 和团队组 `written_confirmation` 仅链接经授权的**公开确认说明**。私人签署文件、邮箱、地址、支付资料及未经确认的姓名不得进入仓库或 Git 历史。
- 候选阶段主张形式化通道即须有陈述。`post_hoc.b4_eligible: false` 关闭的是 B4 的**形式化路径**及 C 通道，不妨碍通过 `journal` 或 `best-paper` 获得 B=4。
- 已公布陈述不得原地改写。旧内容保存在 `verification/statements/<旧-id>.yaml`，状态改为 `superseded`；`statement.yaml` 使用新的 active ID，并以 `supersedes` 关联旧版本。
- 对事后采用第三方陈述，暂按框架口径豁免双人撰写要求，仍须来源与公示信息；此解释仍待制度侧确认。
- 集体署名表示为至少两个不同 curator ID。CI 检查 ID 与档案；独立性、权限、确认真实性、检查器是否当前版本、最低安全版本及数学陈述等价性仍需实质审查。

## 冻结的评级制度

`docs/grading.md` 带 `version: v0.8` front matter，但明确是占位页。[grading-rules.yaml](../grading-rules.yaml)有意不填完整分数映射和金额表。在制度负责人补齐前，非零评分条目校验失败；不得根据框架中的示例授奖推导制度。

导入制度时，把配套表设为 `status: active`，以长度为 12 的 `score_to_level` 列表依次定义 1–12 分等级，以 `amounts_usd` 定义四档金额，并保持 `[JSP-4, JSP-3, JSP-2, JSP-1]` 的从低到高顺序。对照 §3.2 和 §2.1 审核后，将正文与配套表同时提交。

进入 `under-verification` 时记录 `rules.version`、`rules.document_commit` 和业务事件日期 `rules.frozen_at`。校验器从准确 Git 提交读取制度及配套表并核对版本。后续变更不得静默改写冻结规则；撤销或重评须走另行审查的制度流程，不设置逐条目安全例外开关。

## 本地命令与 CI

需要 Python 3.10 或更高版本：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/manage.py validate
python scripts/manage.py links
python scripts/manage.py build
python scripts/manage.py check
python -m unittest discover -s tests -v
```

`validate` 检查源数据 Schema 和跨文件业务约束；`links` 检查本地 Markdown 文件链接、引用式链接、图片和标题锚点，不检查外部 URL 可达性或原始 HTML 链接；`build` 校验后确定性生成 `data/*.json`；`check` 在不修改文件的情况下比较已提交汇总与重新生成结果。汇总不包含时间戳或本机路径。

`python scripts/manage.py history --base <完整提交哈希>` 比较冻结规则、已公布陈述和授奖历史。CI 对有基准提交的 PR 和 push 运行此检查，并拉取完整历史。此检查比较快照，审查者仍须检查中间提交是否泄露私人信息，以及业务事件日期是否真实。

三个工作流分别验证记录与链接、生成可下载的数据产物、检查已提交汇总一致性。工作流仅有仓库读取权限，不自动推送生成提交。源文件与 JSON 在同一 PR 提交。CI 不执行证明仓库、不认证数学结论、不处理支付。大日志和形式化产物放在外部永久归档，仓库仅存归档标识、SHA-256 和字节数。

仓库文件无法直接落实的 GitHub 设置见[平台配置](platform-setup.md)。
