import unittest
from consecutive_characters_from_the_end import consecutive_inverted_characters as solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("aaabbcccdde"), [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)])

    def test2(self):
        self.assertEqual(solution("aaaaaaaZ"), [('Z', 1), ('a', 7)])

    def test3(self):
        self.assertEqual(solution("a"), [('a', 1)])

    def test4(self):
        self.assertEqual(solution("abc12321cba"), [('a', 1), ('b', 1), ('c', 1), ('1', 1), ('2', 1), ('3', 1), ('2', 1), ('1', 1), ('c', 1), ('b', 1), ('a', 1)])

    def test5(self):
        self.assertEqual(solution("123454321"), [('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('4', 1), ('3', 1), ('2', 1), ('1', 1)])

    def test6(self):
        self.assertEqual(solution("ABBA"), [('A', 1), ('B', 2), ('A', 1)])

    def test7(self):
        self.assertEqual(solution("Radar"), [('r', 1), ('a', 1), ('d', 1), ('a', 1), ('R', 1)])

    def test8(self):
        self.assertEqual(solution("$$$$$"), [('$', 5)])

    def test9(self):
        self.assertEqual(solution("Rotor"), [('r', 1), ('o', 1), ('t', 1), ('o', 1), ('R', 1)])

    def test10(self):
        self.assertEqual(
            solution("Red roses run no risk, sir, on Nurse's order"),
            [('r', 1), ('e', 1), ('d', 1), ('r', 1), ('o', 1), (' ', 1), ('s', 1), ("'", 1), ('e', 1), ('s', 1), ('r', 1), ('u', 1), ('N', 1), (' ', 1), ('n', 1), ('o', 1), (' ', 1), (',', 1), ('r', 1), ('i', 1), ('s', 1), (' ', 1), (',', 1), ('k', 1), ('s', 1), ('i', 1), ('r', 1), (' ', 1), ('o', 1), ('n', 1), (' ', 1), ('n', 1), ('u', 1), ('r', 1), (' ', 1), ('s', 1), ('e', 1), ('s', 1), ('o', 1), ('r', 1), (' ', 1), ('d', 1), ('e', 1), ('R', 1)]
        )


if __name__ == '__main__':
    unittest.main()
