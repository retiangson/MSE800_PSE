class SentenceCheck:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        words = self.sentence.strip().split()
        return len(words)

def main():
    sentence = input("Enter a sentence: ")
    check = SentenceCheck(sentence)
    count = check.count_words()
    print(f"Number of words is: {count}")

if __name__ == "__main__":
    main()