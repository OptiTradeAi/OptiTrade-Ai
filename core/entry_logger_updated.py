
import datetime
from signal_sender import enviar_sinal

class EntryLogger:
    def __init__(self, log_file="entry_log.txt"):
        self.log_file = log_file

    def log_entry(self, par, timeframe, estrategia, direcao, gale=0, super_entrada=False):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUPER" if super_entrada else "NORMAL"
        log_line = f"[{timestamp}] PAR: {par}, TIMEFRAME: {timeframe}, ESTRATÉGIA: {estrategia}, DIREÇÃO: {direcao}, GALE: {gale}, TIPO: {status}\n"

from signal_sender import send_signal_to_telegram

# Envio do sinal para o Telegram sempre que um novo sinal for registrado
send_signal_to_telegram(par, direcao, timeframe, gale)

        
        # Grava no arquivo de log
        with open(self.log_file, "a") as f:
            f.write(log_line)

        # Envia automaticamente o sinal para o Telegram
        enviar_sinal(par, timeframe, estrategia, direcao, gale)