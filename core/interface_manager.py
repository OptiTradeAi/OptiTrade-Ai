
import json
from utils import load_json, save_json

CONFIG_PATH = "config/config.json"

def toggle_strategy(strategy_name):
    config = load_json(CONFIG_PATH)
    strategy = config["strategies"].get(strategy_name)
    if strategy:
        strategy["active"] = not strategy["active"]
        save_json(CONFIG_PATH, config)

def set_signal_analysis_count(count):
    config = load_json(CONFIG_PATH)
    config["settings"]["analysis_count"] = count
    save_json(CONFIG_PATH, config)

def toggle_timeframe(tf_name, state):
    config = load_json(CONFIG_PATH)
    if tf_name in config["settings"]["timeframes"]:
        config["settings"]["timeframes"][tf_name] = state
    save_json(CONFIG_PATH, config)

def mark_super_strategy(strategy_name):
    config = load_json(CONFIG_PATH)
    if strategy_name in config["strategies"]:
        config["strategies"][strategy_name]["super"] = True
        save_json(CONFIG_PATH, config)

def delete_strategy(strategy_name, password_input, actual_password):
    if password_input != actual_password:
        return False
    config = load_json(CONFIG_PATH)
    if strategy_name in config["strategies"]:
        del config["strategies"][strategy_name]
        save_json(CONFIG_PATH, config)
        return True
    return False
