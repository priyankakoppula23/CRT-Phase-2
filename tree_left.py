class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
def printLeftView(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            currNode = Q.pop(0)
            if i == 0:
                result.append(currNode.data)
            if currNode.left != None:
                Q.append(currNode.left)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Left view is:", result)
obj1 = Node(12)
obj2 = Node(5)
obj3 = Node(8)
obj4 = Node(-1)
obj5 = Node(2)
obj6 = Node(89)
obj1.left = obj2
obj1.right = obj3 
obj2.left = obj4
obj2.right = obj5
obj3.right = obj6
printLeftView(obj1)