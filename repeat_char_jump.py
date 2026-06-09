
""" Write a Python function, repeat_char_jump(inputString, step). 
The function takes two parameters: inputString and step, where inputString is the 
string you are working with, and step is an integer that denotes the number of characters 
to skip with each jump. The value of step ranges from 1 to the length of the input 
string. The function should return a newly formed string consisting of characters 
selected in the order dictated by the jump length step. 
For example, if inputString is "abcdefg" and step is 3, the function should return 
"adgcfbe". This is because after 'a', comes 'd' (3 characters after 'a'), 
followed by 'g' (3 characters after 'd', circling back to the start of the string 
after 'g'), and so on.
"""

import sys
import unittest
from pathlib import Path


def repeat_char_jump(inputString: str, k: int) -> str:
    # Build the output by visiting characters through circular jumps.
    result = ""
    length = len(inputString)
    # Start from the first character (index 0).
    index = 0

    # Repeat exactly 'length' times so we pick that many characters.
    # The underscore _ is a variable name used when you do not need the loop counter value.
    # '_' means the loop counter value is not needed.
    # The stopping condition is not based on index value, but based on iteration count.
    # The loop runs exactly 'length' times because we need to pick that many characters.
    for _ in range(length):
        # Take the current character.
        result += inputString[index]
        # Move forward by k with wrap-around using modulo.
        index = (index + k) % length
    return result

""" Current index	Character picked	Next index calculation	Next index
    1	    0	    a	            (0 + 3) mod 8	            3
    2	    3	    d	            (3 + 3) mod 8	            6
    3	    6	    g	            (6 + 3) mod 8 = 9 mod 8	    1
    4	    1	    b	            (1 + 3) mod 8	            4
    5	    4	    e	            (4 + 3) mod 8	            7 """


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="repeat_char_jump_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()

