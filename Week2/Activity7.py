class Employee:
    def __init__(self, name, salary, jobTitle):
        self.name = name
        self.salary = salary
        self.jobTitle = jobTitle

    def display_info(self):
        print(f"Name: {self.name}\nJob Title: {self.jobTitle}\nSalary: ${self.salary:,.2f}\n")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise of ${amount:,.2f}!\nUpdated Salary: ${self.salary:,.2f}\n")


def get_raise_amount():
    while True:
        user_input = input("Enter raise amount: ")
        try:
            amount = float(user_input)
            if amount <= 0:
                print("Please enter a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid input! Please enter a number.")


def list_employees():
    if not employees:
        print("No employees found.\n")
    else:
        for idx, emp in enumerate(employees, start=1):
            print(f"{idx}. {emp.name} - {emp.jobTitle} (${emp.salary:,.2f})")
        print()


def add_employee():
    name = input("Enter name: ")
    while True:
        try:
            salary = float(input("Enter salary: "))
            break
        except ValueError:
            print("Invalid salary! Please enter a number.")
    jobTitle = input("Enter job title: ")
    employees.append(Employee(name, salary, jobTitle))
    print(f"Employee '{name}' added successfully!\n")


def edit_employee():
    list_employees()
    try:
        choice = int(input("Select employee number to edit: ")) - 1
        if 0 <= choice < len(employees):
            emp = employees[choice]
            emp.name = input(f"Enter new name ({emp.name}): ") or emp.name
            try:
                salary_input = input(f"Enter new salary ({emp.salary}): ")
                if salary_input:
                    emp.salary = float(salary_input)
            except ValueError:
                print("Invalid salary input, keeping old salary.")
            emp.jobTitle = input(f"Enter new job title ({emp.jobTitle}): ") or emp.jobTitle
            print("Employee updated successfully!\n")
        else:
            print("Invalid selection!\n")
    except ValueError:
        print("Invalid input!\n")


def delete_employee():
    list_employees()
    try:
        choice = int(input("Select employee number to delete: ")) - 1
        if 0 <= choice < len(employees):
            removed = employees.pop(choice)
            print(f"Employee '{removed.name}' deleted successfully!\n")
        else:
            print("Invalid selection!\n")
    except ValueError:
        print("Invalid input!\n")


def raise_employee():
    list_employees()
    try:
        choice = int(input("Select employee number for raise: ")) - 1
        if 0 <= choice < len(employees):
            amount = get_raise_amount()
            employees[choice].give_raise(amount)
        else:
            print("Invalid selection!\n")
    except ValueError:
        print("Invalid input!\n")


# Initial employee list
employees = [
    Employee("Ronald", 58000, "Software Engineer"),
    Employee("Hazel", 44000, "Nurse"),
    Employee("Celestine", 90000, "Doctor"),
    Employee("Ken", 100000, "Attorney")
]

# Main loop
while True:
    print("==== HR Management Menu ====")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Delete Employee")
    print("4. Give Raise to Employee")
    print("5. List All Employees")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        edit_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        raise_employee()
    elif choice == "5":
        list_employees()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select a valid option.\n")