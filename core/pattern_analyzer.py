
# pattern_analyzer.py

class PatternAnalyzer:
    def __init__(self):
        self.patterns = []

    def analyze(self, candles):
        # Exemplo básico de análise de padrão (substituir por lógica real)
        if len(candles) >= 3 and candles[-1]['color'] == candles[-2]['color'] == candles[-3]['color']:
            return {'type': '3_candles_same_color', 'direction': 'reversal'}
        return None

    def add_custom_pattern(self, pattern_func):
        self.patterns.append(pattern_func)

    def run_all_patterns(self, candles):
        results = []
        for pattern in self.patterns:
            result = pattern(candles)
            if result:
                results.append(result)
        return results
