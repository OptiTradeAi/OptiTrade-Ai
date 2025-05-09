class StrategyGrouping:
    def __init__(self, statistics_manager):
        self.stats = statistics_manager

    def categorize_strategies(self):
        stats = self.stats.get_stats()
        super_strategies = {}
        regular_strategies = {}

        for key, data in stats.items():
            strategy_name, timeframe = key.rsplit('_', 1)
            accuracy = data.get('accuracy', 0)

            group = super_strategies if accuracy >= 88 else regular_strategies

            if timeframe not in group:
                group[timeframe] = []

            group[timeframe].append({
                'strategy': strategy_name,
                'accuracy': accuracy,
                'wins': data.get('win', 0),
                'losses': data.get('loss', 0),
            })

        return super_strategies, regular_strategies