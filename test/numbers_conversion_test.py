import unittest
from numbers_conversion import swap_letter_number_tokens as solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution("1-2-3-4-5"), "a-b-c-d-e")

    def test2(self):
        self.assertEqual(solution("a-b-c"), "1-2-3")

    def test3(self):
        self.assertEqual(solution("1-a-3-c-5"), "a-1-c-3-e")

    def test4(self):
        self.assertEqual(solution("z-y-x-w-v"), "26-25-24-23-22")

    def test5(self):
        self.assertEqual(solution("a-26-b-25-c-24"), "1-z-2-y-3-x")

    def test6(self):
        self.assertEqual(solution("13-9-14-15"), "m-i-n-o")

    def test7(self):
        self.assertEqual(solution("12-1-18-9-1"), "l-a-r-i-a")

    def test8(self):
        self.assertEqual(solution("19-15-12-21-20-9-15-14"), "s-o-l-u-t-i-o-n")

    def test9(self):
        self.assertEqual(solution("a-b-c-1-2-3-x-y-z-24-25-26"), "1-2-3-a-b-c-24-25-26-x-y-z")

    def test10(self):
        self.assertEqual(solution("16-9-20-8-15-14-3-8-1-18-13-1"), "p-i-t-h-o-n-c-h-a-r-m-a")


if __name__ == "__main__":
    unittest.main()
