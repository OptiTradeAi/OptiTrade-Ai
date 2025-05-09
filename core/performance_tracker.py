import json
import os

class PerformanceTracker:
    def __init__(self, filepath='core/data/performance.json'):
        self.filepath = filepath
        self.data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = {}
        else:
            self.data = {}

    def _save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update(self, strategy_name, timeframe, result):
        key = f"{strategy_name}_{timeframe}"
        if key not in self.data:
            self.data[key] = {"win": 0, "loss": 0}

        if result == "win":
            self.data[key]["win"] += 1
        elif result == "loss":
            self.data[key]["loss"] += 1

        self._save()

    def get_accuracy(self, strategy_name, timeframe):
        key = f"{strategy_name}_{timeframe}"
        stats = self.data.get(key, {"win": 0, "loss": 0})
        total = stats["win"] + stats["loss"]
        if total == 0:
            return 0
        return round((stats["win"] / total) * 100, 2)

    def get_all_stats(self):
        return self.data

    def reset(self):
        self.data = {}
        self._save()