
class StrategyRegistry:
    def __init__(self):
        self.strategies = {}

    def register(self, name, strategy_function):
        self.strategies[name] = strategy_function

    def unregister(self, name):
        if name in self.strategies:
            del self.strategies[name]

    def get(self, name):
        return self.strategies.get(name)

    def get_all(self):
        return self.strategies
