import unittest
from mutual_reach_pairs import mutual_digit_sum_pairs as solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution(1, 10), 21)

    def test2(self):
        self.assertEqual(solution(10, 12), 2)

    def test3(self):
        self.assertEqual(solution(1, 100), 711)

    def test4(self):
        self.assertEqual(solution(9, 11), 3)

    def test5(self):
        self.assertEqual(solution(10, 20), 27)


if __name__ == "__main__":
    unittest.main()
