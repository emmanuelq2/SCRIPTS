import sys
import unittest
from pathlib import Path


def middle_pairs(numbers):
    # Step 1: count how many elements are in the input list.
    n = len(numbers)    #  [10,20,30,40,50,60] => 6 
    # Step 2: prepare an empty list where we will store tuple pairs.
    result = []
    mid = n // 2   # [10,20,30,40,50,60] => 3 (index of 40)
    # Step 3: check whether the length is odd.
    if n % 2 == 1:  # ood numbers
        # Step 3a: find the middle index.
        # Step 3b: for odd length, pair the middle value with 0 first.
        result.append((numbers[mid], 0))
        # Step 3c: set pointers to the neighbors around the middle.
        left = mid - 1      # [10,20,30,40,50,60] => 2 (index of 30)
        right = mid + 1     # [10,20,30,40,50,60] => 4 (index of 50)
    else:  # even numbers
        # Step 3d: for even length, start from the two middle indices.
        left = mid - 1     # [10,20,30,40,50,60] => 2 (index of 30)  
        right = mid         # [10,20,30,40,50,60] => 3 (index of 40)

    # Step 4: move outward from the center and create pairs.
    while left >= 0 and right < n:
        # Pair current left and right values and add to result.
        result.append((numbers[left], numbers[right]))
        # Move one step farther from the center on both sides.
        left -= 1
        right += 1

    # Step 5: return the final list of tuples.
    return result


solution = middle_pairs


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="tuples_middle_pairs_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(middle_pairs([1, 2, 3, 4, 5]))  # Output: [(3, 0), (2, 4), (1, 5)]
        print(middle_pairs([1, 2, 3, 4]))     # Output: [(2, 3), (1, 4)]
        print(middle_pairs([10, 20, 30, 40, 50, 60]))  # Output: [(30, 40), (20, 50), (10, 60)]
        print(middle_pairs([7]))  # Output: [(7, 0)]
        print(middle_pairs([1, 2]))  # Output: [(1, 2)]
