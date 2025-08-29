from person import Person

class Teacher(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Salary: {self.salary}"