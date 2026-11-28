#Linked List
# Node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None

# Insertion at begining:
    def insert_beg(self,value):
        new_node=Node(value)#new node creation
        new_node.next=self.head #connecting new node to first node
        self.head=new_node #makes new node the first node

# Traversing:
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ->")
            temp=temp.next
        print("none")
# Insertion at the end:
    def insert_end(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
#Delete Node:
# (first)

    def del_first_node(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.next
l1=LinkedList()
l1.insert_beg(90)
l1.insert_beg(100)
l1.insert_beg(110)
l1.insert_end(600)

l1.del_first_node()
l1.display()

    