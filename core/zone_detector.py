
import numpy as np

class ZoneDetector:
    def __init__(self, threshold=0.0005):
        self.threshold = threshold
        self.zones = []

    def detect_zones(self, candles):
        self.zones.clear()
        closes = np.array([candle['close'] for candle in candles])
        highs = np.array([candle['high'] for candle in candles])
        lows = np.array([candle['low'] for candle in candles])

        support = []
        resistance = []

        for i in range(2, len(closes) - 2):
            if lows[i] < lows[i - 1] and lows[i] < lows[i + 1] and lows[i + 1] < lows[i + 2] and lows[i - 1] < lows[i - 2]:
                support.append((i, lows[i]))
            if highs[i] > highs[i - 1] and highs[i] > highs[i + 1] and highs[i + 1] > highs[i + 2] and highs[i - 1] > highs[i - 2]:
                resistance.append((i, highs[i]))

        for index, level in support:
            if not any(abs(level - zone) < self.threshold for zone in self.zones):
                self.zones.append(level)

        for index, level in resistance:
            if not any(abs(level - zone) < self.threshold for zone in self.zones):
                self.zones.append(level)

        return sorted(self.zones)
