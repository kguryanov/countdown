import collections
import random
import time
from string import ascii_lowercase

from data import all_words


class Anagrams:

    def __init__(self, conundrum=None, min_len=4, max_len=9):
        self._conundrum_map = {}
        if conundrum is None:
            conundrum = self._gen_conundrum(max_len)
        self.set_conundrum(conundrum)
        self._conundrum = conundrum
        self.words = self._init_words(min_len, len(self._conundrum))

    def set_conundrum(self, conundrum):
        self._conundrum = conundrum
        for c in set(self._conundrum):
            self._conundrum_map[c] = sum(map(lambda x: 1 if c in x else 0, self._conundrum))

    def get_conundrum(self):
        return self._conundrum

    def _init_words(self, min_len, max_len):
        """
        Load words dictionary and limit the active dictionary with minimal and maximal word lenths
        :param min_len: minimal length of an word in dictionary
        :param max_len: miximal length of an word in dictionary
        :return: A set of words acceptable according to min/max parameters
        """
        return [x for x in all_words if len(x) in range(min_len, max_len + 1)]

    def count_letters(self, word):
        """

        :param word:
        :param conundrum:
        :param conundrum_map:
        :return:
        """
        count: int = 0
        for c in set(self._conundrum):
            c_count = word.count(c)
            if c_count == self._conundrum_map[c]:
                count += c_count

        if count == len(word):
            return count
        return 0

    def _gen_conundrum(self, limit):
        conundrum = ''
        for i in range(limit):
            conundrum += random.choice(ascii_lowercase)
        return conundrum

    def get_words(self):
        words = {}
        for word in self.words:
            count = self.count_letters(word)
            if count > 0:
                # words[word] = count
                words.setdefault(count, []).append(word)
        return collections.OrderedDict(sorted(words.items()))


if __name__ == '__main__':
    my_conundrum = 'nuttylog'
    start = time.time()
    words_game = Anagrams(my_conundrum)
    print("Dictionary init time: {}\n".format(time.time() - start))
    print("Conundrum: {}".format(words_game.get_conundrum()))
    candidates = words_game.get_words()

    if len(candidates) == 0:
        print("No candidates found")
        exit(0)

    for k, v in candidates.items():
        print("Candidates count for length {}: {}".format(k, len(v)))

    best_candidates_key = max(candidates.keys())

    print("Total candidates count: {}".format(sum(len(v) for v in candidates.values())))
    print("Best candidates count ({} letters): {}".format(best_candidates_key, len(candidates[best_candidates_key])))

    # print(candidates)
    print("Best candidates: {}".format(candidates[best_candidates_key]))
