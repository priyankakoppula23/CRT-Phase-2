class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def printInOrder(root):
    if root == None:
        return 
    printInOrder(root.left)
    print(root.val,end=",")
    printInOrder(root.right)
def insertIntoBST(root,val):
    if root == None:
        return Node(val) 
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
def deleteNodeFromBST(root, val):
    if root == None:
        return None
    elif root.val > val:
        root.left = deleteNodeFromBST(root.left, val)
    elif root.val < val:
        root.right = deleteNodeFromBST(root.right, val)
    else:
        if root.left == None and root.right == None:
            return None
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        curr = root.right 
        while curr.left != None:
            curr = curr.left 
        root.val = curr.val 
        root.right = deleteNodeFromBST(root.right, curr.val)
    return root
nums = [10,31,23,9,20,18,21,6,14,39,40,45,26]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printInOrder(root)
print()
root = deleteNodeFromBST(root, 20)
printInOrder(root)
print()