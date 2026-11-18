class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    # Enqueue
    def enqueue(self, value):
        new_node = Node(value)

        if self.isempty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front
            print("Deleted element:", temp.data)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # Display
    def display(self):
        temp = self.front
        print("Queue elements:")

        while temp:
            print(temp.data)
            temp = temp.next

    # Reverse Queue using Stack
    def reverse(self):
        stack = []

        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(stack.pop())

    # Merge two queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(temp.data)
            temp = temp.next

    # Check identical
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None


# Main program

q1 = Queue()
q2 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print("Original Queue:")
q1.display()

q1.dequeue()

print("After Dequeue:")
q1.display()

q1.reverse()

print("Reversed Queue:")
q1.display()

q2.enqueue(50)
q2.enqueue(60)

q1.merge(q2)

print("Merged Queue:")
q1.display()

print("Are queues identical?", q1.identical(q2))