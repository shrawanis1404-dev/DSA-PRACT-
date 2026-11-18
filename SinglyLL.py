class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node value
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("Linked List is empty")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)
    def delete_at_position(self, position):
        if position < 1 or self.head is None:
            print("Invalid position")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
     # Delete at a specific position
    def delete_at_position(self, position):
        if position < 1 or self.head is None:
            print("Invalid position")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Sum of every two consecutive nodes
    def sum_consecutive(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next

ll = LinkedList()

# 1. Create linked list
values = [10, 20, 30, 40, 50]
for value in values:
    ll.append(value)

# 2. Display linked list
ll.display()

# 3. Insert at position
ll.insert_at_position(25, 3)
ll.display()

# 4. Find middle node
ll.find_middle()

# 5. Delete at position
ll.delete_at_position(2)
ll.display()

# 6. Reverse linked list
ll.reverse()
ll.display()

# 7. Sum of every two consecutive nodes
ll.sum_consecutive()

