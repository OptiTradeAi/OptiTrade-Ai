from core.historico_controller import calcular_taxa_por_estrategia

def identificar_super_estrategias(historico, limite=88.0):
    taxas = calcular_taxa_por_estrategia(historico)
    super_estrategias = {}
    for estrategia, taxa in taxas.items():
        if taxa >= limite:
            super_estrategias[estrategia] = taxa
    return super_estrategias