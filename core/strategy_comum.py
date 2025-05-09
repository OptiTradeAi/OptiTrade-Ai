
class StrategyComum:
    @staticmethod
    def verificar(candle_atual, historico, zonas, indicadores):
        confluencias = []

        # Exemplo 1: estratégia das 3 velas com rompimento
        ultimas_3 = historico[-3:]
        if all(c['cor'] == ultimas_3[0]['cor'] for c in ultimas_3):
            if candle_atual.get('rompeu_resistencia') or candle_atual.get('rompeu_bollinger'):
                confluencias.append("3 velas com rompimento")

        # Exemplo 2: exaustão com confirmação
        if candle_atual.get("pavio_inferior", 0) > 2 and candle_atual.get("rompeu_suporte"):
            confluencias.append("Exaustão com pavio e rompimento")

        if confluencias:
            return {
                "valido": True,
                "direcao": "PUT" if candle_atual["cor"] == "verde" else "CALL",
                "confluencias": confluencias
            }

        return {"valido": False}
