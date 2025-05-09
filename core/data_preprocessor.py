import pandas as pd
import numpy as np
from datetime import datetime

def preprocess_candle_data(raw_data):
    processed = []
    for item in raw_data:
        try:
            processed.append({
                'time': datetime.strptime(item['time'], '%H:%M'),
                'open': float(item['open']),
                'high': float(item['high']),
                'low': float(item['low']),
                'close': float(item['close']),
                'volume': float(item.get('volume', 0)),
                'color': 'green' if float(item['close']) > float(item['open']) else 'red' if float(item['close']) < float(item['open']) else 'doji'
            })
        except Exception as e:
            print(f"Erro ao processar candle: {e}")
            continue
    return pd.DataFrame(processed)