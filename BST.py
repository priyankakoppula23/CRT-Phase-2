class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def printInOrder(root):
    if root == None:
        return 
    printInOrder(root.left)
    print(root.val)
    printInOrder(root.right)
def insertIntoBST(root,val):
        if root == None:
            return Node(val) 
        elif root.val > val:
            root.left = insertIntoBST(root.left, val)
        else:
            root.right = insertIntoBST(root.right, val)
        return root
nums = [10,31,23,9,20,18]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printInOrder(root)
    