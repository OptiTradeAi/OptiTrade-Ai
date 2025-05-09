import json
import os

class StrategyTracker:
    def __init__(self, path="core/strategy_data.json"):
        self.path = path
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def record_result(self, strategy_name, timeframe, result):
        key = f"{strategy_name}_{timeframe}"
        if key not in self.data:
            self.data[key] = {"wins": 0, "losses": 0}
        if result == "win":
            self.data[key]["wins"] += 1
        elif result == "loss":
            self.data[key]["losses"] += 1
        self.save()

    def get_accuracy(self, strategy_name, timeframe):
        key = f"{strategy_name}_{timeframe}"
        data = self.data.get(key, {"wins": 0, "losses": 0})
        total = data["wins"] + data["losses"]
        if total == 0:
            return 0.0
        return round((data["wins"] / total) * 100, 2)

    def get_all_strategies_sorted(self):
        sorted_data = []
        for key, value in self.data.items():
            wins = value["wins"]
            losses = value["losses"]
            total = wins + losses
            accuracy = (wins / total) * 100 if total > 0 else 0
            strategy, tf = key.rsplit("_", 1)
            sorted_data.append({
                "strategy": strategy,
                "timeframe": tf,
                "wins": wins,
                "losses": losses,
                "accuracy": round(accuracy, 2)
            })
        return sorted(sorted_data, key=lambda x: x["accuracy"], reverse=True)