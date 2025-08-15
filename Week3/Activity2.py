class FileReader:
    def __init__(self, filepath, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.file = None

    def open_file(self, mode='r'):
        self.file = open(self.filepath, mode, encoding=self.encoding, errors='replace')

    def count_words(self):
        if self.file and not self.file.closed:
            content = self.file.read()
            words = content.split()
            print(f"Total words: {len(words)}")
        else:
            print("No file is open to read.")

    def close_file(self):
        if self.file and not self.file.closed:
            self.file.close()
            self.file = None


# Usage
if __name__ == "__main__":
    filepath = "D:/Users/retia/OneDrive/Documents/Ron School/MSE800_PSE/Week3/demo_file.txt"

    # Reading
    reader = FileReader(filepath, encoding='utf-8')
    reader.open_file(mode='r')
    reader.count_words()
    reader.close_file()
