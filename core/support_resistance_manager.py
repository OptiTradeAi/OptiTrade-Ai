
# support_resistance_manager.py
class SupportResistanceManager:
    def __init__(self):
        self.zones = []

    def update_zones(self, new_zones):
        for zone in new_zones:
            if zone not in self.zones:
                self.zones.append(zone)

    def get_relevant_zones(self, price):
        return [zone for zone in self.zones if abs(zone['value'] - price) < 0.02]
