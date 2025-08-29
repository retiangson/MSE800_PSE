import json, pathlib
CONFIG_PATH = pathlib.Path(__file__).resolve().parent.parent / "config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    _cfg = json.load(f)
DB_URL = _cfg.get("db_url", "sqlite:///school.db")
DEFAULT_ADMIN = _cfg.get("default_admin", {"username":"admin","password":"admin","name":"System Administrator"})
