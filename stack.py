def push(stack, ele):
    stack.append(ele)
    print(ele, "inserted into stack successfully")

def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return
    print(stack[-1], "deleted successfully")
    stack.pop()

stack = []
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
print(stack)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
print(stack)

