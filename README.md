# 联合报道触达分析

联合报道、翻译版本、转载关系和访问记录。当前总览只按站点报告打开量。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.2 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

各站向编辑部提供发布清单和逐次打开记录。`edition` 按本地稿号列出在架版本；`traffic` 预览本周各站打开次数，只计算在架版本；`dispatch` 保存这次发出的周报；`archive` 按期号读回当时的内容。已发期号不覆盖。

从项目根目录运行 `python3 -m app traffic`、`python3 -m app dispatch` 或 `python3 -m app archive --key 2026-W24`。`--ledger` 可指定单独的凭证库。

`workbench.json` 中 `opens` 是逐次打开，空 `token` 表示站点无标识；标识带站点前缀，跨站对应见 `identity_links`。`relationships` 是编辑核对中的转载记录，保留状态和录入期。现有站点周报不使用这些关系计算指标。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`editions` 管理发布和撤稿, `traffic` 汇总各站上报量, `dispatch` 生成站点周报。已有总览仍使用 `data/data.json`。
