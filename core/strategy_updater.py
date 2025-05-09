class StrategyUpdater:
    def __init__(self, statistics_manager, settings_manager):
        self.stats = statistics_manager
        self.settings = settings_manager

    def update_strategy_statuses(self):
        stats = self.stats.get_stats()
        config = self.settings.get('strategy_settings', {})

        for key, data in stats.items():
            strategy_name, timeframe = key.rsplit('_', 1)
            accuracy = data.get('accuracy', 0)
            if timeframe not in config:
                config[timeframe] = {'enabled_strategies': []}

            if accuracy >= 88:
                # Adiciona à lista de super estratégias (internamente)
                if strategy_name not in config[timeframe]['enabled_strategies']:
                    config[timeframe]['enabled_strategies'].append(strategy_name)

            elif accuracy < 80:
                # Remove se não estiver com bom desempenho
                if strategy_name in config[timeframe]['enabled_strategies']:
                    config[timeframe]['enabled_strategies'].remove(strategy_name)

        self.settings.set('strategy_settings', config)