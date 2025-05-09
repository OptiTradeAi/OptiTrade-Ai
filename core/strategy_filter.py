class StrategyFilter:
    def __init__(self, settings_manager, statistics_manager):
        self.settings = settings_manager
        self.statistics = statistics_manager

    def is_strategy_enabled(self, strategy_name, timeframe):
        config = self.settings.get('strategy_settings', {})
        enabled_strategies = config.get(timeframe, {}).get('enabled_strategies', [])
        return strategy_name in enabled_strategies

    def is_super_strategy(self, strategy_name, timeframe):
        stats = self.statistics.get_stats()
        key = f"{strategy_name}_{timeframe}"
        if key in stats:
            return stats[key]["accuracy"] >= 88.0
        return False

    def should_run_strategy(self, strategy_name, timeframe):
        if not self.is_strategy_enabled(strategy_name, timeframe):
            return False
        min_accuracy = self.settings.get('min_strategy_accuracy', 80.0)
        stats = self.statistics.get_stats()
        key = f"{strategy_name}_{timeframe}"
        if key in stats:
            return stats[key]["accuracy"] >= min_accuracy
        return True