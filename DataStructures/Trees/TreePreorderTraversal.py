"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    if root:
        #print root.data,
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        #print root.data,


def inOrder(root):
    if root:
        inOrder(root.left)
        #print root.data,
        inOrder(root.right)
