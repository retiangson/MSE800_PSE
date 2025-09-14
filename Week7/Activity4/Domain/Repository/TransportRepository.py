from Domain.DBManager import DBManager
from Domain.Model.Transport import Transport, RoadTruck, SeaVessel

class TransportRepository:
    def __init__(self):
        self.init()

    def init(self):
        with DBManager().connection() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS transport(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mode TEXT,
                    capacity_kg INTEGER,
                    identifier TEXT
                )
            """)
            conn.commit()

    def add(self, transport: Transport):
        conn = DBManager().connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO transport(mode, capacity_kg, identifier) VALUES(?,?,?)",
            (transport.mode, transport.capacity_kg, transport.identifier)
        )
        conn.commit()
        transport.id = cur.lastrowid
        return transport

    def list(self):
        cur = DBManager().cursor()
        rows = cur.execute("SELECT * FROM transport").fetchall()
        out = []
        for r in rows:
            if r['mode'] == 'ROAD':
                out.append(RoadTruck(r['id'], r['capacity_kg'], r['identifier']))
            else:
                out.append(SeaVessel(r['id'], r['capacity_kg'], r['identifier']))
        return out