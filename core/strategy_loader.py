
import os
import importlib
from core.strategies.base import BaseStrategy

def load_strategies(directory='core/strategies'):
    strategies = []
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != 'base.py':
            module_name = f"{directory.replace('/', '.')}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, BaseStrategy) and obj is not BaseStrategy:
                    strategies.append(obj())
    return strategies
