def selecionar_timeframe_mais_eficaz(taxa_m1, taxa_m5):
    if taxa_m1 >= taxa_m5:
        return "M1"
    else:
        return "M5"