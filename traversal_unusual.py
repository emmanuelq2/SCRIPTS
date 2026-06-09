"""
Diagram of the traversal rule with [1, 2, 3, 4, 5, 6, 7]:

Indexes:  0  1  2  3  4  5  6
Values:   1  2  3  4  5  6  7
                   ^
                middle

Indexes:    0  1  2  3  4  5
Values:     1  2  3  4  5  6
                  ^
                middle

Visit order:
1. Start with the middle element:                [4]
2. Take up to 2 values on the left of middle:    [2, 3]
3. Take up to 2 values on the right of middle:   [5, 6]
4. Take remaining values on the left:            [1]
5. Take remaining values on the right:           [7]

Final result:
[4, 2, 3, 5, 6, 1, 7]
"""

import sys
import unittest
from pathlib import Path

def unusual_traversal(numbers):
    if not numbers:
        return []

    # Step 1: measure the array and locate its middle element.
    n = len(numbers)
    mid = n // 2   # [9, 8, 7, 4, 2, 1] => 3 (index of 4)

    # Step 2: start the result with the middle value.
    result = [numbers[mid]]  # [9, 8, 7, 4, 2, 1] => 4 

    # Step 3: place one pointer just left of the middle
    # and one pointer just right of the middle.
    left = mid - 1  # [9, 8, 7, 4, 2, 1] => 2 (index of 7)
    right = mid + 1  # [9, 8, 7, 4, 2, 1] => 4 (index of 2)

    # Step 4: keep taking values until both sides are exhausted.
    while left >= 0 or right < n:
        # Enter while loop
        # Check left condition
        # Run left block and update left
        # Then continue to the next statement, which is the right if block
        # Check right condition
        # Run right block if true
        # End of loop body
        # Go back to while condition for next iteration
        # Take up to 2 elements from the left side.
        if left >= 0:
            # Step 5: compute the left block boundary.
            start = max(0, left - 1) # [9, 8, 7, 4, 2, 1] => 1 (index of 8)
            # Step 6: append the left block in normal order.
            result.extend(numbers[start:left + 1]) # [9, 8, 7, 4, 2, 1] => append [8, 7]
            # Step 6.5: result is now [4, 8, 7
            # Step 7: move the left pointer past the used values.
            left = start - 1

        # Take up to 2 elements from the right side.
        if right < n:
            # Step 8: compute the right block boundary.
            end = min(n, right + 2) # [9, 8, 7, 4, 2, 1] => 6 (index of 1)
            # Step 9: append the right block in normal order.
            result.extend(numbers[right:end])   # [9, 8, 7, 4, 2, 1] => append [2, 1]
            # Step 10: move the right pointer past the used values.
            right = end

    # Step 11: return the traversal order.
    return result


def run_tests():
    test_dir = Path(__file__).resolve().parent / "test"
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="traversal_unusual_test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print(unusual_traversal([1, 2, 3, 4, 5, 6, 7]))  # Output: [4, 2, 3, 5, 6, 1, 7]
        print(unusual_traversal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Output: [6, 4, 5, 7, 8, 2, 3, 9, 10, 1, 11]
        print(unusual_traversal([10, 20, 30, 40, 50]))  # Output: [30, 10, 20, 40, 50]
        print(unusual_traversal([5]))  # Output: [5]
        print(unusual_traversal([9, 8, 7, 4, 2, 1]))  # Output: [4, 8, 7, 2, 1, 9]
        print(unusual_traversal([]))  # Output: []