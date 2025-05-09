import traceback

class ErrorHandler:
    def __init__(self, logger=None):
        self.logger = logger

    def handle(self, error: Exception, context: str = ""):
        message = f"Erro ocorrido em {context}: {str(error)}\n{traceback.format_exc()}"
        print(message)
        if self.logger:
            self.logger.error(message)