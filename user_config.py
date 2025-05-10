# user_config.py

# ====== CONFIGURAÇÕES GERAIS DO USUÁRIO ======

# Telegram
telegram_token = "SEU_TOKEN_AQUI"
telegram_chat_id = "SEU_CHAT_ID_AQUI"

# Timezone (sempre use 'America/Sao_Paulo' para horário de Brasília)
fuso_horario = "America/Sao_Paulo"

# Controle por sessões (ativar ou não)
sessoes_ativas = False  # Desativado, envio livre

# Sessões configuradas (serão ignoradas enquanto sessoes_ativas for False)
horarios_sessoes = [
    {"inicio": "09:00", "fim": "12:00", "limite_sinais": 10},
    {"inicio": "14:00", "fim": "17:00", "limite_sinais": 8}
]

# Configurações de entrada
usar_gale = True
delay_antes_entrada = 0  # Segundos antes da vela de entrada
tempo_expiracao = 5  # Minutos da operação

# Estratégias permitidas (pode ativar/desativar individualmente)
estrategias_ativas = {
    "3_velas": True,
    "pavio_exaustao": True,
    "rompimento_pavio_regiao": True,
    "super_entrada": True,
    "aprendizado_novo_padrao": True
}

# Timeframes para análise
usar_m1 = True
usar_m5 = True

# Modo de operação
modo_teste = False  # Se True, não envia sinal real, apenas simula

# Filtros de sinais
minimo_confluencias_super_entrada = 3
minimo_acertividade_aceita = 80

# Controle de limite
limite_wins_consecutivos = 3
limite_losses_consecutivos = 3
