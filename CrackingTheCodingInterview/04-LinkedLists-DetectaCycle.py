"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False


"""
def has_cycle(head):
    if ( not head ):
        return False
    slow = head
    fast = head.next
    while (slow != fast):
        if ( not fast or not fast.next ):
            return False
        slow = slow.next
        fast = fast.next.next

    return True
"""