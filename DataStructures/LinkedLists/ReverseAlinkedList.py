"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if not head or not head.next: return head
    newHead = Reverse(head.next)
    newHead.next = head
    head.next = None
    return newHead

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def Reverse(head):
    stack = Stack()
    if head:
        while head:
            stack.push(head)
            head = head.next
        head = stack.pop()
        node = head
        while not stack.isEmpty():
            node.next = stack.pop()
            node = node.next
        node.next = None
    return head

