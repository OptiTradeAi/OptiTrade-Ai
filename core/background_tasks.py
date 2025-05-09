import threading
import time
from core.learning_observer import LearningObserver
from core.signal_history_manager import SignalHistoryManager

class BackgroundTasks:
    def __init__(self):
        self.observer = LearningObserver()
        self.history = SignalHistoryManager()
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        while self.running:
            time.sleep(60)
            try:
                if self.observer.is_ready():
                    accuracy = self.observer.get_accuracy()
                    self.history.update_learning_summary(accuracy)
            except Exception as e:
                print(f"[BackgroundTasks] Erro durante verificação de performance: {e}")