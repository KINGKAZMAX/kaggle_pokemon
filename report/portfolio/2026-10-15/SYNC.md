# 2026-10-15 归档与同步说明

外盘迁移、GitHub 公开展示包与 Figma 云端写入已完成。

[Figma：PTCG 比赛复盘与卡牌战术](https://www.figma.com/design/UpPXmCgS3JXRhhwksWq8xq?node-id=2-2) 位于「設計比賽規劃」团队。8 页包括总览、时间线、Agent/战术和全部卡组；111 组各 60 张，合计 6,660 个可编辑卡槽，逐张名称与顺序核对通过。页面元数据见 [figma_manifest.json](figma_manifest.json)。

| 位置 | 保存什么 | 完成依据 |
|---|---|---|
| 外盘 | 源目录、受限大数据/原生引擎/原提交包、manifest与hash、未公开模型 | 文件数量/大小/hash验证与迁移报告 |
| GitHub现有仓库 | 本人可再分发代码、脱敏聚合、卡组展示、历史复盘和来源 | 实际推送commit与在线读取；禁止用本地文件存在代替上传成功 |
| Figma | 时间线、Agent架构、角色协作、部署修复、负结果与证据卡 | 已创建并检查 8 页，逐张名称、顺序、数量均一致 |

公开展示入口为[index.html](index.html)，结构化数据为[decks.json](decks.json)，过程为[HISTORY](HISTORY.md)。此次文档整理不重跑比赛、训练、自动提交或旧never-stop循环；既有仓库历史也不由新的Mac导入覆盖。

## 发布边界

GitHub不是完整工作盘备份。原生engine、完整官方卡表、原始replays、账号凭据、venv/cache、来源许可未核验的第三方代码/模型、含官方runtime的tar包留在受限存档，按真实许可另行处置。`src`中的catalog切片和tests fixture也需逐文件审核，不能凭扩展名断定可公开。

GitHub通常会警告超过50MiB的普通Git文件并阻止超过100MiB文件；LFS解决传输/存储方式，不解决数据再分发许可。规则与限额以[GitHub官方大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)为准。比赛数据、代码分享、Pokémon素材及Strategy提交要求以[Kaggle官方Strategy Rules](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle-challenge-strategy/rules)为准；本次抓取该规则页没有取得可读正文，因此不声称重新核验了全部实时条款。

## 公开项目参考：学习呈现方法，不移植成绩

- [Lawliet-ai/ptcg-ai-battle-agent](https://github.com/Lawliet-ai/ptcg-ai-battle-agent)：参考架构与measurement tools并列、失败实验可追溯、明确排除官方引擎/卡表/replay的展示方法。其搜索结论只属于其项目，不套用到本项目，也不把p值未显著说成证明两模型等效。
- [henriquetakahiroito/pokemon-tcg-ai-battle](https://github.com/henriquetakahiroito/pokemon-tcg-ai-battle)：参考按模块解释determinization、搜索、numpy推理，以及setup→测试→打包的复现路径；不复制对方score、deck pivot结果或权重为本人结果。
- [dogahwisdom/pokemon-tcg-ai-battle-strategy](https://github.com/dogahwisdom/pokemon-tcg-ai-battle-strategy)：保留为检索到的参考入口。本次网页访问失败、GitHub API返回404，未读取到内容，不推断其架构、成绩、许可或质量。

以上参考核验日为2026-10-15。展示中的本人历史事实仍以[现有Agent catalog](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/eval/AGENT_CATALOG_FULL.md)、[scoreboard](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/report/LADDER_BEST_SO_FAR.md)、[研究brief](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/report/RESEARCH_AND_DECISION_BRIEF.md)及本地manifest/receipt为依据。
