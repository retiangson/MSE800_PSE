class FileReader:
    def __init__(self, filepath, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.file = None

    def open_file(self, mode='r'):
        self.file = open(self.filepath, mode, encoding=self.encoding, errors='replace')


    def read_lines(self):
        if self.file and not self.file.closed:
            for line in self.file:
                print(line[0:-1])
        else:
            print("No file is open to read.")

    def write_lines(self, text):
        if self.file and not self.file.closed:
            self.file.write(text + "\n")
        else:
            print("No file is open for writing.")

    def close_file(self):
        if self.file and not self.file.closed:
            self.file.close()
            self.file = None


# Usage
if __name__ == "__main__":
    filepath = "Week3/demo_file.txt"

    # Reading
    reader = FileReader(filepath, encoding='utf-8')
    reader.open_file(mode='r')
    reader.read_lines()
    reader.close_file()

    # Writing
    writer = FileReader(filepath, encoding='utf-8')
    writer.open_file(mode='a')  # append mode to avoid overwriting
    user_input = input("Enter word to append: ")
    writer.write_lines(user_input)
    writer.close_file()

    # Reading
    reader = FileReader(filepath, encoding='utf-8')
    reader.open_file(mode='r')
    reader.read_lines()
    reader.close_file()
