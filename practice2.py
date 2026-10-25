#SLL
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# #connecting nodes:
# node1.next=node2
# node2.next=node3
# node3.next=node4
# #print:
# current=node1 #pointer which points to node1 right now
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")

# #SECOND APPROACH:
# #Blueprint for node:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #this function handles the entire linked list
# class LinkedList:
#     def __init__(self):
#         self.head=None
# n1=Node(100)
# n2=Node(200)
# n3=Node(300)
# n4=Node(400)
# #connecting nodes
# n1.next=n2
# n2.next=n3
# n3.next=n4
# list=LinkedList()
# list.head=n1
# current=list.head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


#inserting node at the begining:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(400)
n1.next=n2
n2.next=n3
n3.next=n4

myList=linkedList()

myList.head=n1
new_node=Node(900)
new_node.next=myList.head
myList.head=new_node

current =myList.head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("none")











