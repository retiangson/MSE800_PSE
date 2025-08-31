Object-oriented programming principles, control flow, and user interaction.

The purpose and function of each part.

---

## 1. File Structure and Entry Point

```python
if __name__ == "__main__":
    main()
```

### Explanation:
- `__name__` is a built-in Python variable.
- When a Python file is run directly (not imported), `__name__` is set to `"__main__"`.
- This condition ensures that the `main()` function only runs if this script is executed directly.
- If this file is imported into another program, the menu will not start automatically.

**Purpose:** Allows the code to be both executable and reusable as a module.

---

## 2. Class: `LibraryItem` — The Base Class

```python
class LibraryItem:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
```

### Key Syntax Elements:

| Element | Description |
|--------|-------------|
| `class LibraryItem:` | Defines a new class named `LibraryItem`. Follows PascalCase naming convention. |
| `__init__(self, title, author)` | Constructor method. Called automatically when creating a new instance. |
| `self` | Reference to the current object. Required as the first parameter in all instance methods. |
| `self.__title`, `self.__author` | Private attributes due to the double underscore prefix (`__`). This implements **encapsulation** — these variables cannot be accessed directly from outside the class. |

### Encapsulation via Getters and Setters

```python
def get_title(self):
    return self.__title

def set_title(self, title):
    if title.strip():
        self.__title = title
    else:
        print("Title cannot be empty.")
```

- These methods provide **controlled access** to private data.
- Direct access like `item.__title` is blocked by name mangling.
- Users must use `get_title()` and `set_title()` to interact with the data.
- The setter includes validation to prevent invalid input.

This demonstrates **data protection** and **encapsulation**, core principles of OOP.

---

## 3. Inheritance: `Book` and `Magazine` Classes

### Class `Book`

```python
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    def display_details(self):
        print(f"Book - Title: {self.get_title()}, Author: {self.get_author()}")
```

#### Concepts Demonstrated:

| Feature | Description |
|--------|-------------|
| `class Book(LibraryItem)` | `Book` inherits from `LibraryItem`. It automatically gains all attributes and methods of the parent. |
| `super().__init__()` | Calls the constructor of the parent class. Reuses initialization logic without duplicating code. |
| Method overriding | `display_details()` is redefined in `Book` to show a custom format. This is **polymorphism**. |

---

### Class `Magazine`

```python
class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.__issue_frequency = issue_frequency
```

#### Additional Features:

| Feature | Description |
|--------|-------------|
| New attribute | `__issue_frequency` is specific to magazines (e.g., "Monthly"). |
| Private variable | Like other fields, it is private and protected from direct access. |
| Validation in setter | The `set_issue_frequency` method checks that the input is one of the allowed values. |

```python
def set_issue_frequency(self, frequency):
    valid_frequencies = ["Daily", "Weekly", "Monthly", "Quarterly"]
    if frequency in valid_frequencies:
        self.__issue_frequency = frequency
    else:
        print("Invalid frequency. Use: Daily, Weekly, Monthly, Quarterly.")
```

This shows how **encapsulation supports data integrity** by validating changes before applying them.

---

## 4. Class: `Library` — Managing the Collection

```python
class Library:
    def __init__(self):
        self.__items = []
```

### Core Concepts:

| Feature | Description |
|--------|-------------|
| `self.__items = []` | A private list that stores all library items. This is an example of **encapsulation** — the internal state is hidden. |
| Polymorphic storage | The list can hold both `Book` and `Magazine` objects because they are subclasses of `LibraryItem`. |
| `isinstance(item, LibraryItem)` | Ensures only valid items are added. Prevents type errors. |

### Key Methods:

#### `add_item(self, item)`
```python
if isinstance(item, LibraryItem):
    self.__items.append(item)
```
- Type-safe addition.
- Only accepts objects that are instances of `LibraryItem` or its subclasses.

#### `remove_item(self, title)`
```python
for item in self.__items:
    if item.get_title().lower() == title.lower():
        self.__items.remove(item)
        break
```
- Performs a case-insensitive search.
- Removes the first matching item.
- Uses getter method to access the title.

#### `display_all_items(self)`
```python
for item in self.__items:
    item.display_details()
```
- This is a **polymorphic method call**.
- Depending on the actual object type (`Book` or `Magazine`), the correct version of `display_details()` is executed.
- Demonstrates **runtime polymorphism**.

---

## 5. Main Function: Infinite Loop Menu

```python
def main():
    library = Library()

    while True:
        print("\n" + "="*50)
        print("       CITY LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add a Book")
        print("2. Add a Magazine")
        print("3. Remove an Item by Title")
        print("4. Display All Items")
        print("5. Exit")
        print("-"*50)

        choice = input("Enter your choice (1-5): ").strip()
```

### Key Programming Concepts:

| Concept | Description |
|--------|-------------|
| `while True:` | Creates an infinite loop. The program continues running until the user chooses to exit. |
| `break` | Exits the loop when the user selects option 5. Without this, the loop would never terminate. |
| `.strip()` | Removes leading and trailing whitespace from user input to avoid matching errors. |
| Input validation | Before creating objects, the program checks that required fields are not empty. |
| Menu-driven interface | Provides a clear, structured way for users to interact with the system. |

### Control Flow Summary:
1. Display menu
2. Get user choice
3. Perform action based on choice
4. Repeat until exit

This pattern is widely used in command-line applications such as banking systems, inventory tools, and administrative dashboards.

---

## 6. Summary of OOP Principles Applied

| Principle | How It Is Used |
|---------|----------------|
| **Encapsulation** | All data attributes are private (`__title`, `__author`, `__items`). Access is controlled through public methods (getters/setters). |
| **Inheritance** | `Book` and `Magazine` inherit common properties from `LibraryItem`, reducing redundancy and promoting code reuse. |
| **Polymorphism** | The `display_details()` method behaves differently depending on the object type. The same method call produces different outputs. |
| **Abstraction** | Users interact with high-level methods like `add_item()` and `display_all_items()` without needing to know how the internal list works. |
