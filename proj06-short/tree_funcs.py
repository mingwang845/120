"""
    File: tree_funcs.py
    Author: Ming Wang
    Purpose: A simple file simple binary tree
    recursive functions, that do basic calculations and
    things on binary trees
"""



def tree_count(root):
    """
    This function counts the number of nodes
    in the tree
    Arguments: root is the root of the tree
    Return Value: returns the total number of nodes
    """
    if root is None:
        return 0
    left_count = tree_count(root.left)
    right_count = tree_count(root.right)

    return 1 + left_count + right_count


def tree_count_1_child(root):
    """
    This function counts the number of nodes
    in the tree that have exactly one node
    Arguments: root is the root of the tree
    Return Value: returns the total number of nodes
    that have exactly one node
    """

    if root is None:
        return 0

    left_child_exists = root.left is not None
    right_child_exists = root.right is not None

    if left_child_exists and not right_child_exists:
        return 1 + tree_count_1_child(root.left)
    elif not left_child_exists and right_child_exists:
        return 1 + tree_count_1_child(root.right)
    else:
        return tree_count_1_child(root.left) + tree_count_1_child(root.right)


def tree_sum(root):
    """
    This function returns the total sum
    within the tree
    Arguments: root is the root of the tree
    Return Value: returns the total sum of the tree
    """
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_print(root):
    """
    This function prints out all the values/nodes
    within the tree in pre-order recursively
    Arguments: root is the root of the tree
    Return Value: returns N/A
    """
    if root is None:
        return
    print(root.val)
    tree_print(root.left)
    tree_print(root.right)


def tree_print_leaves(root):
    """
    This function prints out all the leaves
    within the tree, meaning don't have any left or
    right node
    Arguments: root is the root of the tree
    Return Value: returns the total sum of the tree
    """
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val)  # Print the value of the leaf node
    else:
        if root.left:
            tree_print_leaves(root.left)  # Corrected recursive call to tree_print_leaves
        if root.right:
            tree_print_leaves(root.right)  # Corrected recursive call to tree_print_leaves


def tree_search(root, val):
    """
    This function returns a boolean on whether or
    not the val paramter exists within the tree.
    Arguments: root is the root of the tree
    val is a int value
    Return Value: returns True or false on whether or not
    the val exists
    """
    if root is None:
        return
    if root.val == val:
        return root
    left_result = tree_search(root.left, val)
    if left_result:
        return left_result

    right_result = tree_search(root.right, val)
    if right_result:
        return right_result


def tree_max(root):
    """
    This function returns max value of the tree, that is
    unorder, so you have to keep track. Additionally, if a root
    is empty replace it with -inf so that you dont' get a type error
    when comparing
    Arguments: root is the root of the tree
    Return Value: returns the max value in the tree
    """
    if root is None:
        return float('-inf')

    left_max = tree_max(root.left)
    right_max = tree_max(root.right)

    if root.val is not None:
        return max(root.val, left_max, right_max)
    else:
        return max(left_max, right_max)
