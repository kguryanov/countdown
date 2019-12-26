import time
import unittest

from words_game.anagrams import Anagrams


class TestWordsMethods(unittest.TestCase):

    def test_match_9(self):
        conundrum = 'specifics'
        start = time.time()
        words_game = Anagrams(conundrum)
        print("Dictionary init time: {}\n".format(time.time() - start))

        candidates = words_game.get_words()
        self.assertGreater(len(candidates), 0, "Expected valid candidates matching \"{}\"".format(conundrum))
        self.assertIn(conundrum, candidates[9], "Candidates disctionary must contain \"{}\"".format(conundrum))


if __name__ == '__main__':
    unittest.main()
