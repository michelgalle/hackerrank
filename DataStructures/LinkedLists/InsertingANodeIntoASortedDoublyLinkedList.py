"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def SortedInsert(head, data):
    node = Node(data)
    if not head: return node
    if head.data > data:
        node.next = head
        head.prev = node
        return node
    cur = head
    while cur.next and cur.data < data:
        cur = cur.next
    if cur.data < data:
        cur.next = node
        node.prev = cur
    else:
        node.prev = cur.prev
        cur.prev = node
        node.prev.next = node
        node.next = cur
    return head
