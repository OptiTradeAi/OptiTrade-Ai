# core/timeframe_manager.py

class TimeframeManager:
    def __init__(self):
        self.active_timeframes = {
            "M1": True,
            "M5": True
        }

    def is_timeframe_active(self, timeframe):
        return self.active_timeframes.get(timeframe, False)

    def set_timeframe_state(self, timeframe, state: bool):
        if timeframe in self.active_timeframes:
            self.active_timeframes[timeframe] = state

    def get_active_timeframes(self):
        return [tf for tf, active in self.active_timeframes.items() if active]

    def set_timeframes_from_config(self, config):
        self.active_timeframes = {
            "M1": config.get("activate_m1", True),
            "M5": config.get("activate_m5", True)
        }