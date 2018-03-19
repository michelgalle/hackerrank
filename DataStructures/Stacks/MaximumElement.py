stack = []
maxStack = []
for _ in range(int(input())):
    q = list(map(int,input().split()))
    if q[0] == 1:

        stack.append(q[1])
        if maxStack == [] or maxStack[len(maxStack)-1] <= q[1]:
            maxStack.append(q[1])
    elif q[0] == 2:
        if stack[len(stack)-1] == maxStack[len(maxStack)-1]:
            maxStack.pop()
        stack.pop()
    else:
        print(maxStack[len(maxStack)-1])


class Stack():
    def init(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop()
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
