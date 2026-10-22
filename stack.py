
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
        self.top = new_node  # Missing line!

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp = None

    def print(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        print("Stack contains...")
        temp = self.top

        while temp:
            print(temp.data)
            temp = temp.next

# Instance creation
st = Stack()
st.push(Node(10))
st.push(Node(50))
st.push(Node(30))
st.push(Node(70))
st.push(Node(80))

st.print()
st.pop()
st.pop()
st.print()