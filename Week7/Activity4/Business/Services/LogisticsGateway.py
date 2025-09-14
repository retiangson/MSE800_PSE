
import threading
from Domain.DBManager import DBManager

class LogisticsGateway:
    #Domain-level Singleton that centralizes transactional operations
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                # Touch DB to ensure it's initialized
                DBManager()
            return cls._instance
