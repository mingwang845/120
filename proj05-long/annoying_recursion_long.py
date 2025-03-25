"""
    File: annoying_recursion_long.py
    Author: Ming Wang
    Purpose: A simple file filled with one annoying
    recursive function
"""

def annoying_fibonacci_sequence(n):
    """
        This function returns a fibonacci sequence value recursively and
        appends to a list
        Arguments: n is a int input
        Return Value: sequence the fibonacci sequence value for n within a list
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Recursively appends and adds to a list for the fibonnaci sequence
        sequence = annoying_fibonacci_sequence(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

