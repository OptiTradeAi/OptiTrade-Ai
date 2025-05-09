
from core.signal_generator import estrategias_ativas

def mostrar_painel_estrategias():
    print("\n==== ESTRATÉGIAS ATIVAS ====")
    for i, (nome, status) in enumerate(estrategias_ativas.items(), 1):
        nome_legivel = nome.replace("_", " ").capitalize()
        status_texto = "ON" if status else "OFF"
        print(f"[{i}] {nome_legivel:<30} | {status_texto}")
    print("==============================\n")
