import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from reverted_letters import inverted_letter as solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("Hello"), "Svool")

    def test2(self):
        self.assertEqual(solution("ABC"), "ZYX")

    def test3(self):
        self.assertEqual(solution("abc"), "zyx")

    def test4(self):
        self.assertEqual(solution("A quick brown FOX jumps over the lazy DOG"), "WLT Z jfrxp yildm ULC qfnkh levi gsv ozab")

    def test5(self):
        self.assertEqual(solution("Zebra"), "Avyiz")

    def test6(self):
        self.assertEqual(solution("CapitaL letters"), "ovggvih XzkrgzO")

    def test7(self):
        self.assertEqual(solution("loWer letters"), "ovggvih olDvi")

    def test8(self):
        self.assertEqual(solution("OPPOSITE letters"), "ovggvih LKKLHRGV")

    def test9(self):
        self.assertEqual(solution("An apple a day keeps the doctor away"), "zdzb Zm zkkov z wzb pvvkh gsv wlxgli")

    def test10(self):
        self.assertEqual(solution("m n"), "m n")


if __name__ == '__main__':
    unittest.main()
