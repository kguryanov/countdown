import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

words_file_name = os.path.join(__location__,'words_alpha.txt')

with open(words_file_name) as word_file:
    all_words = set(word_file.read().split())