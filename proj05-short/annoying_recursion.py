"""
    File: annoying_recursion.py
    Author: Ming Wang
    Purpose: A simple file filled with annoying
    recursive functions
"""

def annoying_factorial(n):
    """
        This function returns a factorial value recursively
        Arguments: n is a int input
        Return Value: the factorial value for n
    """
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6

    # Hard-coded recursive cases
    elif n == 4:
        return 4 * annoying_factorial(3)
    elif n == 5:
        return 5 * annoying_factorial(4)
    elif n == 6:
        return 6 * annoying_factorial(5)

    # General case for n >= 7
    else:
        return n * annoying_factorial(n - 1)


def annoying_fibonacci(n):
    """
        This function returns a fibonacci sequence value recursively
        Arguments: n is a int input
        Return Value: the fibonacci sequence value for n
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    elif n == 4:
        return annoying_fibonacci(2) + annoying_fibonacci(3)
    elif n == 5:
        return annoying_fibonacci(3)+ annoying_fibonacci(4)
    elif n == 6:
        return annoying_fibonacci(4) + annoying_fibonacci(5)
    else:
        return annoying_fibonacci(n-2) + annoying_fibonacci(n-1)


def annoying_tree_of_tuples(n):
    """
        This function returns a tree of tuples value recursively
        Arguments: n is a int input
        Return Value: the tree of tuples value for n
    """
    # Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return (0, 1, 0)
    elif n == 2:
        return ((0, 1, 0), 2, (0, 1, 0))
    elif n == 3:
        return (((0, 1, 0), 2, (0, 1, 0)), 3, ((0, 1, 0), 2, (0, 1, 0)))

    # Hard-coded recursive cases
    elif n == 4:
        return (annoying_tree_of_tuples(3), 4, annoying_tree_of_tuples(3))
    elif n == 5:
        return (annoying_tree_of_tuples(4), 5, annoying_tree_of_tuples(4))
    elif n == 6:
        return (annoying_tree_of_tuples(5), 6, annoying_tree_of_tuples(5))

    # General case for n >= 7
    else:
        left_subtree = annoying_tree_of_tuples(n - 1)
        right_subtree = annoying_tree_of_tuples(n - 1)
        return (left_subtree, n, right_subtree)


def annoying_print_downUp(n):
    """
        This function prints the down and up value for an
        integer
        Arguments: n is a int input
        Return Value: N/A
    """
    if n == 0:
        print(0)
        return
    elif n == 1:
        print(1)
        print(0)
        print(1)
        return
    elif n == 2:
        print(2)
        print(1)
        print(0)
        print(1)
        print(2)
        return
    elif n == 3:
        print(3)
        print(2)
        print(1)
        print(0)
        print(1)
        print(2)
        print(3)
        return

    elif n == 4:
        print(4)
        annoying_print_downUp(3)
        print(4)
        return
    elif n == 5:
        print(5)
        annoying_print_downUp(4)
        print(5)
        return
    elif n == 6:
        print(6)
        annoying_print_downUp(5)
        print(6)
        return
    else:
        print(n)
        annoying_print_downUp(n-1)
        print(n)
        return