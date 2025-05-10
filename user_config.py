# user_config.py

# ====== CONFIGURAÇÕES GERAIS DO USUÁRIO ======

# Telegram
telegram_token = "SEU_TOKEN_AQUI"
telegram_chat_id = "SEU_CHAT_ID_AQUI"

# Timezone (sempre use 'America/Sao_Paulo' para horário de Brasília)
fuso_horario = "America/Sao_Paulo"

# Controle por sessões (ativado ou não)
sessoes_ativas = False  # Envio de sinais livre, sem controle por horário

# Sessões configuradas (só funcionarão se sessoes_ativas = True)
horarios_sessoes = [
    {"inicio": "09:00", "fim": "12:00", "limite_sinais": 10},
    {"inicio": "14:00", "fim": "17:00", "limite_sinais": 8}
]

# Configurações de entrada
usar_gale = True
delay_antes_entrada = 0  # Segundos de espera antes da entrada
tempo_expiracao = 5  # Minutos da operação

# Estratégias ativas
estrategias_ativas = {
    "3_velas": True,
    "pavio_exaustao": True,
    "rompimento_pavio_regiao": True,
    "super_entrada": True,
    "aprendizado_novo_padrao": True
}

# Timeframes analisados
usar_m1 = True
usar_m5 = True

# Modo de operação
modo_teste = False  # True = simulação (não envia para o Telegram)

# Filtros
minimo_confluencias_super_entrada = 3
minimo_acertividade_aceita = 80

# Controle de limite de operações
limite_wins_consecutivos = 3
limite_losses_consecutivos = 3

# ====== DICIONÁRIO DE CONFIGURAÇÃO ======
USER_CONFIG = {
    "telegram_token": telegram_token,
    "telegram_chat_id": telegram_chat_id,
    "fuso_horario": fuso_horario,
    "sessoes_ativas": sessoes_ativas,
    "horarios_sessoes": horarios_sessoes,
    "usar_gale": usar_gale,
    "delay_antes_entrada": delay_antes_entrada,
    "tempo_expiracao": tempo_expiracao,
    "estrategias_ativas": estrategias_ativas,
    "usar_m1": usar_m1,
    "usar_m5": usar_m5,
    "modo_teste": modo_teste,
    "minimo_confluencias_super_entrada": minimo_confluencias_super_entrada,
    "minimo_acertividade_aceita": minimo_acertividade_aceita,
    "limite_wins_consecutivos": limite_wins_consecutivos,
    "limite_losses_consecutivos": limite_losses_consecutivos
}
