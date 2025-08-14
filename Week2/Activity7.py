class Employee:
    def __init__(self, name, salary, jobTitle):
        self.name = name
        self.salary = salary
        self.jobTitle = jobTitle

    def display_info(self):
        print(f"Name: {self.name}\nJob Title: {self.jobTitle}\nSalary: ${self.salary:,.2f}")
        print("-" * 30)

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise of ${amount:,.2f}!\nUpdated Salary: ${self.salary:,.2f}")
        print("-" * 30)


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


# List of employees
employees = [
    Employee("Ronald", 58000, "Software Engineer"),
    Employee("Hazel", 44000, "Nurse"),
    Employee("Celestine", 90000, "Doctor"),
    Employee("Ken", 100000, "Attorney")
]

# Loop through each employee
for emp in employees:
    emp.display_info()
    raiseAmount = get_raise_amount()
    emp.give_raise(raiseAmount)