import json
import os

class UserSettings:
    def __init__(self, path="core/user_settings.json"):
        self.path = path
        self.settings = {
            "active_timeframes": ["M1", "M5"],
            "signal_threshold": 80,
            "observation_mode": True,
            "observation_signals": 50,
            "active_strategies": [],
            "super_strategies_only": False,
            "enable_gale": True,
            "send_signals": False
        }
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.settings.update(json.load(f))

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save()

    def get_setting(self, key):
        return self.settings.get(key)

    def get_all(self):
        return self.settings