class LibraryItem:
    """Base class for all library items. Uses encapsulation to protect data."""

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Setters
    def set_title(self, title):
        if title.strip():
            self.__title = title
        else:
            print("Title cannot be empty.")

    def set_author(self, author):
        if author.strip():
            self.__author = author
        else:
            print("Author cannot be empty.")

    def display_details(self):
        """Placeholder method to be overridden."""
        print(f"Title: {self.__title}, Author: {self.__author}")


class Book(LibraryItem):
    """Represents a book. Inherits from LibraryItem."""

    def __init__(self, title, author):
        super().__init__(title, author)

    def display_details(self):
        print(f"Book - Title: {self.get_title()}, Author: {self.get_author()}")


class Magazine(LibraryItem):
    """Represents a magazine. Adds issue frequency."""

    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.__issue_frequency = issue_frequency

    def get_issue_frequency(self):
        return self.__issue_frequency

    def set_issue_frequency(self, frequency):
        valid_frequencies = ["Daily", "Weekly", "Monthly", "Quarterly"]
        if frequency in valid_frequencies:
            self.__issue_frequency = frequency
        else:
            print(f"Invalid frequency. Choose from: {valid_frequencies}")

    def display_details(self):
        print(f"Magazine - Title: {self.get_title()}, Author: {self.get_author()}, "
              f"Issue Frequency: {self.__issue_frequency}")


class Library:
    """Manages a collection of library items."""

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print(f"Added: '{item.get_title()}'")
        else:
            print("Cannot add: Not a valid library item.")

    def remove_item(self, title):
        found = False
        for item in self.__items:
            if item.get_title().lower() == title.lower():
                self.__items.remove(item)
                print(f"Removed: '{title}'")
                found = True
                break
        if not found:
            print(f"Item titled '{title}' not found.")

    def display_all_items(self):
        if not self.__items:
            print("The library is currently empty.")
        else:
            print("\nAll Library Items:")
            print("-" * 60)
            for item in self.__items:
                item.display_details()
            print("-" * 60)


# === Main Program with Interactive Menu ===
def main():
    # Create a library instance
    library = Library()

    while True:
        print("\n" + "="*50)
        print("   🏛️  CITY LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add a Book")
        print("2. Add a Magazine")
        print("3. Remove an Item by Title")
        print("4. Display All Items")
        print("5. Exit")
        print("-"*50)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            if title and author:
                book = Book(title, author)
                library.add_item(book)
            else:
                print("Title and author cannot be empty.")

        elif choice == '2':
            title = input("Enter magazine title: ").strip()
            author = input("Enter publisher/author: ").strip()
            freq = input("Enter issue frequency (Daily, Weekly, Monthly, Quarterly): ").strip().capitalize()
            if title and author and freq:
                magazine = Magazine(title, author, freq)
                library.add_item(magazine)
            else:
                print("All fields are required.")

        elif choice == '3':
            title = input("Enter title of the item to remove: ").strip()
            if title:
                library.remove_item(title)
            else:
                print("Title cannot be empty.")

        elif choice == '4':
            library.display_all_items()

        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            break  # Exit the infinite loop

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()