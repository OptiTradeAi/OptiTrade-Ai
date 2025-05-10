# user_config.py

telegram_token = "7605762525:AAFHQWncC5Nf4cdGkvlBkwwvyShKwZxByLY"
telegram_chat_id = "-1002695222621"

fuso_horario = "America/Sao_Paulo"

# Controle por sessões
sessoes_ativas = True

sessoes = [
    {
        "nome": "Sessão Manhã",
        "inicio": "09:00",
        "fim": "12:00",
        "limite_sinais": 10
    },
    {
        "nome": "Sessão Tarde",
        "inicio": "14:00",
        "fim": "17:00",
        "limite_sinais": 8
    },
    {
        "nome": "Sessão Noite",
        "inicio": "19:00",
        "fim": "21:00",
        "limite_sinais": 5
    }
]

# Timeframes e tempo de expiração
timeframe_m1_ativo = True
timeframe_m5_ativo = True
tempo_expiracao_m1 = 1
tempo_expiracao_m5 = 5

# Estratégias e opções gerais
usar_telegram = True
gale_ativo = True
modo_teste = False
usar_m1 = True
usar_m5 = True

# Filtros para aprendizado adaptativo (sem bloqueio por estatística)
stop_win = 3
stop_loss = 3
minimo_confluencias_super_entrada = 2
minimo_acertividade_aceita = 0  # IA envia e aprende com os resultados

estrategias_ativas = {
    "3_velas": True,
    "pavio_exaustao": True,
    "rompimento_pavio_regiao": True,
    "super_entrada": True,
    "aprendizado_novo_padrao": True
}

# Dicionário final usado pela IA
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
