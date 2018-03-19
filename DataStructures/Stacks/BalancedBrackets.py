#!/bin/python3

import sys

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
        return 'YES'
    for c in expression:
        if c == '{':
            stack.push('}')
        elif c == '[':
            stack.push(']')
        elif c == '(':
            stack.push(')')
        else:
            if stack.isEmpty() or c != stack.pop():
                return 'NO'
    if not stack.isEmpty():
        return 'NO'
    return 'YES'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = is_matched(s)
        print(result)
