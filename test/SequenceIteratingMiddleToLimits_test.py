import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from SequenceIteratingMiddleToLimits import iterateMiddleToEnd as solution


class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [3, 8, 5])

    def test_case2(self):
        self.assertEqual(solution([1, -1, 1, -1, 1, -1]), [-1, -1, -1])

    def test_case3(self):
        self.assertEqual(solution([-100] * 200), [10000] * 100)

    def test_case4(self):
        self.assertEqual(solution([5, -7, 2, -9, 1, -3, 8]), [-9, 2, 21, 40])

    def test_case5(self):
        self.assertEqual(solution([3, 6, 2, 9, -4, -1, 0, 5, 7]), [-4, -9, 0, 30, 21])

    def test_case6(self):
        self.assertEqual(solution([9] * 200), [81] * 100)

    def test_case7(self):
        self.assertEqual(solution([5]), [5])

    def test_case8(self):
        self.assertEqual(solution([0, 0]), [0])


if __name__ == '__main__':
    unittest.main()
