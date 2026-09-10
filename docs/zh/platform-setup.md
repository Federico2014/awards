# GitHub 平台配置

[English](../platform-setup.md)

本页按修订版框架整理交接事项。此次初始化**尚未执行**这些平台设置。当前检出仓库属于 `Federico2014/awards`；创建组织、迁移仓库、更改可见性、邀请 owner 和启用 Pages 都是单独的平台操作。

- 目标组织：`JustinSunPrize`；显示名：`Justin Sun Prize · 孙宇晨奖`；仓库：公开 `awards`；默认分支：`main`。
- 录入授奖前确认至少两位组织 owner，使用组织公共邮箱和准确法律实体。提交前确认适合永久公开的 Git 身份及 GitHub noreply 邮箱。
- 按框架开启 Issues、Discussions，关闭 Projects、Wiki；开启 Discussions 后置顶[入口说明](discussions-notice.md)。
- 保护 `main`：所有变更走 PR，至少一人批准；必需检查为 `Schema validation`、`Markdown links`、`Data consistency`；禁止强推及分支删除，规则适用于管理员且不允许绕过。先运行工作流，再在 GitHub 选择对应检查名。
- 有渲染器后单独配置 Pages。此次只准备正文与数据，没有网站构建或部署。框架中的组织名和临时域名拼写不一致，应在组织名称最终确定后确认实际 Pages 地址。
- 支付不在信息公示站点或仓库处理。大产物外部归档，保留永久标识与校验和。

仍需补齐完整评级制度、候选来源记录、公众提交常设责任人、保密行为举报渠道、owner 名单及自定义域名。框架暂将公众提交处理交由策展委员会。此次按框架建议采用 MIT（代码）及 CC BY 4.0（内容与数据）；第三方材料保留原许可。
