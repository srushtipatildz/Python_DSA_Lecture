
# Doubly Linear Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # Append at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Print in reverse order
    def print_list(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("Reverse Order:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Main program
list1 = LinkedList()

list1.insert(10)
list1.insert(20)

list1.append(30)
list1.append(40)

list1.print_list()
