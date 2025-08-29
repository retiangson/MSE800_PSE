# School Management (School_Management)

Layered, OOP Python project using SQLAlchemy ORM with a simple interactive menu-based CLI.

## Features
- Domain / Contracts / Business / Infrastructure / Client layers
- Config-driven (config.json)
- Default admin created from config (username/password)
- Role-based menus: Admin / Teacher / Student
- SQLite DB via config (db_url)

## Quickstart
```bash
pip install -r requirements.txt
python main.py
```

On first run, initialize DB when prompted. Default admin credentials come from `config.json`.
