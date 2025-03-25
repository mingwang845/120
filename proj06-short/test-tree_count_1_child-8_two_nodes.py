#! /usr/bin/python3

""" Code to test the tree_count_1_child() function

    Author: Russ Lewis
"""

import tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_count_1_child()...")
    print()

    retval = tree_funcs.tree_count_1_child(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


