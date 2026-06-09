import unittest
from ordering_special_character import special_order as solution


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution("abcde"), "edcab")

    def test_case_2(self):
        self.assertEqual(solution("abcdef"), "fedabc")

    def test_case_3(self):
        self.assertEqual(solution("a"), "a")

    def test_case_4(self):
        self.assertEqual(solution("zyxwvutsrqpon"), "nopqrstzyxwvu")

    def test_case_5(self):
        self.assertEqual(solution("abcddcba"), "abcdabcd")

    def test_case_6(self):
        self.assertEqual(
            solution("abcdefghijklmnopqrstuvwxyz" * 4 + "abcd"),
            "dcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab"
        )


if __name__ == '__main__':
    unittest.main()
