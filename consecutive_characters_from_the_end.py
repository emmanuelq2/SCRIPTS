import sys
import unittest
from pathlib import Path


def consecutive_inverted_characters(s):
    groups: list[tuple[str, int]] = []
    current_group_char: str | None = None
    current_group_length = 0
    s = s[::-1]
    
    for char in s:
        # Ignore non-alphanumeric characters.
        # if char.isdigit() or char.isalpha():
            # Extend the current run if the character is the same.
        if char == current_group_char:
            current_group_length += 1
        else:
            # Save the previous run before starting a new one.
            if current_group_char is not None:
                groups.append((current_group_char, current_group_length))
            # Start tracking a new character run.
            current_group_char = char
            current_group_length = 1
    
    # Add the last run after the loop ends.
    if current_group_char is not None:
        groups.append((current_group_char, current_group_length))
    
    # Return all consecutive groups as tuples.
    return groups


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="consecutive_characters_from_the_end_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()