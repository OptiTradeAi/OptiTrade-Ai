import time
from core.engine import OptiEngine

if __name__ == "__main__":
    print("OptiEngine inicializado")
    OptiEngine().iniciar_monitoramento()

    # Mantém o serviço vivo no Render
    while True:
        time.sleep(3600)
