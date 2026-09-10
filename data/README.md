# Machine-readable data / 机器可读数据

[awards.json](awards.json) and [candidates.json](candidates.json) are generated from source records. Both use `{ "schema_version": 1, "items": [] }` when no records exist. Each item includes the source entry, repository-relative path, bilingual Markdown, verification record and active statement. Records are sorted by stable entry ID.

两份 JSON 从源记录生成，当前 `items` 均为空。每项包含结构化条目、仓库相对路径、中英文 Markdown、核验记录和当前陈述，并按稳定 ID 排序。候选数据不代表授奖。

Run `python scripts/manage.py build` after source changes and commit both outputs in the same PR. Do not edit the generated JSON directly. `python scripts/manage.py check` detects drift. Schema IDs use the reserved `example.invalid` domain as local identifiers and are resolved from [schema/](schema/); they are not remote schema services.

修改源记录后生成并同步提交汇总，不直接编辑 JSON。Schema 使用保留域名作为本地标识，由仓库内文件解析，不依赖远程 Schema 服务。

See [record maintenance](../docs/records.md) / [记录维护](../docs/zh/records.md) for fields and validation boundaries. A future website should render these files and `docs/`; no website or Pages deployment is included in this initialization.
