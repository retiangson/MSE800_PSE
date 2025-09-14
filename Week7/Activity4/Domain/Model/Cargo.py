
class Cargo:
    def __init__(self, id=None, ref=None, description="", weight_kg=0, status="QUEUED"):
        self.id = id
        self.ref = ref
        self.description = description
        self.weight_kg = weight_kg
        self.status = status  # QUEUED, LOADED, IN_TRANSIT, DELIVERED

    def __repr__(self):
        return f"<Cargo {self.ref} {self.description} {self.weight_kg}kg [{self.status}]>"
