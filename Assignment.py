# #Q.1 Create a Stack with following operations 
# # 1. Push 
# stack = []

# def push():
#     value = input("Enter element: ")
#     stack.append(value)
#     print("Element pushed successfully!")

# push()

# print("Stack:", stack)
# # 2. Pop 
# def pop():
#    if len(stack) == 0:
#     print("Stack is empty")
#    else:
#      print("Popped element:", stack.pop())

# # pop()
# #3.Display 
# def display():
#  if len(stack) == 0:
#   print("Stack is empty")
#  else:
#   print("Stack elements (top to bottom):")
# for i in range(len(stack) - 1, -1, -1):
#  print(stack[i])

# push()
# push()
# push()

# print("Stack:", stack)
# display()
# # 4. Reverse String using Stack 
# string = input("Enter a string: ")
# stack = []

# for ch in string:
#     stack.append(ch)

# reverse = ""

# while len(stack) > 0:
#     reverse += stack.pop()

# print("Reversed string:", reverse)
# 5. Reverse Stack using another Stack
stack = [10, 20, 30, 40, 50]
temp = []

print("Original Stack:", stack)

while len(stack) > 0:
    temp.append(stack.pop())

stack = temp

print("Reversed Stack:", stack)
