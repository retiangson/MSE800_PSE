class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def string_length(self):
        return self.text.lenght()
    
    def to_uppercase(self):
        return self.text.upper()

# Create an instance of the StringManipulator class
name = StringManipulator("example")

# Call the find_character method on the object
result = name.find_character('x')
print(result)  # Output: 1

length = name.string_length()
print("Length of string is:", length)  

uppercase_text = name.to_uppercase()
print("Uppercase:", uppercase_text)