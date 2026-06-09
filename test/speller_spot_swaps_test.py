import unittest
from speller_spot_swaps import spot_swaps as solution

class SpotSwapsTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("hello", "hlelo"), [(1, 'e', 'l')])

    def test2(self):
        self.assertEqual(solution("abcdef", "abcfed"), [])

    def test3(self):
        self.assertEqual(solution("goodbye", "godobye"), [(2, 'o', 'd')])

    def test4(self):
        self.assertEqual(solution("firsttest", "firtestst"), [])

    def test5(self):
        self.assertEqual(solution("pythonista", "pyhtonista"), [(2, 't', 'h')])

    def test6(self):
        self.assertEqual(solution("qwertyuiop", "qewrtyuiop"), [(1, 'w', 'e')])

    def test7(self):
        self.assertEqual(solution("hellothereworld", "helotlehreworld"), [(6, 'h', 'e')])

if __name__ == "__main__":
    unittest.main()