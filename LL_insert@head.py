class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()

def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtHead(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)
 
 
 
 

 
