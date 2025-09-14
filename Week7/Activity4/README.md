
# AucklandPortLogistics

A Auckland Transport logistics system for port operations demonstrating **Singleton** and **Factory** design patterns. `DBManager` and `LogisticsGateway` are singletons that centralize the SQLite connection and domain orchestration. `TransportFactory` creates transport assets (ROAD trucks and SEA vessels) without exposing concrete classes to the UI. The project mirrors a layered architecture (`Business`, `Domain`, `ui`)

## Run
```bash
python main.py
```
