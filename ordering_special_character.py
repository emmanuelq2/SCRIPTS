import sys
import unittest
from pathlib import Path


def special_order(inputString: str) -> str:
    result = ""
    length = len(inputString)
    mid = length // 2

    # Step 1: take characters from the end down to the middle.
    for i in range(length - 1, mid - 1, -1):
        result += inputString[i]

    # Step 2: append characters from the start up to the middle.
    for i in range(0, mid):
        result += inputString[i]

    return result


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="ordering_special_character_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(special_order("Hello my friend!"))
        print(special_order("Python is great"))
        print(special_order("abcdefg"))
        print(special_order("1234567890"))