# 🚀 Feishu Leaderboard Agent (基于飞书的多智能体排行榜数据分析流)

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.21-green)
![Feishu Open API](https://img.shields.io/badge/Feishu-API-00BFFF)
![License](https://img.shields.io/badge/license-MIT-blue)

本项目是一个基于 Python 异步框架与大语言模型构建的多智能体（Multi-Agent）自动化数据流转与诊断系统。它深度集成了飞书（Feishu）开放平台 API，旨在解决跨系统数据孤岛问题，实现业务排行榜数据的自动抽取、LLM 智能归因分析以及异常预警的完整自动化闭环。

## ✨ 核心特性 (Features)

* **🤖 多智能体协同 (Multi-Agent Routing)**：采用 `Fetcher -> Analyzer -> Reporter` 的流水线架构，职责清晰，高内聚低耦合。
* **📊 自动化数据流转**：定时从飞书多维表格/应用商店接口抓取原始数据，自动完成 JSON 规范化与清洗。
* **🧠 智能诊断与归因**：结合大语言模型，对排行榜指标的波动进行上下文逻辑推理与深度分析。
* **⚡ 闭环告警 (Human-in-the-loop)**：支持常规数据日报模式与高危加急告警（Urgent Message）模式，异常情况自动触发飞书机器人直呼业务负责人。

---

## 📈 架构流程图 (Architecture Flowchart)

> **核心处理逻辑**：系统通过定时任务触发，数据抽取节点完成初筛后流转至分析节点，最终由报告节点决定推送策略。

```mermaid
graph TD
    A[Cron 定时任务 / Webhook] -->|触发执行| B[Data Fetcher Agent]
    B -->|1. 请求排行榜原始数据| C[(外部接口 / 飞书多维表格)]
    C -->|2. 返回非结构化数据| B
    B -->|3. 清洗并输出标准化 JSON| D[Analyzer Agent]
    
    D -->|4. 调用 LLM 进行深度诊断| E{检测到指标异常?}
    
    E -->|是 - 如排名断崖下跌| F[Reporter Agent - 高危告警]
    E -->|否 - 指标平稳波动| G[Reporter Agent - 业务日报]
    
    F -->|5a. 触发飞书加急消息 / @负责人| H[飞书机器人]
    G -->|5b. 推送结构化分析图表| H
