
import random

class SignalGenerator:
    def __init__(self):
        self.signals = []
        self.active_strategies = []
        self.analysis_data = []
        self.accuracy_stats = {}
        self.learning_mode = False

    def set_strategies(self, strategies):
        self.active_strategies = strategies

    def analyze_market(self, data):
        # Simulação de análise de mercado
        analyzed = random.choice([True, False])
        if analyzed:
            signal = self._generate_signal(data)
            self.signals.append(signal)
            return signal
        return None

    def _generate_signal(self, data):
        # Gerar sinal simulado com base em dados
        return {
            'pair': data.get('pair', 'EUR/USD'),
            'direction': random.choice(['CALL', 'PUT']),
            'confidence': random.randint(70, 95),
            'strategy': random.choice(self.active_strategies if self.active_strategies else ['Estratégia A']),
            'timeframe': data.get('timeframe', 'M1')
        }

    def get_recent_signals(self, count=10):
        return self.signals[-count:]

    def learn_from_results(self, results):
        for result in results:
            strat = result['strategy']
            if strat not in self.accuracy_stats:
                self.accuracy_stats[strat] = {'wins': 0, 'losses': 0}
            if result['result'] == 'WIN':
                self.accuracy_stats[strat]['wins'] += 1
            else:
                self.accuracy_stats[strat]['losses'] += 1

    def get_strategy_accuracy(self):
        accuracies = {}
        for strat, stats in self.accuracy_stats.items():
            total = stats['wins'] + stats['losses']
            accuracy = (stats['wins'] / total) * 100 if total > 0 else 0
            accuracies[strat] = round(accuracy, 2)
        return accuracies
