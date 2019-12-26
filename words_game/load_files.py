import collections
import random
import time
from string import ascii_lowercase

words = {}
max_len = 9
min_len = 5


def load_words(min_len, max_len):
    """
    Load words dictionary and limit the active dictionary with minimal and maximal word lenths
    :param min_len: minimal length of an word in dictionary
    :param max_len: miximal length of an word in dictionary
    :return: A set of words acceptable according to min/max parameters
    """
    with open('../data/words_alpha.txt') as word_file:
        valid_words = [x for x in set(word_file.read().split()) if len(x) in range(min_len, max_len + 1)]

    return valid_words


def count_letters(word, conundrum, conundrum_map):
    """

    :param word:
    :param conundrum:
    :param conundrum_map:
    :return:
    """
    count: int = 0
    for c in set(conundrum):
        c_count = sum(map(lambda x: 1 if c in x else 0, word))
        if c_count == conundrum_map[c]:
            count += c_count

    if count == len(word):
        return count
    return 0


def gen_conundrum(limit):
    conundrum = ''
    for i in range(limit):
        conundrum += random.choice(ascii_lowercase)
    return conundrum


def get_words(dict, conundrum):
    words = {}
    conundrum_map = {}
    for c in set(conundrum):
        conundrum_map[c] = sum(map(lambda x: 1 if c in x else 0, conundrum))
    for word in dict:
        count = count_letters(word, conundrum, conundrum_map)
        if count > 0:
            # words[word] = count
            words.setdefault(count, []).append(word)
    return collections.OrderedDict(sorted(words.items()))


if __name__ == '__main__':
    print(ascii_lowercase)

    conundrum = gen_conundrum(max_len)
    # conundrum = "conundrum"
    start = time.time()
    english_words = load_words(min_len, len(conundrum))
    print("Dictionary load time: {}".format(time.time() - start))
    print("Dictionary size: {}".format(len(english_words)))

    print(conundrum)

    start = time.time()
    candidates = get_words(english_words, conundrum)
    print("Dictionary analyze time: {}\n".format(time.time() - start))

    if len(candidates) == 0:
        print("No candidates found")
        exit(0);

    for k, v in candidates.items():
        print("Count for length {}: {}".format(k, len(v)))

    best_candidates_key = max(candidates.keys())

    print("Total candidates count: {}".format(sum(len(v) for v in candidates.values())))
    print("Best candidates count ({} letters): {}".format(best_candidates_key, len(candidates[best_candidates_key])))

    # print(candidates)
    print("Best candidates: {}".format(candidates[best_candidates_key]))
