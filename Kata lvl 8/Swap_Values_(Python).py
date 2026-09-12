"""
I would like to be able to pass an array with two elements to my function to swap the values. However it appears
that the values aren't changing.

Can you figure out what's wrong here?
"""

def swap_values(pair: list) -> None:
    temp = pair[0]
    pair[0] = pair[1]
    pair[1] = temp