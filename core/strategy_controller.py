
from core.strategy_comum import StrategyComum
from core.strategy_super import StrategySuper
from signal_sender import enviar_sinal_telegram, enviar_resultado_entrada
from user_config import USER_CONFIG
from datetime import datetime, timedelta
import time

sinais_em_espera = []

def aplicar_estrategias(par, timeframe='M1'):
    # Simulação de dados da vela atual
    candle_atual = {
        "cor": "verde",
        "pavio_superior": 3,
        "pavio_inferior": 1,
        "rompeu_bollinger": True,
        "proximo_resistencia": True,
        "rompeu_resistencia": True,
        "rompeu_suporte": False
    }

    historico = [
        {"cor": "verde"}, {"cor": "verde"}, {"cor": "verde"}
    ]

    zonas = {
        "suporte": [1.1200],
        "resistencia": [1.1300]
    }

    indicadores = {
        "bollinger_rompida": True
    }

    candidatos = []

    resultado_super = StrategySuper.verificar(candle_atual, historico, zonas, indicadores)
    if resultado_super.get("valido"):
        resultado_super["forca"] = len(resultado_super["confluencias"])
        resultado_super["tipo"] = "super"
        candidatos.append(resultado_super)

    resultado_comum = StrategyComum.verificar(candle_atual, historico, zonas, indicadores)
    if resultado_comum.get("valido"):
        resultado_comum["forca"] = len(resultado_comum["confluencias"])
        resultado_comum["tipo"] = "comum"
        candidatos.append(resultado_comum)

    if not candidatos:
        return None

    melhor_sinal = sorted(candidatos, key=lambda x: x["forca"], reverse=True)[0]
    direcao = melhor_sinal["direcao"]
    confluencias = ", ".join(melhor_sinal["confluencias"])
    forca = melhor_sinal["forca"]

    # Definir tempo de entrada com base no timeframe
    tempo_expiracao = USER_CONFIG["tempo_expiracao_m1"] if timeframe == "M1" else USER_CONFIG["tempo_expiracao_m5"]
    delay_entrada = 2 if timeframe == "M1" else 2
    delay_resultado = 1 if timeframe == "M1" else tempo_expiracao

    horario_entrada = (datetime.now() + timedelta(minutes=delay_entrada)).strftime("%H:%M")

    enviar_sinal_telegram(par, direcao, tempo_expiracao, confluencias, timeframe)

    # Simular espera até o resultado real
    time.sleep(delay_entrada * 60 + delay_resultado * 60)

    resultado_final = "WIN"  # Aqui no futuro será o resultado real com leitura gráfica
    if resultado_final in ["WIN", "WIN com Gale"]:
        enviar_resultado_entrada(par, horario_entrada, resultado_final, confluencias)

    return resultado_final
