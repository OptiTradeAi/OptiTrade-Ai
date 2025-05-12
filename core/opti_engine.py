from core import candles_reader

def get_candles(par, timeframe):
    return candles_reader.obter_candles(par=par, timeframe=timeframe)

# Aqui entra o restante do seu código original da IA
# O restante do opti_engine.py deve chamar get_candles(par, timeframe)
# em vez de buscar de outra fonte

# Exemplo de uso dentro do loop de análise
def analisar_par(par, timeframe):
    candles = get_candles(par, timeframe)
    # A lógica abaixo depende de como está implementada sua engine
    # Por exemplo:
    # resultado = aplicar_estrategias(candles)
    # if resultado:
    #     enviar_sinal_telegram(...)
    print(f"[{par}] Analisando {len(candles)} candles...")

# Este é um exemplo básico de loop
def iniciar_analise():
    pares = ['EUR/USD', 'GBP/USD']
    timeframe = 'M5'
    for par in pares:
        analisar_par(par, timeframe)

# Quando rodar este módulo diretamente, inicia análise
if __name__ == "__main__":
    iniciar_analise()
