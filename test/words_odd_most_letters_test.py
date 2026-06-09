import unittest
from words_odd_most_letters import words_odd_most_letters as solution

class TestSolution(unittest.TestCase):

    def test1(self):
        # In the given sentence, the words "a", "programming" have an odd number of characters. 
        # The most frequently occurring character in "a", "programming" are "a" and "r" respectively.
        self.assertEqual(solution("Python is a high-level programming language"), "ar")

    def test2(self):
        # In the given sentence, the words "Mastering", "Looping", and "and" have an odd number of characters. 
        # The most frequently occurring character in "Mastering", "Looping", and "and" are "m", "o", and "a" respectively.
        self.assertEqual(solution("Mastering Advanced Looping and Implementation"), "moa")

    def test3(self):
        # In the given sentence, the word "loops" has an odd number of characters. 
        # The most frequently occurring character in "loops" is "o".
        self.assertEqual(solution("nested loops"), "o")

    def test4(self):
        # In the given sentence, the word "a" has an odd number of characters. 
        # The most frequently occurring character is "a" in "a".
        self.assertEqual(solution("Python provides us with a built-in"), "a")

    def test5(self):
        # In the given sentence, the words "navigated", "through" have odd number of characters.
        # The most frequently occurring character in "navigated" is "a" and in "through" is "h".
        self.assertEqual(solution("Bravo! You've just successfully navigated through"), "ah")

    def test6(self):
        # In the given sentence, the words "use", "knowledge", "a", "exploration", "loops" have odd number of characters. 
        # The most frequently occurring character in these words are "u", "e", "a", "o", "o" respectively.
        self.assertEqual(solution("Now, use this knowledge as a foundation in your exploration of nested loops"), "ueaoo")

    def test7(self):
        # In the given sentence, the words "Isn't", "fascinating" have odd number of characters. 
        # The most frequently occurring character in these words are "i" and "a" respectively.
        self.assertEqual(solution("Isn't it fascinating"), "ia")

    def test8(self):
        # The input string is a single word with an even number of characters, so the result is "".
        self.assertEqual(solution("Python"), "")

    def test9(self):
        # The input string is a single character string, so the result "a".
        self.assertEqual(solution("a"), "a")

    def test10(self):
        # The input string is a single word with an even number of characters, so the result is "".
        self.assertEqual(solution("high-level"), "") 

if __name__ == "__main__":
    unittest.main()