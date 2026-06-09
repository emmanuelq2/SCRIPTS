import unittest
from tuples_middle_pairs import middle_pairs as solution


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [(3, 0), (2, 4), (1, 5)])

    def test2(self):
        self.assertEqual(solution([1, 2, 3, 4]), [(2, 3), (1, 4)])

    def test3(self):
        self.assertEqual(solution([1000, -1000, 500, -500, 250, -250]), [(500, -500), (-1000, 250), (1000, -250)])

    def test4(self):
        self.assertEqual(solution([7, 3, 5, 7, 8, 2, 0, -1, -4, 10]), [(8, 2), (7, 0), (5, -1), (3, -4), (7, 10)])

    def test5(self):
        self.assertEqual(solution([6, 4, 1, -2, -5, -8, 9, 11, -50]), [(-5, 0), (-2, -8), (1, 9), (4, 11), (6, -50)])

    def test6(self):
        self.assertEqual(solution([-999, 999, -500, 500, -250, 250, -100, 100]), [(500, -250), (-500, 250), (999, -100), (-999, 100)])

    def test7(self):
        self.assertEqual(solution([-1000, -1000, 1000, 0, 1000, -1000, -1000]), [(0, 0), (1000, 1000), (-1000, -1000), (-1000, -1000)])


if __name__ == "__main__":
    unittest.main()
