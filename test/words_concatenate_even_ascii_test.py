import unittest
from words_concatenate_even_ascii import words_concatenate_even as solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution("Python is a high-level programming language.", 'n'), 
            "hleel"
        )

    def test2(self):
        self.assertEqual(
            solution("Practice makes perfect.", 'f'), 
            "ceec."
        )

    def test3(self):
        self.assertEqual(
            solution("Mastering Advanced Looping and Implementation.", 'l'), 
            "ced"
        )

    def test4(self):
        self.assertEqual(
            solution("I will pass this test!", 'w'), 
            "llssis"
        )

    def test5(self):
        self.assertEqual(
            solution("Participate in exciting challenges.", 'a'), 
            ""
        )

    def test6(self):
        self.assertEqual(
            solution("The quick brown fox jumps over the lazy dog.", 'f'), 
            "e."
        )

    def test7(self):
        self.assertEqual(
            solution("This sentence is a test sentence.", 't'), 
            "isencess"
        )

    def test8(self):
        self.assertEqual(
            solution("This is a long string with lots of characters and words.", 'v'), 
            "issngingthtsfctersds."
        )

    def test9(self):
        self.assertEqual(
            solution("Another sentence to test the function.", 'o'), 
            "ence"
        )

    def test10(self):
        self.assertEqual(
            solution("Some additional variety in test cases.", 'k'), 
            "eiae."
        )

if __name__ == '__main__':
    unittest.main()