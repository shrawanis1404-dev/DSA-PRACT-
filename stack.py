#reverse stack using another stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp.next = None

    def print(self):
        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next

    # Reverse stack using another stack
    def reverse(self, st1):
        temp = self.top
        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

    # Reverse string using stack
    def reverse_string(self, s):
        st = Stack()

        for ch in s:
            st.push(Node(ch))

        rev = ""
        while not st.isempty():
            rev += st.top.data
            st.pop()

        return rev


st = Stack()
st1 = Stack()

st.push(Node(20))
st.push(Node(54))
st.push(Node(30))
st.push(Node(18))
st.push(Node(87))

print("Original Stack:")
st.print()

st.pop()

print("After Pop:")
st.print()

st.reverse(st1)

print("Reversed Stack:")
st1.print()

print("Reversed String:")
print(st.reverse_string("hello"))