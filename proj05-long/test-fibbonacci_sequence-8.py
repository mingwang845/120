#! /usr/bin/python3

""" Code to test the annoying_fibonacci_sequence() function

    Author: Russ Lewis
"""

import annoying_recursion_long





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 8

    print("Testing annoying_fibonacci_sequence()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion_long.annoying_fibonacci_sequence(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


