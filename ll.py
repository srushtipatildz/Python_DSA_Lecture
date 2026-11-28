class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedLikst:
    def __init__(self):
        self.head=None

# insertion at begining
    def insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
# traversing:

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("none")
L1=LinkedLikst()
L1.insert(20)
L1.insert(90)
L1.insert(900)
L1.display()