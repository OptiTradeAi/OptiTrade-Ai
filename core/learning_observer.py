import json
import os
from core.performance_tracker import PerformanceTracker

class LearningObserver:
    def __init__(self, filepath='core/data/learning_state.json'):
        self.filepath = filepath
        self.performance = PerformanceTracker()
        self.config = {"active": False, "min_signals": 50, "signal_buffer": []}
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    self.config = json.load(f)
                except json.JSONDecodeError:
                    self.config = {"active": False, "min_signals": 50, "signal_buffer": []}

    def _save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f, indent=4)

    def set_active(self, active: bool):
        self.config["active"] = active
        self._save()

    def set_min_signals(self, quantity: int):
        self.config["min_signals"] = quantity
        self._save()

    def add_signal_result(self, strategy_name, timeframe, result):
        self.config["signal_buffer"].append({
            "strategy": strategy_name,
            "timeframe": timeframe,
            "result": result
        })

        if len(self.config["signal_buffer"]) > self.config["min_signals"]:
            self.config["signal_buffer"].pop(0)

        self._save()

    def is_ready(self):
        return len(self.config["signal_buffer"]) >= self.config["min_signals"]

    def get_accuracy(self):
        stats = {}
        for signal in self.config["signal_buffer"]:
            key = f"{signal['strategy']}_{signal['timeframe']}"
            if key not in stats:
                stats[key] = {"win": 0, "loss": 0}
            if signal["result"] == "win":
                stats[key]["win"] += 1
            elif signal["result"] == "loss":
                stats[key]["loss"] += 1

        accuracy = {}
        for key, s in stats.items():
            total = s["win"] + s["loss"]
            if total > 0:
                acc = round((s["win"] / total) * 100, 2)
                accuracy[key] = acc

        return accuracy

    def reset(self):
        self.config["signal_buffer"] = []
        self._save()