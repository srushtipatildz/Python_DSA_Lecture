
# Linked List Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse Linked List
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # Delete First Node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete Alternate Nodes
    def delete_alternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next

    # Concatenate Two Linked Lists
    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head


# Create L1
L1 = LinkedList()
L1.insert(10)
L1.insert(20)
L1.insert(30)

# Create L2
L2 = LinkedList()
L2.insert(40)
L2.insert(50)
L2.insert(60)

print("L1:")
L1.display()

print("L2:")
L2.display()

# Concatenate L1 and L2
L1.concatenate(L2)
print("After Concatenation:")
L1.display()

# Reverse Linked List
L1.reverse()
print("Reversed Linked List:")
L1.display()

# Delete First Node
L1.delete_first()
print("After Deleting First Node:")
L1.display()

# Delete Last Node
L1.delete_last()
print("After Deleting Last Node:")
L1.display()

# Delete Alternate Nodes
L1.delete_alternate()
print("After Deleting Alternate Nodes:")
L1.display()
