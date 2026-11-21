
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    # 1. Add Process (Enqueue)
    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        # If queue is empty or new process has highest priority
        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Process added successfully!")

    # 2. Execute Process (Dequeue)
    def dequeue(self):
        if self.head is None:
            print("Queue is empty!")
            return

        temp = self.head
        print("Executed Process:")
        print("PID:", temp.pid)
        print("Name:", temp.name)
        print("Priority:", temp.priority)

        self.head = self.head.next

    # 3. View Next Process
    def display_next(self):
        if self.head is None:
            print("No process available!")
        else:
            print("Next Process:")
            print("PID:", self.head.pid)
            print("Name:", self.head.name)
            print("Priority:", self.head.priority)

    # 4. Display All Processes
    def display_all(self):
        if self.head is None:
            print("Queue is empty!")
            return

        temp = self.head
        print("Pending Processes:")

        while temp is not None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next

    # 5. Count Processes
    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        print("Total Processes:", c)


# Main Program
pq = PriorityQueue()

pq.enqueue(101, "System Process", 1)
pq.enqueue(102, "Interactive Process", 2)
pq.enqueue(103, "Background Process", 3)
pq.enqueue(104, "Low Priority Process", 4)
pq.enqueue(105, "Another System Process", 1)

pq.display_all()

pq.display_next()

pq.dequeue()

pq.display_all()

pq.count()

        
      