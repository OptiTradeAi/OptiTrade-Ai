
import random
from datetime import datetime, timedelta

def gerar_candle(fechamento_anterior):
    variacao = random.uniform(-0.0004, 0.0004)
    abertura = fechamento_anterior
    fechamento = abertura + variacao
    minimo = min(abertura, fechamento) - abs(variacao) * 0.5
    maximo = max(abertura, fechamento) + abs(variacao) * 0.5
    cor = 'verde' if fechamento > abertura else 'vermelha'
    return {
        'abertura': round(abertura, 5),
        'fechamento': round(fechamento, 5),
        'minimo': round(minimo, 5),
        'maximo': round(maximo, 5),
        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cor': cor
    }

# Simula lista de candles para um par
def obter_candles(par='EUR/USD', timeframe='M5', quantidade=20):
    candles = []
    fechamento = 1.10000
    for _ in range(quantidade):
        candle = gerar_candle(fechamento)
        candles.append(candle)
        fechamento = candle['fechamento']
    return candles
