"""Implement a function that duplicates every digit in a given non-negative integer number, n.
For example, if n equals 1234, the function should return 11223344 """

import sys
import unittest
from pathlib import Path


'''
Full walkthrough for 1234:

Start:

n = 1234
reversed_n = 0
place = 1
First loop:

digit = 4
duplicated_digit = 44
reversed_n = 0 + 44 × 1 = 44
place = 100
n = 123
Second loop:

digit = 3
duplicated_digit = 33
reversed_n = 44 + 33 × 100 = 3344
place = 10000
n = 12
Third loop:

digit = 2
duplicated_digit = 22
reversed_n = 3344 + 22 × 10000 = 223344
place = 1000000
n = 1
Fourth loop:

digit = 1
duplicated_digit = 11
reversed_n = 223344 + 11 × 1000000 = 11223344
place = 100000000
n = 0
Loop stops, function returns:
11223344

Why the result is correct even though digits are read from right to left

The code reads digits from the end of the number first:
4, then 3, then 2, then 1

If n is 0, the loop does not run, and the function returns 0.
That is usually acceptable for integers, because 00 and 0 are the same numeric value.

In short, this function uses arithmetic only:

% 10 to read the last digit
// 10 to remove the last digit
× 10 + digit to duplicate a digit
place *= 100 to position each duplicated pair correctly
'''

def digits_duplicate(n: int) -> int:
    reversed_n = 0
    place = 1
    while n > 0:
        # This gets the last digit of n: if n is 1234, then digit will be 4
        digit = n % 10
        # This creates the doubled version of that digit. For example, if digit is 4, then duplicated_digit will be (4 * 10) + 4 = 44
        duplicated_digit = (digit * 10) + digit
        # This puts the duplicated digit into the correct position inside the final number.
        reversed_n += duplicated_digit * place
        place *= 100  # This shifts the placement by 2 decimal positions for the next duplicated pair. Because each digit becomes two digits: for example, if the next digit is 3, then duplicated_digit will be 33, which takes up two decimal places.
        n = n // 10   # This removes the last digit from n.
        
    return reversed_n


solution = digits_duplicate


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="digits_duplicate_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()