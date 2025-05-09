
import pandas as pd

class PatternAnalytics:
    def __init__(self):
        self.pattern_data = []

    def record_pattern(self, pattern_name, result):
        self.pattern_data.append({'pattern': pattern_name, 'result': result})

    def get_accuracy_by_pattern(self):
        df = pd.DataFrame(self.pattern_data)
        if df.empty:
            return {}
        grouped = df.groupby('pattern')['result'].value_counts().unstack().fillna(0)
        accuracy = {}
        for pattern in grouped.index:
            total = grouped.loc[pattern].sum()
            wins = grouped.loc[pattern].get('win', 0)
            accuracy[pattern] = round((wins / total) * 100, 2) if total else 0
        return accuracy

    def get_top_patterns(self, threshold=80):
        accuracy = self.get_accuracy_by_pattern()
        return {p: acc for p, acc in accuracy.items() if acc >= threshold}
