
def ler_grafico(par):
    # Simulação de leitura de gráfico
    import random
    candles = []
    for _ in range(20):
        candle = {
            'abertura': random.uniform(1.0, 1.5),
            'fechamento': random.uniform(1.0, 1.5),
            'maxima': random.uniform(1.5, 1.6),
            'minima': random.uniform(1.0, 1.1),
            'cor': random.choice(['verde', 'vermelha'])
        }
        candles.append(candle)
    return candles
