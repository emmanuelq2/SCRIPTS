import unittest
from numbers_words_moved import numbers_in_words_moved  as solution


class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution("I have 2 apples and 5 oranges and 3 grapefruits."), "I have a2pples and o5ranges and g3rapefruits.")

    def test2(self):
        self.assertEqual(solution("4 foxes are chasing 1 rabbit."), "f4oxes are chasing r1abbit.")
 
    def test3(self):
        self.assertEqual(solution("Let's meet at 7 at the clock tower."), "Let's meet at a7t the clock tower.")

    def test4(self):
        self.assertEqual(solution("There are 8 wonders of the world."), "There are w8onders of the world.")

    def test5(self):
        self.assertEqual(solution("I will bring 6 bottles of water and 4 packets of chips."), "I will bring b6ottles of water and p4ackets of chips.")

    def test6(self):
        self.assertEqual(solution("It is a 9 day journey to the mountains."), "It is a d9ay journey to the mountains.")

    def test7(self):
        self.assertEqual(solution("She has lived in 4 cities and 2 countries."), "She has lived in c4ities and c2ountries.")

    def test8(self):
        self.assertEqual(solution("He walked 5 miles to school every day."), "He walked m5iles to school every day.")

    def test9(self):
        self.assertEqual(solution("The city has 6 gates."), "The city has g6ates.")

    def test10(self):
        self.assertEqual(solution("There are 3 books on the table."), "There are b3ooks on the table.")

if __name__ == '__main__':
    unittest.main()