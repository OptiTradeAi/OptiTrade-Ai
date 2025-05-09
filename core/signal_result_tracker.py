
# signal_result_tracker.py

def registrar_resultado(sinal, resultado):
    with open("resultados.txt", "a") as f:
        linha = f"{sinal['par']} | {sinal['direcao']} | {sinal['expiracao']} | {resultado}\n"
        f.write(linha)

def carregar_resultados():
    resultados = []
    try:
        with open("resultados.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(" | ")
                resultados.append({
                    "par": partes[0],
                    "direcao": partes[1],
                    "expiracao": partes[2],
                    "resultado": partes[3]
                })
    except FileNotFoundError:
        pass
    return resultados
