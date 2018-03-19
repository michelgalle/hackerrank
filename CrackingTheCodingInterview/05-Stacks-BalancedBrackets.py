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


def is_matched(expression):
    stack = Stack()
    if expression == '':
        return True
    for c in expression:
        if c == '{':
            stack.push('}')
        elif c == '[':
            stack.push(']')
        elif c == '(':
            stack.push(')')
        else:
            if stack.isEmpty() or c != stack.pop():
                return False
    if not stack.isEmpty():
        return False
    return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
