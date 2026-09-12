"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    split_it = s.rsplit(" ")
    l = ""
    for f in split_it:
        if not l or len(f) < len(l):
            l = f
    return len(l) 