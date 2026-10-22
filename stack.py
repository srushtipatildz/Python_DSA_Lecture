
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp = None

    def reverse(self):
        prev = None
        temp = self.top

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.top = prev

    def print(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        print("Stack contains...")
        temp = self.top

        while temp:
            print(temp.data)
            temp = temp.next

    def compare(self, stack2):
        temp1 = self.top
        temp2 = stack2.top

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

        temp1 = temp1.next
        temp2 = temp2.next

        if temp1 is None and temp2 is None:
            return True
        return False

# Instance creation
st = Stack()

st.push(Node(10))
st.push(Node(50))
st.push(Node(30))
st.push(Node(70))
st.push(Node(80))

# Print stack
st.print()

# Pop elements
st.pop()
st.pop()

st.print()

# Reverse stack
st.reverse()

print("After reversing:")
st.print()
st1 = Stack()
st1.push(Node(10))
st1.push(Node(20))
st1.push(Node(30))

st2 = Stack()
st2.push(Node(10))
st2.push(Node(20))
st2.push(Node(30))

if st1.compare(st2):
    print("Stacks are equal")
else:
    print("Stacks are not equal")