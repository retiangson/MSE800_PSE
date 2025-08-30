class Student:
    def __init__(self, name, age): #Private method Accessable only within the class
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self): #Public method Accessable everywhere
        return self.__grade
    

    def _promote(self): #Protected method Accessable only within the class and derived classes
        """Change the student's grade to the next level."""
        self.__demote() #Private Accessable here only, with in class
        if self.__grade == 'A':
            self.__grade = 'A+'   # Example: improve grade
        else:
            self.__grade = 'A'
        return self.__grade

    
    def __demote(self): #Private method Accessable only within the class
        """Change the student's grade to the next level."""
        if self.__grade == 'A':
            self.__grade = 'A-'   # Example: improve grade
        else:
            self.__grade = 'A'
        return self.__grade

# New class that demonstrates using public and protected attributes
class GraduateStudent(Student):
    def __init__(self, name, age, thesis_title):
        super().__init__(name, age)
        self.thesis_title = thesis_title   # additional public attribute

    def display_info(self):
        # Access public and protected attributes
        return f"Graduate Student: {self.name}, Age: {self._age}, Thesis: {self.thesis_title}"
    
    def promote(self):   #Accessing protected method from derive class GraduateStudent
        return self._promote()
    
    #def demote(self):   #Try Access Private class - Not possible
    #    return self.__demote()

class main:
    # Demonstration
    s = Student('Ali', 20)
    print(s._promote())      # method that changes grade in protected level can still be accessable but discourage
    #print(s.__demote()) # Not posible

    g = GraduateStudent("Sara", 25, "AI in Healthcare")
    print(g.display_info()) # demonstrates public & protected usage
    print(g.promote())      # new method that changes grade in protected level
    #print(g.demote())      # new method that changes grade - not possible