
class AdvancedMetrics:
    def __init__(self):
        self.metrics = {}

    def update(self, strategy_name, result):
        if strategy_name not in self.metrics:
            self.metrics[strategy_name] = {"wins": 0, "losses": 0}
        if result == "win":
            self.metrics[strategy_name]["wins"] += 1
        elif result == "loss":
            self.metrics[strategy_name]["losses"] += 1

    def get_accuracy(self, strategy_name):
        data = self.metrics.get(strategy_name)
        if data:
            total = data["wins"] + data["losses"]
            return (data["wins"] / total) * 100 if total > 0 else 0
        return 0

    def get_best_strategies(self, min_accuracy=80):
        return {
            name: self.get_accuracy(name)
            for name in self.metrics
            if self.get_accuracy(name) >= min_accuracy
        }
