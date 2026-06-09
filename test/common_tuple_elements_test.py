import unittest
from common_tuple_elements import common_tuple_elements_traversing as solution

class TestStringSearch(unittest.TestCase):
    def test_case_1(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')]
        searchArray = [(1, 'abcdef'), (5, 'uvwxy')]
        expected_output = [(1, 'abc')]
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_2(self):
        sourceArray = [(1, 'abc')]
        searchArray = [(2, 'def')]
        expected_output = []
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_3(self):
        sourceArray = [(1, 'abc'), (2, 'def')]
        searchArray = [(3, 'abc'), (4, 'def')]
        expected_output = [(1, 'abc'), (2, 'def')]
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_4(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi'), (4, 'jkl')]
        searchArray = [(5, 'mnopqr')]
        expected_output = []
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_5(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        searchArray = [(4, 'abcdefghi'), (5, 'defghiabc')]
        expected_output = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_6(self):
        sourceArray = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        searchArray = [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]
        expected_output = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        self.assertEqual(solution(sourceArray, searchArray), expected_output)

    def test_case_7(self):
        sourceArray = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        searchArray = [(4, 'abcd'), (5, 'bcda')]
        expected_output = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        self.assertEqual(solution(sourceArray, searchArray), expected_output)


if __name__ == '__main__':
    unittest.main()