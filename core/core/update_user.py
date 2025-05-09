from user_config import USER_CONFIG

class UpdateUser:
    def __init__(self):
        self.config = USER_CONFIG

    def obter_chat_id(self):
        return self.config.get("telegram_chat_id", "")

    def obter_token(self):
        return self.config.get("telegram_token", "")

    def usar_sessoes(self):
        return self.config.get("horario_envio_sinais", {}).get("usar_sessoes", False)

    def obter_sessoes(self):
        return self.config.get("horario_envio_sinais", {}).get("sessoes", [])

    def usar_limites(self):
        return self.config.get("limites", {}).get("usar_limites", False)

    def obter_stop_win(self):
        return self.config.get("limites", {}).get("stop_win", 0)

    def obter_stop_loss(self):
        return self.config.get("limites", {}).get("stop_loss", 0)
