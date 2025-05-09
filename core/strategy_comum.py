from core.strategy_super import StrategySuper
from core.strategy_comum import StrategyComum

class StrategyController:
    def __init__(self):
        self.super = StrategySuper()
        self.comum = StrategyComum()

    def analisar(self, par, timeframe):
        confluencias = []

        resultado_super = self.super.verificar(par, timeframe)
        if resultado_super:
            confluencias.append(resultado_super)

        resultado_comum = self.comum.verificar(par, timeframe)
        if resultado_comum:
            confluencias.append(resultado_comum)

        if not confluencias:
            return None

        return {
            "par": par,
            "direcao": "CALL" if "alta" in " ".join(confluencias).lower() else "PUT",
            "horario": timeframe,
            "confluencias": ", ".join(confluencias)
        }
