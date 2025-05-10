if __name__ == "__main__":
    print("========================================")
    print("      OptiTrade AI - Versão Local")
    print(" Monitoramento Real de Pares OTC M1/M5")
    print("========================================\n")

    engine = OptiEngine()

    try:
        engine.iniciar_monitoramento()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
    except Exception as e:
        print(f"Erro durante execução: {e}")
