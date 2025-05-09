
from user_config import USER_CONFIG
import requests

def enviar_resultado_entrada(par, horario, resultado, confluencias):
    emoji = "✅" if resultado == "WIN" else ("🌀" if "Gale" in resultado else "❌")
    mensagem = f"""━━━━━━━━━━━━━━━━━━━━
📊 <b>Resultado Confirmado</b>

• Par: <b>{par}</b>  
• Horário da Entrada: <b>{horario}</b>  
• Resultado: {emoji} <b>{resultado}</b>  
• Confluências: <i>{confluencias}</i>  

📡 <i>Powered by Kaon</i>
━━━━━━━━━━━━━━━━━━━━"""

    try:
        url = f"https://api.telegram.org/bot{USER_CONFIG['telegram_token']}/sendMessage"
        data = {
            "chat_id": USER_CONFIG["chat_id"],
            "text": mensagem,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
    except Exception as e:
        print("[ERRO] Falha ao enviar resultado:", e)
