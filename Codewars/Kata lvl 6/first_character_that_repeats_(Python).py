"""
Find the first character that repeats in a string and return that character. If there is no such character, return undefined/null/None/Nothing, etc. (depending on your language). Your function should be case-sensitive (a is not equivalent to A).

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.

Another example:

In 'translator' you should return 't', not 'a'.

v      v
translator
  ^   ^
While second 'a' appears before second 't', the first 't' is before the first 'a'.
"""


def first_dup(s):
    for letter in s:
        if s.count(letter) > 1:
            return letter
    return None