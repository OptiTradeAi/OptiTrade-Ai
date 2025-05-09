
class SupportResistanceTracker:
    def __init__(self):
        self.support_zones = []
        self.resistance_zones = []

    def update_zones(self, price_data):
        # Lógica simplificada para detectar zonas de suporte e resistência
        highs = [candle['high'] for candle in price_data]
        lows = [candle['low'] for candle in price_data]

        resistance = max(highs)
        support = min(lows)

        if resistance not in self.resistance_zones:
            self.resistance_zones.append(resistance)

        if support not in self.support_zones:
            self.support_zones.append(support)

    def get_support(self):
        return self.support_zones[-3:]  # Últimos 3 suportes

    def get_resistance(self):
        return self.resistance_zones[-3:]  # Últimas 3 resistências
