"""
Write a function to split a string of space-separated words and convert it into an array of words. Words in the input will be separated by exactly one space. The input will not have leading or trailing spaces. A "word" is any contiguous sequence of characters that does not contain any space.

Examples (Input ==> Output):
"string" ==> ["string"]
"Robin Singh" ==> ["Robin", "Singh"]
"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""


# First solution
def string_to_array(s):
    s = s.split(" ")
    return s

# Second solution is just shorter
def string_to_array(s):
    return s.split(" ")