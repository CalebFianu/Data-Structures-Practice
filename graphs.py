class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
def max_depth(root):
    if root == None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))