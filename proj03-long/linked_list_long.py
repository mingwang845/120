"""
File: linked_list_long.py
Author: Ming Wang
Purpose: Creates multiple functions regarding modifying and using
linked list, by using a seperate class called list_node.py to do these
implementations.
"""

from list_node import ListNode


def is_sorted(head):
    """
        Checks to see if the linked list is sorted or not in descending order
        Arguments:
        head (list_node()): Head value of a linked list
        Return Value:
        True of False regarding whether or not the list is sort in descending order
        Pre-condition:
        N/A
    """
    cur = head

    if head is None or head.next is None:
        return True
    # checks and goes until you reach None
    while cur.next is not None:
        #if the current value is greater than the next value
        # and if it is then return false
        if(cur.val > cur.next.val):
            return False
        else:
            cur = cur.next
    return True

def list_sum(head):
    """
        Sums up all the values within the linked list
        Arguments:
        head (list_node()): Head value of a linked list
        Return Value:
        O or sum or head.val: which the int total value that is contained within the
        linked list that is given
        Pre-condition:
        N/A
    """
    cur = head
    if head is None:
        return 0
    if head.next is None:
        return head.val

    sum = 0
    # iterates through the whole linkedlist, the reason why
    # you don't do cur.next is that you can account for all values
    while cur is not None:
        sum += cur.val
        cur = cur.next

    return sum


def partition_list(head):
    """
        Splits the list into two seperate list, but by
        partitioning them with alternating values with each list.
        The concept is ever even position in one list, and then every
        odd is the other list. Alteranating which list to add the next head value
        into.
        Arguments:
        head (list_node()): Head value of a linked list
        Return Value:
        (head, None) (first_head.next, second_head.next) Returns the head of each list
        Pre-condition:
        N/A
    """
    # checks to see if the inputted list either has only one value or none
    # and if it's either than you return immediately
    if head is None or head.next is None:
        return head, None

    cur = head
    first_head = ListNode(None)
    second_head = ListNode(None)
    # creates and initializes the two new listNode's that are being
    # created
    first = first_head
    second = second_head

    # changes when you should add a value to which certain lsit
    switch = True

    # the loop will run until the current value in the head
    # linked list is none and there is nothing to add
    while cur:
        # if the switch is true add to the first list
        if switch:
            first.next = cur
            first = first.next
        # else the switch is false add to the second list
        else:
            second.next = cur
            second = second.next
        #reverses and changes the switch
        # iterates to teh next value in cur
        switch = not switch
        cur = cur.next
    # Makes sure the set the last value/ the end of the linked list to tell the user
    # that the linked list is done
    first.next = None
    second.next = None
    # returns the head of both teh first and second head
    # the reason .next is used so that it skips the first initalized none value
    return first_head.next, second_head.next

def accordion_3(head, start_pos):
    """
        Takes a linked list and add every third element/item in the linked list.
        While also making sure that the you start adding to the new value at the given
        starting position.
        Arguments:
        head (list_node()): Head value of a linked list
        start_pos (int): Starting position index of the linked list
        Return Value:
        head or new_head (list_node()): the Head of of the linked list
        Pre-condition:
        N/A
    """
    # checks to see if head is None, if not skip
    if head is None:
        return None
    # chekcs to see if the head.next is None and the start_Pos is 0
    # if so it means it only has one value and the pos is 0 so you can just return the head
    # itself
    if head.next is None and start_pos == 0:
        return head
    cur = head

    # counts what position you are in the linked list so you can %3 to add
    # to the new linked list
    count = 0

    # iterates until the cur isn't None and the index is less than the
    # desired start_pos
    while cur and count < start_pos:
        cur = cur.next
        count +=1

    # if the cur is None then return None as the linked list is empty
    if cur is None:
        return None

    # initializes the new head while also using new_tail as a dummy value you need to add


    new_head = cur
    new_tail = new_head
    cur = cur.next
    index = 1 # reset the index as one

    # iterates until the cur value is None
    while cur:
        # checks to see if the value can me %3 if so you add to the new_tail
        if index %3 == 0:
            new_tail.next = cur
            new_tail = new_tail.next
        cur = cur.next
        index += 1
    # sets the last value in the last value of the list None indicating
    # the linked list is done
    new_tail.next = None

    return new_head


def pair(list1, list2):
    """
        Builds a tuple for each value in the list1 and list2 by combining them
        in the format of (headOne.val, headTwo.val) and iterates through and will
        add to a combined listNode that stores the tuple as the value in the linked list
        and will add to the combined tuple until you reach the end of the shorter linked list.
        Arguments:
        list1 (list_node()): Head value of a linked list
        list2 (list_node()): Head value of a linked list
        Return Value:
        combined.next (list_node()): Head of the combined linked list
        Pre-condition:
        N/A
    """
    # initializes the two linkedList
    headOne = list1
    headTwo = list2

    # creates and initializes the combined list node
    combined = ListNode(None)
    current = combined # set as the head of the combined linked list

    # while loop will run until the shorter list doesn't have any more values
    # the parameters is used to ensure both headOne and headTwo aren't None
    # and if one is false than the while loop will end
    while headOne is not None and headTwo is not None:
        # creates the new node Tuple that you want to add to teh combined list
        new_node = ListNode((headOne.val, headTwo.val))
        # sets the current.next pointer at the new node and the current and new node
        current.next = new_node
        current = new_node

        headOne = headOne.next
        headTwo = headTwo.next

    return combined.next