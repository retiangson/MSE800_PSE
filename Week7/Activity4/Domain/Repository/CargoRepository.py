from Domain.DBManager import DBManager
from Domain.Model.Cargo import Cargo

class CargoRepository:
    def __init__(self):
        self.init()

    def init(self):
        with DBManager().connection() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS cargo(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ref TEXT UNIQUE,
                    description TEXT,
                    weight_kg INTEGER,
                    status TEXT
                )
            """)
            conn.commit()

    def add(self, cargo: Cargo):
        conn = DBManager().connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cargo(ref, description, weight_kg, status) VALUES(?,?,?,?)",
            (cargo.ref, cargo.description, cargo.weight_kg, cargo.status)
        )
        conn.commit()
        cargo.id = cur.lastrowid
        return cargo

    def get_by_ref(self, ref):
        cur = DBManager().cursor()
        row = cur.execute("SELECT * FROM cargo WHERE ref=?", (ref,)).fetchone()
        if not row:
            return None
        return Cargo(row['id'], row['ref'], row['description'], row['weight_kg'], row['status'])

    def update_status(self, ref, status):
        conn = DBManager().connection()
        conn.execute("UPDATE cargo SET status=? WHERE ref=?", (status, ref))
        conn.commit()

    def list(self, only_active=True):
        cur = DBManager().cursor()
        q = "SELECT * FROM cargo"
        rows = cur.execute(q).fetchall()
        return [Cargo(r['id'], r['ref'], r['description'], r['weight_kg'], r['status']) for r in rows]


