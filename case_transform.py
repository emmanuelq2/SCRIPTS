"""Write a Python function that transforms each word so that:

    If the word starts with a letter, make the first character uppercase and make the rest lowercase.
    If the word starts with a non-letter character, leave that first character unchanged and make the rest lowercase.
"""

import sys
import unittest
from pathlib import Path

def case_transform(input_str: str) -> str:
    words = input_str.split()
    transformed_words = []

    for word in words:
        if word[0].isalpha():
            transformed_words.append(word.capitalize())
        else:
            transformed_words.append(word[0] + word[1:].lower())

    return " ".join(transformed_words)


solution = case_transform


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="case_transform_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
