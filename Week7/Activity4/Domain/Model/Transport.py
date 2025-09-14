
class Transport:
    def __init__(self, id=None, mode="", capacity_kg=0, identifier=""):
        self.id = id
        self.mode = mode  # ROAD or SEA
        self.capacity_kg = capacity_kg
        self.identifier = identifier

    def __repr__(self):
        return f"<Transport {self.mode}:{self.identifier} cap={self.capacity_kg}kg>"

class RoadTruck(Transport):
    def __init__(self, id=None, capacity_kg=20000, identifier="TRK-001"):
        super().__init__(id, "ROAD", capacity_kg, identifier)

class SeaVessel(Transport):
    def __init__(self, id=None, capacity_kg=500000, identifier="VES-001"):
        super().__init__(id, "SEA", capacity_kg, identifier)
