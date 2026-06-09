import unittest
from words_replaced import replace_inverse_words as solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'], ['simple', 'bond', 'e']), ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'])
        
    def test2(self):
        self.assertEqual(solution(['hello world!', 'i am here', 'python is love'], ['world', 'here', 'love']), ['hello dlrow!', 'i am ereh', 'python is evol'])
        
    def test3(self):
        self.assertEqual(solution(['i am not a robot', 'you are not alone', 'we are all together'], ['am', 'are', 'are']), ['i ma not a robot', 'you era not alone', 'we era all together'])
        
    def test4(self):
        self.assertEqual(solution(['apple', 'ball', 'cat'], ['a', 'b', 'c']), ['apple', 'ball', 'cat'])
        
    def test5(self):
        self.assertEqual(solution(['this is a test', '', '', 'one more'], ['test', 'a', 'b', 'one']), ['this is a tset', '', '', 'eno more'])
        
    def test6(self):
        self.assertEqual(solution(['lower case sentence', 'upper case Sentence', 'another Sentence here', 'final Sentence yay'], ['sentence', 'sentence', 'sentence', 'sentence']), ['lower case ecnetnes', 'upper case Ecnetnes', 'another Ecnetnes here', 'final Ecnetnes yay'])
        
    def test7(self):
        self.assertEqual(solution(['this is a very very long sentence just to check the maximum limit of the sentence. see if it can handle the maximum characters or not.', 'can it handle', 'it or not', "let's see."], ['very', 'handle', 'it', 'see']), ['this is a yrev yrev long sentence just to check the maximum limit of the sentence. see if it can handle the maximum characters or not.', 'can it eldnah', 'ti or not', "let's ees."])
        
    def test8(self):
        self.assertEqual(solution(['just a string', 'with some words', 'and nothing else'], ['just', 'some', 'nothing']), ['tsuj a string', 'with emos words', 'and gnihton else'])

if __name__ == '__main__':
    unittest.main()