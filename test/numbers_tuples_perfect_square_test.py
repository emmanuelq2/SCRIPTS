import unittest
from numbers_tuples_perfect_squares import adding_numbers_perfect_square as solution

class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        arr1 = [2, 3, 16]
        arr2 = [1, 9, 10]
        expected_output = [(3, 1), (16, 9)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_2(self):
        arr1 = [0]
        arr2 = [0]
        expected_output = [(0, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_3(self):
        arr1 = [4, 13, 23]
        arr2 = [-4, -3, -24]
        expected_output = [(4, -4), (4, -3), (13, -4)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_4(self):
        arr1 = [0, 1, 2, -100, 100]
        arr2 = [-100, 100, 30, 0, -1, -2, -3]
        expected_output = [(0, 100), (0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (-100, 100), (100, -100), (100, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_5(self):
        arr1 = [100, 75, 36, 9, -25, -64, -100]
        arr2 = [-1, 1, 24, 0, -1, -24]
        expected_output = [(100, 0), (36, 0), (9, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_6(self):
        arr1 = []
        arr2 = [1, 2, 3, 4]
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_7(self):
        arr1 = [1, 2, 3, 4]
        arr2 = []
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_8(self):
        arr1 = []
        arr2 = []
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)


if __name__ == "__main__":
    unittest.main()