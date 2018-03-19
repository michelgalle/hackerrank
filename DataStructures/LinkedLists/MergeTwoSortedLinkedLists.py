"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeListsR(headA, headB):
    if not headB:
        return headA
    elif not headA:
        return headB
    if headA.data > headB.data:
        headB.next = MergeListsR(headA, headB.next)
        return headB
    else:
        headA.next = MergeListsR(headA.next, headB)
        return headA


def MergeLists(headA, headB):
    if not headA or not headB:
        return headA if not headB else headB

    if headA.data <= headB.data:
        node = headA
        headA = headA.next
    else:
        node = headB
        headB = headB.next

    head = node

    while headA and headB:
        if headA.data <= headB.data:
            node.next = headA
            headA = headA.next
        elif headA.data > headB.data:
            node.next = headB
            headB = headB.next
        node = node.next
    node.next = headA or headB

    return head
