"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""

from string import ascii_lowercase

def is_pangram(st):
    str_set = set(st.lower())
    alpha_set = set()
    for item in str_set:
        if item.isalpha():
            alpha_set.add(item)
    print(alpha_set)
    print(set(ascii_lowercase))
    if alpha_set == set(ascii_lowercase):
        return True
    return False
