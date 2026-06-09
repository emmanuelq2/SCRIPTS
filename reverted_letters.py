import sys
import unittest
from pathlib import Path


def inverted_letter(input_str: str) -> str:
    # Build a list of transformed words.
    transformed_words = []

    # Split input by whitespace so each word is processed independently.
    for word in input_str.split():
        # Collect converted characters for the current word.
        transformed_chars = []

        # Convert every character using the opposite-alphabet rule.
        for char in word:
            # Lowercase mapping: a <-> z, b <-> y, ..., m <-> n.
            if "a" <= char <= "z":
                transformed_chars.append(chr(ord("z") - (ord(char) - ord("a"))))
            # Uppercase mapping: A <-> Z, B <-> Y, ..., M <-> N.
            elif "A" <= char <= "Z":
                transformed_chars.append(chr(ord("Z") - (ord(char) - ord("A"))))
            else:
                # Keep non-letter characters unchanged.
                transformed_chars.append(char)

        # Rebuild the transformed word from its converted characters.
        transformed_words.append("".join(transformed_chars))

    # Move the last transformed word to the front.
    if not transformed_words:
        return ""

    ordered_words = [transformed_words[-1]] + transformed_words[:-1]
    return " ".join(ordered_words)

solution = inverted_letter


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="reverted_letters_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(inverted_letter("CapitaL letters"))  # ovggvih XzkrgzO
        print(inverted_letter("Hello World! Are you good?"))