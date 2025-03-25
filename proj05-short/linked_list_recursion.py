"""
    File: linked_list_recursion.py
    Author: Ming Wang
    Purpose: Iterates through a linkedlist with and without
    recursion, checking that each subsequent value is 2 higher
"""
def is_plus_two(head):
    """
        This function returns True or false regarding whether or not
        the linked list is in increasing 2 + order iteratively
        Arguments: head is a listNode representing head of a linked list
        Return Value: returns false if it doesn't follow the pattern
        and returns true if the linked does follow the pattern
    """
    if head is None or head.next is None:
        return True
    cur = head
    # iterates until the next value if unavaible indicating it's the last value
    while cur.next is not None:
        # checks to see if the next value if two more if not return false
        if cur.val + 2 != cur.next.val:
            return False
        cur = cur.next
    return True


def is_plus_two_recursive(head):
    """
        This function returns True or false regarding whether or not
        the linked list is in increasing 2 + order recursively
        Arguments: head is a listNode representing head of a linked list
        Return Value: returns false if it doesn't follow the pattern
        and returns true if the linked does follow the pattern
    """
    if head is None or head.next is None:
        return True
    if head.val + 2 != head.next.val:
        return False
    return is_plus_two_recursive(head.next)