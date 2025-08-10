def main():
    personal_details = []

    name = input("Enter your name: ")

    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        else:
            print("Invalid input. Please enter a positive integer for age.")

    address = input("Enter your address: ")

    personal_details = [name, int(age), address]

    print("\nPersonal Details:")
    print(f"Name: {personal_details[0]}")
    print(f"Age: {personal_details[1]}")
    print(f"Address: {personal_details[2]}")

    while True:
        years_input = input("\nHow many years do you want to add to your age? ")
        if years_input.isdigit() and int(years_input) > 0:
            add = int(years_input)
            break
        else:
            print("Invalid input. Please enter a positive integer")

    personal_details[1] += add

    print(f"\nAfter adding {add} years, {personal_details[0]} will be {personal_details[1]} years old and lives at {personal_details[2]}.")

if __name__ == "__main__":
    main()