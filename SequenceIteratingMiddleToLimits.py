import sys
import unittest
from pathlib import Path


def iterateMiddleToEnd(numbers):
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        left = mid - 1
        right = mid + 1
        result = [numbers[mid]]
    else:
        left = mid - 1
        right = mid
        result = []

    while left >= 0 and right < len(numbers):
        result.append(numbers[left] * numbers[right])
        left -= 1
        right += 1

    return result


def solution(numbers):
    return iterateMiddleToEnd(numbers)


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="SequenceIteratingMiddleToLimits_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()