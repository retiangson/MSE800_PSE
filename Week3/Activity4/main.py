from products import product_menu
from customers import customer_menu
from orders import order_menu

while True:
    print("\n=== Main Menu ===")
    print("1. Products")
    print("2. Customers")
    print("3. Orders")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        product_menu()
    elif choice == '2':
        customer_menu()
    elif choice == '3':
        order_menu()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")