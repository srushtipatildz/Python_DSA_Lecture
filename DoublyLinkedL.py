
# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print_list(self):
        temp = self.head
        print("List Elements:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(13))

list1.print_list()
