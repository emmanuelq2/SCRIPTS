import unittest
from numbers_extraction import numbers_extraction_sum as solution

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"), 18)
        
    def test_2(self):
        self.assertEqual(solution("michael scored 100 points"), 100)
        
    def test_3(self):
        self.assertEqual(solution("lena scored 50 points and lee scored 50 points"), 100)
        
    def test_4(self):
        self.assertEqual(solution("sam scored 25 points, john scored 25 points, jim scored 25 points, and sue scored 25 points"), 100)
        
    def test_5(self):
        self.assertEqual(solution("1 point scored by max"), 1)
        
    def test_6(self):
        self.assertEqual(solution("no points scored in this game"), 0)
        
    def test_7(self):
        self.assertEqual(solution("abc scored 3 points and def scored 9 points then ghi scored 27 points"), 39)
        
    def test_8(self):
        self.assertEqual(solution("game score: pete 2 points, eve 4 points, zane 8 points"), 14)
        
    def test_9(self):
        self.assertEqual(solution("jake scored1point, john scored2points"), 3)
        
    def test_10(self):
        self.assertEqual(solution("this game ended with no score"), 0)


if __name__ == '__main__':
    unittest.main()
