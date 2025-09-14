
from Business.Services.LogisticsService import LogisticsService

svc = LogisticsService()

def menu():
    while True:
        print("\n=== Auckland Port Logistics ===")
        print("1) Register cargo")
        print("2) Add transport (ROAD/SEA)")
        print("3) Plan dispatch")
        print("4) List cargo")
        print("5) List transport")
        print("0) Exit")

        choice = input("Select: ").strip()
        if choice == "1":
            ref = input("Cargo Ref: ")
            desc = input("Description: ")
            w = int(input("Weight (kg): "))
            c = svc.register_cargo(ref, desc, w)
            print("Registered:", c)
        elif choice == "2":
            mode = input("Mode (ROAD/SEA): ")
            cap = int(input("Capacity (kg): "))
            ident = input("Identifier: ")
            t = svc.add_transport(mode, cap, ident)
            print("Added:", t)
        elif choice == "3":
            ref = input("Cargo Ref to dispatch: ")
            mode = input("Preferred Mode (ROAD/SEA): ")
            t = svc.plan_dispatch(ref, mode)
            print(f"Dispatch planned using {t}")
        elif choice == "4":
            for c in svc.cargo_repo.list():
                print(c)
        elif choice == "5":
            for t in svc.transport_repo.list():
                print(t)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
