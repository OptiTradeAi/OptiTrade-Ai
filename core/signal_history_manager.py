
import json
import os

class SignalHistoryManager:
    def __init__(self, history_file='signal_history.json'):
        self.history_file = history_file
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_history(self):
        with open(self.history_file, 'w') as file:
            json.dump(self.history, file, indent=4)

    def add_signal(self, signal_data):
        self.history.append(signal_data)
        self.trim_history()
        self.save_history()

    def trim_history(self, max_length=500):
        if len(self.history) > max_length:
            self.history = self.history[-max_length:]

    def get_recent_signals(self, limit=100):
        return self.history[-limit:]

    def clear_history(self):
        self.history = []
        self.save_history()
