from person import Person

class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    # Overridden version (hides address)
    def display_info(self):
        return (f"Name: {self.name}, Address: Confidential, "
            f"Age: {self.age}, ID: {self.ID}, Academic Record: {self.academic_record}")
    # Method to call the original parent version explicitly
    def display_original_info(self):
        return super().display_info() + f", Academic Record: {self.academic_record}"