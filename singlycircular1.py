
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create circular linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Display linked list
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
        print("(back to head)")
    
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position < 1:
           print("Invalid position")
           return

    # Insert at beginning
        if position == 1:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
            return

    # Insert at any other position
        temp = self.head
        p = 1

        while p < position - 1 and temp.next != self.head:
           temp = temp.next
           p += 1

        if p != position - 1:
           print("Invalid position")
           return

        new_node.next = temp.next
        temp.next = new_node

    


list1 = LinkedList()
list1.append(30)
list1.append(40)
list1.display()
list1.insert_at_position(Node(58),1) 
list1.display()
