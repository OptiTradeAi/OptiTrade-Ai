# strategy_three_candles.py

from datetime import datetime
from core.utils import verificar_rompimento, verificar_resistencia_suporte

def estrategia_tres_velas_consecutivas(candles):
    """
    Estratégia de reversão após 3 velas consecutivas da mesma cor com confirmação por rompimento.
    Retorna um dicionário com os dados do sinal ou None.
    """
    if len(candles) < 5:
        return None

    vela1, vela2, vela3 = candles[-4], candles[-3], candles[-2]
    vela_atual = candles[-1]

    if not all(v is not None for v in [vela1, vela2, vela3, vela_atual]):
        return None

    # Verifica se as três velas anteriores são da mesma cor
    if vela1['cor'] == vela2['cor'] == vela3['cor']:
        cor_reversao = 'PUT' if vela1['cor'] == 'verde' else 'CALL'

        # Verifica se a última vela rompeu uma resistência ou suporte
        if verificar_rompimento(vela3, vela_atual):
            if verificar_resistencia_suporte(vela_atual, candles):
                return {
                    'estrategia': '3 Velas com Rompimento',
                    'direcao': cor_reversao,
                    'confianca': 85,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

    return None