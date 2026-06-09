import unittest
from reverse_words import reverse_words as solution


class SolutionTests(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(solution("abc 123 def ghi"), "cab 312 fde igh")

    def test_input_2(self):
        self.assertEqual(solution("bat"), "tba")

    def test_input_3(self):
        self.assertEqual(solution("raceCar"), "rraceCa")

    def test_input_4(self):
        self.assertEqual(solution("mAnGo666 TaCo123i"), "6mAnGo66 iTaCo123")

    def test_input_5(self):
        self.assertEqual(solution("_ab 77Y UwF88"), "b_a Y77 8UwF8")

    def test_input_6(self):
        self.assertEqual(solution("SingleWord"), "dSingleWor")

    def test_input_7(self):
        self.assertEqual(solution("abcdefghij"), "jabcdefghi")
        
    def test_input_8(self):
        self.assertEqual(solution("ZzZzZzZ 1234567890 zYxWvUtS"), "ZZzZzZz 0123456789 SzYxWvUt")


if __name__ == "__main__":
    unittest.main()
