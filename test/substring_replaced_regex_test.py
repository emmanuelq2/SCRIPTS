import unittest
from substring_replaced import replace_substring
from substring_replaced_regex import replace_substring_regex as solution

class ReplaceSubstringTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution("hello world", "world", "friend"), "hello friend")

    def test_2(self):
        self.assertEqual(solution("i love coding", "code", "craft"), "i love coding")

    def test_3(self):
        self.assertEqual(solution("it is a beautiful day", "beautiful", "gloomy"), "it is a gloomy day")

    def test_4(self):
        self.assertEqual(solution("practice makes perfect", "perfect", "better"), "practice makes better")

    def test_5(self):
        self.assertEqual(solution("keep calm and carry on", "carry on", "code on"), "keep calm and code on")

    def test_6(self):
        self.assertEqual(solution("long text long text", "long", "short"), "short text short text")

    def test_7(self):
        self.assertEqual(solution("lower case", "lower", ""), " case")

    def test_8(self):
        self.assertEqual(solution("a quick brown fox jumps over a lazy dog", "jumps", "skips"), "a quick brown fox skips over a lazy dog")

    def test_9(self):
        self.assertEqual(solution("this is a test", "this", "that"), "that is a test")

    def test_10(self):
        self.assertEqual(solution("final test case", "case", "example"), "final test example")

if __name__ == "__main__":
    unittest.main()