# user_config.py

telegram_token = "7605762525:AAFHQWncC5Nf4cdGkvlBkwwvyShKwZxByLY"
telegram_chat_id = "-1002695222621"
fuso_horario = "America/Sao_Paulo"

# Sessões desativadas (IA roda o tempo todo)
sessoes_ativas = False
sessoes = []

# Timeframe configurado para M5 apenas
usar_m1 = False
usar_m5 = True
tempo_expiracao_m1 = 1
tempo_expiracao_m5 = 5

# Estratégias de mercado ativas
estrategias_ativas = {
    "bollinger_band": True,            # Cruzamento da banda + reversão com referência
    "engolfo": True,                   # Engolfo de alta/baixa
    "martelo_estrela": True,          # Martelo / Estrela cadente
    "inside_bar": True,               # Inside Bar (explosão)
    "tres_velas_simples": True,       # Três velas com rompimento ou fraqueza
    "candle_forca_zona": True,        # Vela cheia forte em zona
    # Estratégias desativadas
    "3_velas": False,
    "pavio_exaustao": False,
    "rompimento_pavio_regiao": False,
    "super_entrada": False,
    "aprendizado_novo_padrao": False
}

# Envio e comportamento
usar_telegram = True
gale_ativo = True
modo_teste = False

# Filtros desligados para aprendizado livre
stop_win = 3
stop_loss = 3
minimo_confluencias_super_entrada = 0
minimo_acertividade_aceita = 0

# Pacote de configuração final usado pela IA
USER_CONFIG = {
    "telegram_token": telegram_token,
    "telegram_chat_id": telegram_chat_id,
    "fuso_horario": fuso_horario,
    "sessoes_ativas": sessoes_ativas,
    "sessoes": sessoes,
    "usar_telegram": usar_telegram,
    "usar_m1": usar_m1,
    "usar_m5": usar_m5,
    "tempo_expiracao_m1": tempo_expiracao_m1,
    "tempo_expiracao_m5": tempo_expiracao_m5,
    "gale_ativo": gale_ativo,
    "modo_teste": modo_teste,
    "estrategias_ativas": estrategias_ativas,
    "stop_win": stop_win,
    "stop_loss": stop_loss,
    "minimo_confluencias_super_entrada": minimo_confluencias_super_entrada,
    "minimo_acertividade_aceita": minimo_acertividade_aceita
}
