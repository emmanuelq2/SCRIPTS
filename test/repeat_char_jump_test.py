import unittest
from repeat_char_jump import repeat_char_jump as solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("abcdefg", 3), "adgcfbe")

    def test2(self):
        self.assertEqual(solution("a", 1), "a")

    def test3(self):
        self.assertEqual(solution("av", 1), "av")

    def test4(self):
        self.assertEqual(solution("cgldxdv", 4), "cxgdlvd")

    def test5(self):
        self.assertEqual(solution("z", 1), "z")

    def test6(self):
        self.assertEqual(solution("aaa", 2), "aaa")

    def test7(self):
        self.assertEqual(solution("zyxwvutsrqponmlkjihgfedcba", 5), "zupkfavqlgbwrmhcxsnidytoje")

    def test8(self):
        self.assertEqual(solution("zyxwvutsrqponmlkjihgfedcba", 15), "zkvgrcnyjufqbmxitepalwhsdo")

    def test9(self):
        self.assertEqual(solution("abcdefghij", 1), "abcdefghij")

    def test10(self):
        self.assertEqual(solution("abcdefghij", 9), "ajihgfedcb")


if __name__ == "__main__":
    unittest.main()
