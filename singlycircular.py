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
            self.head=new_node
        else:
            temp = self.head
            while temp.next!=self.head:
               temp = temp.next

            temp.next = new_node
        new_node.next=self.head

    # Display linked list
    def display(self):
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp==self.head:
                break
        print("None")
        #delete node
list1=LinkedList()
n1=Node(10)
n2=Node(20)
list1.append(Node(30))
list1.append(Node(40))
list1.display()
