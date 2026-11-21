
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
            print("Process added successfully")
            return

        temp = self.head

        while temp.next is not None and temp.next.priority <= priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        print("Process added successfully")

    def dequeue(self):
        if self.head is None:
            print("Empty queue")
            return

        temp = self.head

        print("Deleted Process details:")
        print("Process id:", temp.pid)
        print("Process name:", temp.name)
        print("Process priority:", temp.priority)

        self.head = self.head.next

    def display_next(self):
        if self.head is None:
            print("No process available")
            return

        print("Next process:")
        print("Process id:", self.head.pid)
        print("Process name:", self.head.name)
        print("Process priority:", self.head.priority)

    def display_all(self):
        if self.head is None:
            print("Empty queue")
            return

        temp = self.head

        print(" processes are :")
        while temp:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next

    def count(self):
        temp = self.head
        c = 0

        while temp:
            c += 1
            temp = temp.next

        print("Total processes:", c)


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




    

