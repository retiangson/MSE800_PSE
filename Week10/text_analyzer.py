"""
Text Analyzer Module

This module defines a class for analyzing user-provided text.
It calculates:
1. Total length of the text.
2. Number of uppercase characters.
3. Number of digits.
4. Number of special characters.
"""

from typing import Dict

class TextAnalyzer:
    """
    A class to analyze text input for length, uppercase, digits,
    and special character counts.
    """

    def __init__(self, text: str) -> None:
        """
        Initialize the TextAnalyzer with the given text.

        Args:
            text (str): The input text to analyze.

        Raises:
            TypeError: If input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        self.text = text

    def calculate_length(self) -> int:
        """
        Calculate the total length of the input text.

        Returns:
            int: The length of the text.
        """
        return len(self.text)

    def count_uppercase(self) -> int:
        """
        Count the number of uppercase characters in the input text.

        Returns:
            int: Number of uppercase letters.
        """
        return sum(1 for char in self.text if char.isupper())

    def count_digits(self) -> int:
        """
        Count the number of digits in the input text.

        Returns:
            int: Number of digit characters.
        """
        return sum(1 for char in self.text if char.isdigit())

    def count_special_characters(self) -> int:
        """
        Count the number of special (non-alphanumeric) characters in the input text.

        Returns:
            int: Number of special characters.
        """
        return sum(1 for char in self.text if not char.isalnum() and not char.isspace())

    def analyze(self) -> Dict[str, int]:
        """
        Perform a complete analysis of the text.

        Returns:
            Dict[str, int]: A dictionary containing analysis results.
        """
        return {
            "total_length": self.calculate_length(),
            "uppercase_count": self.count_uppercase(),
            "digit_count": self.count_digits(),
            "special_character_count": self.count_special_characters(),
        }

def main() -> None:
    """
    Entry point for running the Text Analyzer interactively.
    """
    print("=== TEXT ANALYZER ===")
    user_input = input("Enter a word or sentence: ").strip()

    analyzer = TextAnalyzer(user_input)
    results = analyzer.analyze()

    print("\n=== ANALYSIS RESULT ===")
    print(f"Input: {user_input}")
    print(f"Total Length: {results['total_length']}")
    print(f"Uppercase Count: {results['uppercase_count']}")
    print(f"Digit Count: {results['digit_count']}")
    print(f"Special Character Count: {results['special_character_count']}")

if __name__ == "__main__":
    main()