#! /usr/bin/python3

""" Code to test the tree_count() function

    Author: Russ Lewis
"""

import tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = None



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_count()...")
    print()

    retval = tree_funcs.tree_count(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


