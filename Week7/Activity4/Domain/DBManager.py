
import sqlite3
import threading

class DBManager:
    """
    Thread-safe SQLite connection manager (Singleton).
    Ensures a single connection is reused app-wide for speed and consistency.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path="port.db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._conn = sqlite3.connect(db_path, check_same_thread=False)
                cls._instance._conn.row_factory = sqlite3.Row
            return cls._instance

    def connection(self):
        return self._conn

    def cursor(self):
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()

    def __enter__(self):
        return self._conn

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self._conn.rollback()
        else:
            self._conn.commit()
