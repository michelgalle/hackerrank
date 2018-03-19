"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    while True:
        if not headA and not headB:
            return 1
        if not headA and headB or headA and not headB or headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next