import asyncio
from agents.data_fetcher import DataFetcherAgent
from agents.analyzer import AnalyzerAgent
from agents.reporter import ReporterAgent

async def main():
    # 1. 初始化各 Agent 实例
    fetcher = DataFetcherAgent(app_id="your_app_id", app_secret="your_app_secret")
    analyzer = AnalyzerAgent(llm_api_key="your_api_key")
    reporter = ReporterAgent(webhook_url="https://open.feishu.cn/...")

    print("=== 🚀 开始执行排行榜同步与诊断工作流 ===")
    
    # 2. 编排 Multi-Agent 流水线
    try:
        raw_data = await fetcher.fetch_ranking_data()
        analysis = await analyzer.analyze_trends(raw_data)
        push_status = await reporter.send_feishu_report(analysis)
        
        print(f"=== ✅ 工作流执行完毕，最终状态: {push_status} ===")
    except Exception as e:
        print(f"=== ❌ 工作流执行失败: {str(e)} ===")

if __name__ == "__main__":
    asyncio.run(main())
