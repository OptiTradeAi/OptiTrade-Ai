
from user_config import USER_CONFIG
import requests
from datetime import datetime, timedelta

def enviar_sinal_telegram(par, direcao, expiracao, confluencias, timeframe='M1'):
    if not USER_CONFIG["usar_telegram"]:
        print("[TELEGRAM] Envio desativado nas configurações.")
        return

    token = USER_CONFIG["telegram_token"]
    chat_id = USER_CONFIG["chat_id"]

    minutos_para_entrada = 1 if timeframe == 'M1' else 2
    hora_entrada = (datetime.now() + timedelta(minutes=minutos_para_entrada)).strftime("%H:%M")

    mensagem = f"""🚀 OptiTrade AI Identificou

📈 {par}
{'🔼 COMPRA' if direcao.upper() == 'CALL' else '🔽 VENDA'}
⏰ {hora_entrada}  ⏳ {expiracao} Minuto{'s' if expiracao > 1 else ''}
Confluências: {confluencias}

📡 Powered by Kaon"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    print("[TELEGRAM] Sinal enviado com sucesso." if response.status_code == 200 else f"[TELEGRAM] Erro: {response.text}")

def enviar_resultado_entrada(par, horario, resultado, confluencias):
    if resultado not in ["WIN", "WIN com Gale"]:
        return  # Só envia confirmação para resultados positivos

    token = USER_CONFIG["telegram_token"]
    chat_id = USER_CONFIG["chat_id"]

    mensagem = f"""━━━━━━━━━━━━━━━━━━━━
📊 <b>Resultado Confirmado</b>

• Par: {par}
• Horário da Entrada: {horario}
• Resultado: {'✅ WIN' if resultado == 'WIN' else '✅ WIN com Gale'}
• Confluências: {confluencias}

📡 <i>Powered by Kaon</i>
━━━━━━━━━━━━━━━━━━━━"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

def enviar_mensagem_stop(tipo, quantidade):
    token = USER_CONFIG["telegram_token"]
    chat_id = USER_CONFIG["chat_id"]

    icone = "✅" if tipo == "WIN" else "⛔"
    titulo = "STOP WIN ATIVADO" if tipo == "WIN" else "STOP LOSS ATIVADO"
    linha = f"Vitórias seguidas: ✅ {quantidade}" if tipo == "WIN" else f"Derrotas seguidas: ❌ {quantidade}"

    mensagem = f"""━━━━━━━━━━━━━━━━━━━━
{icone} <b>{titulo}</b>

{linha}
Respeite seu gerenciamento.
Aguarde o próximo ciclo.

📡 <i>Powered by Kaon</i>
━━━━━━━━━━━━━━━━━━━━"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)
