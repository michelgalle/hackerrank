"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


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


def ReversePrint(head):
    if head:
        ReversePrint(head.next)
        print(head.data)

def ReversePrint(head):
    stack = Stack()
    if head:
        while head:
            stack.push(head)
            head = head.next
        while not stack.isEmpty():
            print(stack.pop().data)
