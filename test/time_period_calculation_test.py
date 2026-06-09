import unittest
from time_period_calculation import time_period_length as solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("00:00:00 - 00:00:01"), 0)

    def test2(self):
        self.assertEqual(solution("00:00:00 - 00:01:00"), 1)

    def test3(self):
        self.assertEqual(solution("00:59:59 - 01:00:00"), 1)

    def test4(self):
        self.assertEqual(solution("00:00:00 - 23:59:59"), 1439)

    def test5(self):
        self.assertEqual(solution("01:05:05 - 16:30:50"), 925)

    def test6(self):
        self.assertEqual(solution("12:15:30 - 14:00:00"), 105)

    def test7(self):
        self.assertEqual(solution("02:45:20 - 06:37:35"), 232)


if __name__ == '__main__':
    unittest.main()
