
class AIInsightManager:
    def __init__(self):
        self.strategy_performance = {}
        self.timeframe_analysis = {}

    def update_strategy_performance(self, strategy_name, success_rate):
        self.strategy_performance[strategy_name] = success_rate

    def update_timeframe_analysis(self, timeframe, success_rate):
        self.timeframe_analysis[timeframe] = success_rate

    def get_top_strategies(self, threshold=0.8):
        return {k: v for k, v in self.strategy_performance.items() if v >= threshold}

    def get_best_timeframe(self):
        if not self.timeframe_analysis:
            return None
        return max(self.timeframe_analysis, key=self.timeframe_analysis.get)

    def clear_insights(self):
        self.strategy_performance.clear()
        self.timeframe_analysis.clear()
