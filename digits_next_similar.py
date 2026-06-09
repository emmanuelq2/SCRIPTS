

""" Writing a function that takes a positive integer, n, as input and returns the number of times
a digit appears immediately next to an identical digit in the number """

import sys
import unittest
from pathlib import Path

def solution(n):
    # Tracks how many times two neighboring digits are equal (e.g., ...33... counts once).
    count = 0

    while n > 0:
        """ Start n = 1234
        Take right digit: digit = 1234 % 10 = 4
        Shift: n = 1234 // 10 = 123
        Neighbor check uses n % 10 = 3
        
        Next loop:
        digit = 123 % 10 = 3
        n = 123 // 10 = 12
        neighbor is 12 % 10 = 2 """

        # Read the current rightmost digit.
        digit = n % 10
        # Shift right by one digit so the new rightmost digit is the previous neighbor =>  loop compare neighboring digits one pair at a time.
        n = n // 10
        # Compare adjacent digits in the original number: previous rightmost vs its left neighbor.
        if n % 10 == digit:
            count += 1
        
    return count


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="digits_next_similar_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(solution(1234))  # Output: 0
        print(solution(1123))  # Output: 1
        print(solution(1111))  # Output: 3
        print(solution(11122))  # Output: 3
        print(solution(1122))  # Output: 2