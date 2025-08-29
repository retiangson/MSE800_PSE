
from student import Student
from academic import Academic
from general_staff import GeneralStaff

if __name__ == "__main__":
    # Create instances
    student = Student("Ron", "123 University St", 20, "S001", "Excellent")
    academic = Academic("Hazel", "45 College Rd", 45, "A123", "TX-2024", 90000)
    staff = GeneralStaff("Celestine", "78 Campus Ln", 35, "G555", "TX-5678", 25.5)

    # Display info
    print(student.display_info())
    print(academic.display_info())
    print(staff.display_info())