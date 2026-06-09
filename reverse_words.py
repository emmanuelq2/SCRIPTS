import sys
import unittest
from pathlib import Path


def reverse_words(input_str: str) -> str:
    # Split the string into words and rotate each word by moving the last
    # character to the front.
    rotated_words = []

    for word in input_str.split():
        if len(word) <= 1:
            rotated_words.append(word)
        else:
            rotated_words.append(word[-1] + word[:-1])

    return " ".join(rotated_words)


solution = reverse_words


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="reverse_words_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(reverse_words("Hello dear user123"))