class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printpreorder(root):
    if root == None:
        return
    print(root.data)
    printpreorder(root.left)
    printpreorder(root.right)
def printInOrder(root):
    if root == None:
        return
    printInOrder(root.left)
    print(root.data)
    printInOrder(root.right)
def printPostOrder(root):
    if root == None:
        return
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.data)


o1 = Node(-15)
o2 = Node(10)
o3 = Node(7)
o4 = Node(115)
o5 = Node(102)
o6 = Node(15)
o7 = Node(8)
o8 = Node(3)
o9 = Node(71)
o10 = Node(80)
o1.left = o2
o1.right = o3
o2.left = o4
o2.right = o5
o5.left = o8
o3.left = o6
o3.right = o7
o6.right = o9
o7.right = o10

printpreorder(o1)
printInOrder(o1)
printPostOrder(o1)

