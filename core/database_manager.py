
import sqlite3

class DatabaseManager:
    def __init__(self, db_path='core/optitrade.db'):
        self.db_path = db_path
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS strategy_stats (
                    strategy_name TEXT,
                    timeframe TEXT,
                    wins INTEGER DEFAULT 0,
                    losses INTEGER DEFAULT 0
                )
            ''')
            conn.commit()

    def update_stats(self, strategy_name, timeframe, result):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO strategy_stats (strategy_name, timeframe, wins, losses)
                VALUES (?, ?, 0, 0)
                ON CONFLICT(strategy_name, timeframe)
                DO NOTHING
            ''', (strategy_name, timeframe))
            if result == 'win':
                cursor.execute('''
                    UPDATE strategy_stats
                    SET wins = wins + 1
                    WHERE strategy_name = ? AND timeframe = ?
                ''', (strategy_name, timeframe))
            elif result == 'loss':
                cursor.execute('''
                    UPDATE strategy_stats
                    SET losses = losses + 1
                    WHERE strategy_name = ? AND timeframe = ?
                ''', (strategy_name, timeframe))
            conn.commit()

    def get_stats(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM strategy_stats')
            return cursor.fetchall()
