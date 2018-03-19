'''
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def put(self, value):
        self.stack1.append(value)
'''


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class MyQueue(object):

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        if self.length == 0:
            return None
        return self.head.value

    def put(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            tail = None
        return value


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
