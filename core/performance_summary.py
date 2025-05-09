
import json
import os

class PerformanceSummary:
    def __init__(self, path='core/data/performance.json'):
        self.path = path
        self.stats = {
            'total_signals': 0,
            'wins': 0,
            'losses': 0,
            'win_rate': 0.0,
            'win_gale1': 0,
            'super_strategies': {}
        }
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.stats = json.load(f)

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, 'w') as f:
            json.dump(self.stats, f, indent=4)

    def update(self, result, strategy=None, gale_level=0):
        self.stats['total_signals'] += 1
        if result == 'win':
            self.stats['wins'] += 1
            if gale_level == 1:
                self.stats['win_gale1'] += 1
        elif result == 'loss':
            self.stats['losses'] += 1

        if strategy:
            if strategy not in self.stats['super_strategies']:
                self.stats['super_strategies'][strategy] = {'wins': 0, 'losses': 0}
            if result == 'win':
                self.stats['super_strategies'][strategy]['wins'] += 1
            elif result == 'loss':
                self.stats['super_strategies'][strategy]['losses'] += 1

        self.recalculate()
        self.save()

    def recalculate(self):
        total_effective = self.stats['wins'] + self.stats['losses']
        if total_effective > 0:
            self.stats['win_rate'] = round((self.stats['wins'] / total_effective) * 100, 2)
        else:
            self.stats['win_rate'] = 0.0
