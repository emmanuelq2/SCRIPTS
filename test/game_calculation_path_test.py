import unittest
from game_calculating_path import calculatingPath as solution


class SolutionTests(unittest.TestCase):
    def test01(self):
        self.assertEqual(solution([5, 3, 2, 6, 2, 1, 7], 3), [3, -1, 3, 1, 2, 2, 1])

    def test02(self):
        self.assertEqual(solution([2, 4, 2, 1, 3, 2, 8, 4, 7], 4), [-1, -1, -1, -1, -1, -1, 1, -1, 1])

    def test03(self):
        self.assertEqual(solution([1, 1, 1, 1, 1], 1), [-1, -1, -1, -1, -1])

    def test04(self):
        self.assertEqual(solution([8, 1, 6, 2, 4, 7, 3], 7), [1, 2, 1, -1, 1, -1, 1])

    def test05(self):
        self.assertEqual(solution([10, 9, 8, 7, 6, 5], 5), [1, 1, 1, 1, 1, -1])

    def test06(self):
        self.assertEqual(solution([10]*500, 1), [50 - i // 10 for i in range(500)])

    def test07(self):
        self.assertEqual(solution([1]*500, 1), [-1]*500)

    def test08(self):
        self.assertEqual(solution([i for i in range(1, 11)]*2, 10), [5, 4, 5, 3, -1, 4, 3, 2, 2, -1, 4, 3, 2, 2, -1, 1, 1, 1, 1, -1])

    def test09(self):
        self.assertEqual(solution([i for i in range(1, 11)]*2, 1), [-1, 4, 5, 3, 3, 4, 3, 2, 2, 2, -1, 3, 2, 2, 2, 1, 1, 1, 1, 1])

    def test10(self):
        self.assertEqual(solution([10 - i for i in range(10)]*50, 5), [50 - i // 10 if i % 10 != 5 else -1 for i in range(500)])


if __name__ == '__main__':
    unittest.main()