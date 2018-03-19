""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(n, min=0, max=10000):
    if not n:
        return True
    if n.data <= min or n.data >= max:
        return False
    return checkBST(n.left, min, n.data) and checkBST(n.right, n.data, max)