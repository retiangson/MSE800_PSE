#Using __init__, you initialize instance variables when creating an object. 
#These variables hold data specific to that instance and can be accessed or modified by the object's methods. 
#This allows each object to maintain its own state independently of other instances.
class StringManipulator:
    def find_character(text, char):
        return text.find(char)
    
    def string_length(text):
        return len(text)
    
    def to_uppercase(text):
        return text.upper()

# Usage:
text = "example"
name = StringManipulator

result = name.find_character(text, 'x')
print(result)  # Output: 1

length = name.string_length(text)
print("Length of string is:", length)

uppercase_text = name.to_uppercase(text)
print("Uppercase:", uppercase_text)

