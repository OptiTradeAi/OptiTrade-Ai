
from datetime import datetime
from user_config import USER_CONFIG
import pytz

def obter_sessao_ativa():
    fuso = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso).strftime("%H:%M")
    for sessao in USER_CONFIG.get("sessoes", []):
        if sessao["inicio"] <= agora <= sessao["fim"]:
            return sessao
    return None
