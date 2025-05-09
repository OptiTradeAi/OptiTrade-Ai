from datetime import datetime
from core.update_user import UpdateUser

class SessionManager:
    def __init__(self):
        self.update_user = UpdateUser()

    def sessao_ativa(self):
        """
        Verifica se a IA deve estar ativa com base nas configurações de horário.
        """
        if not self.update_user.usar_sessoes():
            return True  # Sessões desativadas → sempre ativo

        agora = datetime.now().strftime("%H:%M")
        for sessao in self.update_user.obter_sessoes():
            if sessao["inicio"] <= agora <= sessao["fim"]:
                return True
        return False

    def obter_proximo_par(self):
        """
        Define o próximo par e timeframe para análise.
        Por enquanto retorna fixo para fins de teste.
        """
        return "EURUSD-OTC", "M1"
