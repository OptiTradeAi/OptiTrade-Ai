import json
import os

class StrategyStatistics:
    def __init__(self, file_path='data/strategy_stats.json'):
        self.file_path = file_path
        self.stats = self._load_stats()

    def _load_stats(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def _save_stats(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.stats, f, indent=2)

    def register_result(self, strategy_name, timeframe, result):
        key = f"{strategy_name}_{timeframe}"
        if key not in self.stats:
            self.stats[key] = {"wins": 0, "losses": 0, "total": 0, "accuracy": 0.0}

        if result == 'win':
            self.stats[key]['wins'] += 1
        elif result == 'loss':
            self.stats[key]['losses'] += 1
        
        self.stats[key]['total'] += 1
        self.stats[key]['accuracy'] = round(
            100 * self.stats[key]['wins'] / self.stats[key]['total'], 2
        )

        self._save_stats()

    def get_stats(self):
        return self.stats

    def reset(self):
        self.stats = {}
        self._save_stats()