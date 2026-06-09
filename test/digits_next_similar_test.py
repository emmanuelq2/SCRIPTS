import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from digits_next_similar import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(113224), 2)

    def test2(self):
        self.assertEqual(solution(33333888), 6)

    def test3(self):
        self.assertEqual(solution(13579), 0)

    def test4(self):
        self.assertEqual(solution(345672), 0)

    def test5(self):
        self.assertEqual(solution(22333555), 5)

    def test6(self):
        self.assertEqual(solution(100000), 4)

    def test7(self):
        self.assertEqual(solution(10), 0)

    def test8(self):
        self.assertEqual(solution(98876), 1)

    def test9(self):
        self.assertEqual(solution(4444), 3)

    def test10(self):
        self.assertEqual(solution(1), 0)


if __name__ == '__main__':
    unittest.main()
