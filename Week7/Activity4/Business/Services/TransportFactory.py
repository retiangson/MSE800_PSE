
from Domain.Model.Transport import RoadTruck, SeaVessel

class TransportFactory:
    #Factory that creates transport instances for different modes.  Extendable (e.g., add RAIL or AIR later without changing client code).
    @staticmethod
    def create(mode: str, capacity_kg: int, identifier: str):
        m = (mode or "").strip().upper()
        if m in ("ROAD", "TRUCK"):
            return RoadTruck(capacity_kg=capacity_kg, identifier=identifier)
        elif m in ("SEA", "VESSEL", "SHIP"):
            return SeaVessel(capacity_kg=capacity_kg, identifier=identifier)
        else:
            raise ValueError(f"Unsupported mode: {mode}")
