from core.session_manager import SessionManager
from core.strategy_controller import StrategyController
from core.result_tracker import ResultTracker
from core.signal_sender import SignalSender

class OptiEngine:
    def __init__(self):
        print("OptiEngine inicializado")
        self.session_manager = SessionManager()
        self.strategy_controller = StrategyController()
        self.result_tracker = ResultTracker()
        self.signal_sender = SignalSender()

    def iniciar_monitoramento(self):
        print("Monitoramento iniciado...")
        while True:
            if not self.session_manager.sessao_ativa():
                continue

            par_ativo, timeframe = self.session_manager.obter_proximo_par()
            sinal = self.strategy_controller.analisar(par_ativo, timeframe)

            if sinal:
                self.signal_sender.enviar(sinal)
                self.result_tracker.registrar_analise(sinal)
