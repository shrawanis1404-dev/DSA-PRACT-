class Node:
    def __init__(self,data):
       self.prev=None
       self.data=data
       self.next=None
    class LinkedList:
        def __init__(self):
            self.head=None
        def append(self,new):
        
            if self is None:
                self.head=new
                return
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
            new.prev=temp
        def insert(self,data,pos):
            new=Node(data)
            #insert node at first position
            if pos==1:
                
                new.next=self.head
                self.head.prev=new
                self.head=new
                return
            #insert node from 2 nd to last position
            temp=self.head
            i=1
            while i!=pos-1 and temp.next:
                temp=temp.next
                i+=1
            if temp.next:
                temp.next.prev=new
           
            new.prev=temp
            new.next=temp.next
            temp.next=new
            
            
            
            
        def print(self):
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
        def delete(self,value):
            temp=self.head
            if temp and temp.data==value:
                self.head=temp.next
                return
            while temp and temp.next:
                if temp.next.data==value:
                    temp.next=temp.next.next
                    return
                temp=temp.next
    l1=LinkedList()
    l1.append(10)
    l1.append(20)
    l1.append(30)
    l1.append(40)
    l1.append(50)
    print("Original list :")
    l1.print()
    l1.insert(45,3)
    print("After inserting 45:")
    l1.print()
    #l1.delete(30)
    #print("After deleting 30:")
    #l1.print()


            
            
