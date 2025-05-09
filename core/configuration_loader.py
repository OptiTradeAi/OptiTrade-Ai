# core/configuration_loader.py

import json
import os

class ConfigurationLoader:
    def __init__(self, path="config.json"):
        self.path = path
        self.default_config = {
            "activate_m1": True,
            "activate_m5": True,
            "signal_analysis_count": 50,
            "super_strategy_threshold": 88,
            "password": "admin"
        }
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.path):
            self.save_config(self.default_config)
            return self.default_config.copy()

        with open(self.path, "r") as file:
            try:
                data = json.load(file)
                for key in self.default_config:
                    if key not in data:
                        data[key] = self.default_config[key]
                return data
            except json.JSONDecodeError:
                self.save_config(self.default_config)
                return self.default_config.copy()

    def save_config(self, new_config=None):
        config_to_save = new_config if new_config else self.config
        with open(self.path, "w") as file:
            json.dump(config_to_save, file, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()