"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    node = head
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next

    return head
