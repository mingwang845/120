"""
    File: linked_list_recursion_long.py
    Author: Ming Wang
    Purpose: A simple file filled with linked list
    recursive functions
"""
from list_node import ListNode

def array_to_list_recursive(data):
    """
        This function recursively iterates and changes the
        input array into a linked list format
        Arguments: data is an array of data
        Return Value: head pointer for the converted
        array to linked list value
    """
    if not data:
        return None
    head = ListNode(data[0])
    head.next = array_to_list_recursive(data[1:])

    return head

def accordion_recursive(head):
    """
        This function recursively iterates and only has
        the values of every other value in a linked list
        starting with at the second value in the linked list
        Arguments: head pointer to the orginal linked list
        Return Value: head pointer for the new updated linked list

    """
    if head is None or head.next is None:
        return None
    head = head.next
    head.next = accordion_recursive(head.next)
    return head


def pair_recursive(head1, head2):
    """
        This function recursively iterates a two linked
        lists and combines the value of each val
        into a new linked list with tuples, and finishs when the
        shorter linked list has no more values
        Arguments: head1 the first linked list head pointer
        head2 the second linked list head point
        Return Value: head pointer for the combined tuple linked list
    """
    if head1 is None or head2 is None:
        return
    head = ListNode((head1.val, head2.val))
    head.next = pair_recursive(head1.next, head2.next)

    return head