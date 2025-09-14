
from Business.Interfaces.ILogisticsService import ILogisticsService
from Business.Services.TransportFactory import TransportFactory
from Business.Services.LogisticsGateway import LogisticsGateway
from Domain.Repository.CargoRepository import CargoRepository
from Domain.Repository.TransportRepository import TransportRepository
from Domain.Model.Cargo import Cargo

class LogisticsService(ILogisticsService):
    def __init__(self):
        self._gateway = LogisticsGateway()  # Singleton
        self.cargo_repo = CargoRepository()
        self.transport_repo = TransportRepository()

    # --- Cargo ---
    def register_cargo(self, ref, description, weight_kg):
        return self.cargo_repo.add(Cargo(ref=ref, description=description, weight_kg=weight_kg))

    # --- Transport ---
    def add_transport(self, mode, capacity_kg, identifier):
        transport = TransportFactory.create(mode, capacity_kg, identifier)
        return self.transport_repo.add(transport)

    # --- Planning ---
    def plan_dispatch(self, cargo_ref, preferred_mode):
        cargo = self.cargo_repo.get_by_ref(cargo_ref)
        if not cargo:
            raise ValueError(f"Cargo {cargo_ref} not found")
        # Naive planning: pick the first available in preferred mode with capacity.
        transports = [t for t in self.transport_repo.list() if t.mode == preferred_mode.upper() and t.capacity_kg >= cargo.weight_kg]
        if not transports:
            raise ValueError("No suitable transport available")
        self.cargo_repo.update_status(cargo_ref, "IN_TRANSIT")
        return transports[0]
