# 做过什么、结果如何、学到了什么

整理日：2026-10-15。所有μ为历史仓库记录；没有在本次同步中重新查询比赛成绩、重跑训练或推进提交。

## 从多路线实验到受控规则迭代

| 阶段 | 工作 | 结果与后续决策 |
|---|---|---|
| 远端早期Track A/B/C | 规则+浅搜索、MaskablePPO蒸馏、deck GA、AlphaZero自博弈 | 复杂路线未稳定超过规则基线；失败代码部分移到graveyard |
| 6/22 Session44 | 重置文档与架构，保留稳定agent/主干 | `core/meta/discovery`等有scaffold，不能把六大pillar全算已实现 |
| 6/23–6/24 | Dragapult loader修复、R7 bench guard；Lucario field MCTS25cycles | 真实接口修复与真实训练并存；field MCTS历史580.6低于Search660.5 |
| 6/26 S45–50 | Agent catalog、field harness、Wilson CI、pilot×deck、Alakazam移植 | local gate作为过滤；牌组与pilot不能随便互换 |
| 6/27–6/28 | 社区Archaludon v5+R7；R8–R12逐lever探针 | 历史ref54083197为1196.1；多个local gate更高的探针线上更低 |
| 7/28–7/29 Mac支线 | 比赛规则、first-min、合法动作、deterministic package、H1–H3和exact-loader | v2本地撤销；v4/v5分别有真实平台部署回执 |
| 7/30 Mac目录产物 | BC/value、Transformer、PPO rollout/update、checkpoint与ML packaging | 8个checkpoint约82.47MB；文件存在与训练效果核验分开 |
| 8/1–8/2 Mac | H-OPT、H4固定伤害排序、Formal contract/schema、历史replay stale-index分析 | 实现与历史pin测试有证据；fresh-remap controller/belief-search仍有设计边界 |
| 8/5–8/9 Mac | 官方Data更新、13个identity consumers、15包审计、内部Strategy草稿 | 574测试只支持旧pin一致；current Data身份未闭合；Writeup仍Draft |

远端有真实Git历史；本机支线原Git没有commit。此次导入只能称“历史工作区归档”，不回填虚构开发提交日期。远端7/31的auto fleet snapshot commit是快照事实，不自动证明新训练或提升。[状态文档](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/STATE.md)、[路线](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/ROADMAP.md)、[任务](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/TASKS.md)保留了不同时间截面。

## 原创实现与外部适配

我的代码/工程工作包括手写priority/context处理、浅搜索封装、包装与loader修复、合法fallback、bench guard、评测、训练脚本、逐lever实验和证据整理。游戏语义与native API来自官方引擎；官方sample及社区pilot必须署名，不能把移植解释为原创训练。

远端Dragapult/Lucario源自官方kiyotah样例；Alakazam best5源自ryotasueyoshi；Archaludon/Cinderace为社区v5；Starmie/Froslass来自ashleysandlin spread。Mac另一Alakazam包receipt注明Javier Valenzuela来源，与远端best5不是同一artifact。来源与版本详见[Agent catalog](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/eval/AGENT_CATALOG_FULL.md)。

## 负结果是复盘的核心

**接口先于强度。** 远端dragapult v1 ref53950246和Kyogre v0 ref53854588有线上`__file__` ERROR。Mac v2则是在本地官方式`exec(code,{})`四种环境复现后撤销，未提交线上。相同bug不能合并成同一次事件；普通import smoke不足以证明官方loader可用。

**训练更长没有自动变强。** 同Lucario历史记录为Search660.5、basicMCTS651.3、field25cycle MCTS580.6；Track B最好585.1，跨deck共享蒸馏是已知问题。random/mirror/Snorlax/proxy pool高胜率不能代替真实field。该次序只支持这些版本的历史负结果，不能推出所有RL无效。[研究与决策brief](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/report/RESEARCH_AND_DECISION_BRIEF.md)、[RULINGS](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/RULINGS.md)。

**搜索有成本，也可能根本没触发。** 远端SearchScorer约200ms，仅在高价值context尝试；缺engine指针、begin input或预算即fallback，Lucario混合策略还有top2 guard。必须看call/override/fallback计数，不能看到Search类名就声称“搜索贡献了分数”。慢MCTS、空bench和推理不一致会直接丢局。[搜索代码](https://github.com/KINGKAZMAX/kaggle_pokemon/blob/main/agent/search_policy.py)。

**local gate不能给线上排名排顺序。** Archaludon R8a+b local75.3%但历史μ983.8低于R7的1196.1；LucarioSearch local69.6%却μ500.1。pilot也不能跨deck直接搬：Dragapult pilot放到Lucario list时local约10%。这些不是严格同步因果实验，能支持的是保留对照、扩大真实field覆盖和拒绝单点晋升。

**Mac H1应保留失败。** 256局pilot的预注册primary42.19%，区间包含50%，座位差28.13pp，未晋升；384局removal另有runner来源/hash缺陷，应降级历史证据。574通过只意味着历史代码/数据pin自洽，不是574局胜利。

## 训练与成绩的证据边界

远端文档与历史ref可对应PPO/MCTS训练和线上负结果；部分模型代码/产物已经退役或不在main。Mac有actor-visible tensorization、deck-conditioned Transformer policy/value、BC训练、PPO采样/update及8个checkpoint，但本次没有读取其内部训练metadata，也未找到对应完整run/holdout receipts。不能把文件名step10000/g1000直接写成已核验训练量、收敛曲线或竞技收益。

catalog标题22 COMPLETE、旧brief21 COMPLETE和later probe表不是同一cutoff；session45 CSV独立解析是21 COMPLETE+2 ERROR。1196.1、880.9、660.5均是历史μ，不是胜率，也不是2026-10-15的当前成绩。远端STATE两次重传的文案“Final lock-in”不等于平台Final chooser已选中；Mac晚期20 Complete与动态账号分数也未闭合exact archive/stableID/active身份。Strategy内部草稿不等于正式提交。

## 开发 Agent 的分工

Mac记录了lead、rules、builder、evaluator、auditor五角色：builder是生产代码单写者，evaluator记录冻结实验，auditor独立审查。每轮少量假设、只实施一个，先定义样本量/指标/停止条件，再决定保留或拒绝。远端late STATE的并行gate与串行限额submit属于另一运行体系；协议/启动脚本存在不证明每个角色一直并发运行。

[返回展示页](index.html) · [卡组JSON](decks.json) · [同步范围](SYNC.md)
