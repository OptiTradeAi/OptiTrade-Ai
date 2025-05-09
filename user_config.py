
USER_CONFIG = {
    "telegram_token": "7605762525:AAFHQWncC5Nf4cdGkvlBkwwvyShKwZxByLY",
    "chat_id": "-1002695222621",

    "timeframe_m1_ativo": True,
    "timeframe_m5_ativo": True,
    "tempo_expiracao_m1": 1,
    "tempo_expiracao_m5": 5,
    "gale_ativo": True,
    "usar_telegram": True,

    "sessoes": [
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
    ],

    "stop_win": 3,
    "stop_loss": 3
}
