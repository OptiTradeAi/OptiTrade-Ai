
import json
from datetime import datetime
from core.utils.paths import get_storage_path

class SignalStorage:
    def __init__(self):
        self.storage_file = get_storage_path("signals.json")
        self.data = self._load()

    def _load(self):
        try:
            with open(self.storage_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.data, file, indent=2)

    def add_signal(self, signal):
        signal['timestamp'] = datetime.now().isoformat()
        self.data.append(signal)
        self._save()

    def get_all_signals(self):
        return self.data

    def clear(self):
        self.data = []
        self._save()
