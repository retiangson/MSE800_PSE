class Student:
    """
    The Student class demonstrates the use of:
    - Public attributes & methods (accessible anywhere)
    - Protected attributes & methods (accessible within class and subclasses)
    - Private attributes & methods (accessible only within the class itself)

    Attributes:
        name (str): Public attribute storing student name
        _age (int): Protected attribute storing student age
        __grade (str): Private attribute storing student grade
    """

    def __init__(self, name, age):
        """
        Initialize a new student with name and age.
        By default, grade is private and set to 'A'.
        """
        self.name = name       # Public attribute
        self._age = age        # Protected attribute
        self.__grade = 'A'     # Private attribute

    def get_grade(self):
        """
        Public method to access the private grade.
        Returns:
            str: The student's grade
        """
        return self.__grade
    
    def _promote(self):
        """
        Protected method that modifies the student's grade.
        Accessible inside this class and subclasses.
        
        - Calls a private method __demote() internally
        - Then promotes the student (e.g., A → A+)

        Returns:
            str: The updated grade after promotion
        """
        self.__demote()  # Private method can be called here
        if self.__grade == 'A':
            self.__grade = 'A+'   # Example promotion
        else:
            self.__grade = 'A'
        return self.__grade
    
    def __demote(self):
        """
        Private method that modifies the student's grade.
        Accessible only inside the Student class.

        Returns:
            str: The updated grade after demotion
        """
        if self.__grade == 'A':
            self.__grade = 'A-'   # Example demotion
        else:
            self.__grade = 'A'
        return self.__grade


class GraduateStudent(Student):
    """
    GraduateStudent inherits from Student.
    Demonstrates how subclasses can access:
    - Public methods
    - Protected methods
    But cannot directly access private methods or attributes.
    """

    def __init__(self, name, age, thesis_title):
        """
        Initialize a GraduateStudent with additional attribute: thesis_title
        """
        super().__init__(name, age)
        self.thesis_title = thesis_title   # New public attribute

    def display_info(self):
        """
        Display student details.
        Demonstrates accessing public and protected attributes.
        """
        return f"Graduate Student: {self.name}, Age: {self._age}, Thesis: {self.thesis_title}"
    
    def promote(self):
        """
        Calls the protected _promote() method from the parent class.
        """
        return self._promote()
    
    # def demote(self):   # ❌ Not possible
    #     return self.__demote() 
    # (Private methods from Student cannot be accessed here)


class Main:
    """
    Demonstration class to show usage of Student and GraduateStudent.
    """

    # Demonstration
    s = Student('Ali', 20)
    print(s._promote())      
    # ⚠️ Protected methods are technically accessible outside the class
    # but should be avoided in practice (discouraged).
    
    # print(s.__demote())  # ❌ Not possible (private method)
    
    g = GraduateStudent("Sara", 25, "AI in Healthcare")
    print(g.display_info())  # Accessing public & protected data
    print(g.promote())       # Accessing protected method through subclass


# ==========================================================
# 📌 NOTES / DOCUMENTATION
#
# Access Modifiers in Python:
# ----------------------------
# 1. Public (no underscore):
#    - Example: name, get_grade()
#    - Accessible everywhere (inside class, subclasses, outside class).
#
# 2. Protected (single underscore _):
#    - Example: _age, _promote()
#    - Accessible in class and subclasses.
#    - Can still be accessed outside, but discouraged by convention.
#
# 3. Private (double underscore __):
#    - Example: __grade, __demote()
#    - Accessible ONLY inside the class.
#    - Not accessible directly in subclasses or outside.
#    - Python uses "name mangling" → stored as _ClassName__variable.
#
# Example Behavior:
# -----------------
# s = Student("Ali", 20)
# print(s.name)        # ✅ Works (public)
# print(s._age)        # ⚠️ Works but discouraged (protected)
# print(s.get_grade()) # ✅ Correct way to access private
# print(s.__grade)     # ❌ AttributeError (private)
#
# g = GraduateStudent("Sara", 25, "AI in Healthcare")
# print(g.display_info()) # ✅ Works
# print(g.promote())      # ✅ Works (calls protected method from parent)
# print(g.__demote())     # ❌ AttributeError (private)