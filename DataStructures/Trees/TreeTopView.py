"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root, order = 0):
    #Write your code here
    if not root: return
    if order <= 0: topView(root.left, -1)
    print root.data ,
    if order >= 0: topView(root.right, 1)