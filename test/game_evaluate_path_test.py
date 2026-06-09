import unittest
from game_evaluate_path import evaluatePath as solution

class EvaluatePathTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([2, 1, -3, 4]), (2, 1))

    def test2(self):
        self.assertEqual(solution([0]), (0, 0))

    def test3(self):
        self.assertEqual(solution([3, 4, 1, 1, -3, 1]), (4, 5))

    def test4(self):
        self.assertEqual(solution([3, -3]), (0, 0))

    def test5(self):
        self.assertEqual(solution([3, 2, -1, 2, 2, -1, 4]), (1, 7))

    def test6(self):
        self.assertEqual(solution([1]*500), (0, 998))    

if __name__ == '__main__':
    unittest.main()