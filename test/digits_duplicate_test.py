import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from digits_duplicate import digits_duplicate as solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(1234), 11223344)

    def test2(self):
        self.assertEqual(solution(1), 11)

    def test3(self):
        self.assertEqual(solution(22), 2222)

    def test4(self):
        self.assertEqual(solution(9876), 99887766)

    def test5(self):
        self.assertEqual(solution(10000), 1100000000)

    def test6(self):
        self.assertEqual(solution(0), 0)

    def test7(self):
        self.assertEqual(solution(3333), 33333333)

    def test8(self):
        self.assertEqual(solution(4444), 44444444)

    def test9(self):
        self.assertEqual(solution(5555), 55555555)

    def test10(self):
        self.assertEqual(solution(6666), 66666666)


if __name__ == '__main__':
    unittest.main()
