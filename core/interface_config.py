
# interface_config.py

# Este módulo lida com as configurações visuais e preferências do usuário para o painel do OptiTrade AI

user_preferences = {
    "theme": "dark",
    "active_timeframes": ["M1", "M5"],
    "super_strategies_only": False,
    "signal_threshold": 80,
    "signal_count_for_analysis": 50,
    "auto_mode": True,
}

def update_preference(key, value):
    if key in user_preferences:
        user_preferences[key] = value
        return True
    return False

def get_preferences():
    return user_preferences
