class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        def delete(self,value):
            temp=self.head
            prev=None   
            if(temp.data==value):
                self.head=self.head.next
                return
            while(temp is not None):
                if(temp.data==value):
                    break
                else:
                 prev=temp
                 temp=temp.next
            if(temp==None):
                print("Value is not in the list")     
                return
            prev.next=temp.next
            temp=None
    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next
list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))

list.print()