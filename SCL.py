# Singly Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Back to Head)")

    # Delete from beginning
    def delete(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # Search
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print("Element found")
                return

            temp = temp.next
            if temp == self.head:
                break

        print("Element not found")


# Main program
cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)

cll.display()

cll.search(20)

cll.delete()
cll.display()