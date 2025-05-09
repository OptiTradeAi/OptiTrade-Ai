import json
import os

HISTORICO_PATH = "dados/historico_sinais.json"

def carregar_historico():
    if not os.path.exists(HISTORICO_PATH):
        return []
    with open(HISTORICO_PATH, "r") as f:
        return json.load(f)

def salvar_historico(historico):
    with open(HISTORICO_PATH, "w") as f:
        json.dump(historico, f, indent=4)

def adicionar_resultado_ao_historico(resultado):
    historico = carregar_historico()
    historico.append(resultado)
    if len(historico) > 300:
        historico = historico[-300:]
    salvar_historico(historico)

def calcular_taxa_acertos(historico):
    if not historico:
        return 0.0
    acertos = sum(1 for item in historico if item["resultado"] in ["WIN", "WIN-GALE"])
    return round(acertos / len(historico) * 100, 2)

def calcular_taxa_por_estrategia(historico):
    estatisticas = {}
    for item in historico:
        estrategia = item.get("estrategia", "Desconhecida")
        if estrategia not in estatisticas:
            estatisticas[estrategia] = {"total": 0, "acertos": 0}
        estatisticas[estrategia]["total"] += 1
        if item["resultado"] in ["WIN", "WIN-GALE"]:
            estatisticas[estrategia]["acertos"] += 1

    resultados = {}
    for estrategia, dados in estatisticas.items():
        total = dados["total"]
        acertos = dados["acertos"]
        taxa = round(acertos / total * 100, 2) if total > 0 else 0.0
        resultados[estrategia] = taxa
    return resultados

def limpar_historico():
    if os.path.exists(HISTORICO_PATH):
        os.remove(HISTORICO_PATH)