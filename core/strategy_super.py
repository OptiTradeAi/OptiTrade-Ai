
class StrategySuper:
    @staticmethod
    def verificar(candle_atual, historico, zonas, indicadores):
        confluencias = []

        if candle_atual.get('cor') == 'verde' and candle_atual.get('pavio_superior', 0) > 2:
            confluencias.append('Pavio longo superior')

        if candle_atual.get('proximo_resistencia'):
            confluencias.append('Próximo à resistência')

        if candle_atual.get('rompeu_bollinger'):
            confluencias.append('Rompimento de Bollinger')

        if len(confluencias) >= 3:
            return {
                "valido": True,
                "direcao": "CALL" if candle_atual['cor'] == 'verde' else "PUT",
                "confluencias": confluencias
            }

        return {"valido": False}
