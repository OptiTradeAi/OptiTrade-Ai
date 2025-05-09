
from core.strategy_controller import aplicar_estrategias
from user_config import USER_CONFIG
from signal_sender import enviar_mensagem_stop
from datetime import datetime
import time
import requests
import pytz

class OptiEngine:
    def __init__(self):
        self.pares_otc = USER_CONFIG.get("pares_otc_ativos", [])
        self.timeframe_m1 = USER_CONFIG.get("timeframe_m1_ativo", True)
        self.timeframe_m5 = USER_CONFIG.get("timeframe_m5_ativo", True)
        self.stop_win = USER_CONFIG.get("stop_win", 3)
        self.stop_loss = USER_CONFIG.get("stop_loss", 3)
        self.usa_sessoes = USER_CONFIG.get("sessoes", []) != []
        self.resetar_sessao()
        self.fuso_brasilia = pytz.timezone("America/Sao_Paulo")

    def agora_brasilia(self):
        return datetime.now(self.fuso_brasilia)

    def resetar_sessao(self):
        self.win_seguidos = 0
        self.loss_seguidos = 0
        self.pausado = False
        self.sinais_sessao = []
        self.sessao_atual = None
        self.enviou_resumo = False

    def checar_sessao_ativa(self):
        agora = self.agora_brasilia().strftime("%H:%M")
        for sessao in USER_CONFIG.get("sessoes", []):
            if sessao["inicio"] <= agora <= sessao["fim"]:
                return sessao
        return None

    def aplicar_resultado(self, resultado, par, hora, confluencias):
        if resultado == "WIN":
            self.win_seguidos += 1
            self.loss_seguidos = 0
        elif resultado == "WIN com Gale":
            self.win_seguidos += 1
            self.loss_seguidos = 0
        elif resultado == "LOSS":
            self.loss_seguidos += 1
            self.win_seguidos = 0

        self.sinais_sessao.append({
            "par": par,
            "resultado": resultado,
            "hora": hora,
            "confluencias": confluencias
        })

        if self.stop_win and self.win_seguidos >= self.stop_win:
            self.pausado = True
            enviar_mensagem_stop("WIN", self.win_seguidos)
        elif self.stop_loss and self.loss_seguidos >= self.stop_loss:
            self.pausado = True
            enviar_mensagem_stop("LOSS", self.loss_seguidos)

    def iniciar_monitoramento(self):
        print("OptiEngine iniciou com sucesso.")
        print("Modo: Sessões ativadas" if self.usa_sessoes else "Modo: Livre (sem sessões)")

        while True:
            if self.usa_sessoes:
                self.sessao_atual = self.checar_sessao_ativa()
                if not self.sessao_atual:
                    print("[AGUARDANDO] Fora do horário de qualquer sessão.")
                    time.sleep(30)
                    continue

                if len(self.sinais_sessao) >= self.sessao_atual["limite_sinais"]:
                    print("[ENCERRADO] Limite de sinais da sessão atingido.")
                    time.sleep(30)
                    continue

            if self.pausado:
                print("[PAUSADO] Stop WIN ou LOSS atingido.")
                time.sleep(30)
                continue

            for par in self.pares_otc:
                print(f"Analisando: {par}")
                if self.timeframe_m1:
                    resultado = aplicar_estrategias(par, timeframe='M1')
                    if resultado:
                        hora = self.agora_brasilia().strftime("%H:%M")
                        self.aplicar_resultado(resultado, par, hora, "Detectado")
                        return

                if self.timeframe_m5:
                    resultado = aplicar_estrategias(par, timeframe='M5')
                    if resultado:
                        hora = self.agora_brasilia().strftime("%H:%M")
                        self.aplicar_resultado(resultado, par, hora, "Detectado")
                        return

            print("Aguardando próximo ciclo...")
            time.sleep(10)
