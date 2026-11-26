#BST using linked ist
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    cntl=0
    cntnl=0
    cnt=0
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:#BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:#left subtree
                    if temp.left is None:
                       temp.left=new_node
                       return
                    else:
                       temp=temp.left
                else:
                    #right subtree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def preorder(self,rt):
            if rt is None:
                return
            else:
                print(rt.data,end=" ")
                self.preorder(rt.left)
                self.preorder(rt.right)
    def postorder(self,rt):
            if rt is None:
                return
            else:
                self.postorder(rt.left)
                self.postorder(rt.right)
                print(rt.data,end=" ")
    def descending(self,rt):
            if rt is None:
                return
            else:
                self.inorder(rt.right)
                print(rt.data,end=" ")
                self.inorder(rt.left)
    def minimum(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nMinimum node value:",temp.data)
    def maximum(self):
            temp=self.root
            while temp.right:
                temp=temp.right
            print("\nMaximum node value:",temp.data)
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
              return True
            elif key<temp.data:
               temp=temp.left
            else:
               temp=temp.right
        return False
    def count_leaf(self,rt):
            if rt is None:
                return
            else:
                self.count_leaf(rt.left)
                if rt.left is None and rt.right is None:
                    self.cntl+=1
                
                self.count_leaf(rt.right)
    def count_nonleaf(self,rt):
                if rt is None:
                    return
                else:
                    self.count_nonleaf(rt.left)
                    if rt.left is not  None or rt.right is not None:
                        self.cntnl+=1
                    
                    self.count_nonleaf(rt.right)
    def count(self,rt):
        if rt is None:
            return
        else:
            self.count(rt.left)
            self.cnt+=1
            self.count(rt.right)
    #BFS
    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
            return
        arr=[]
        cnt=0
        arr.append(rt)
        while cnt<len(arr):
            temp=arr[cnt]
            cnt+=1
            print(temp.data,end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)


b1=BST()
b1.insert(Node(10))
b1.insert(Node(23))
b1.insert(Node(347))
b1.insert(Node(37))
b1.insert(Node(0))
b1.insert(Node(24))
b1.insert(Node(874))
print("Inorder")
b1.inorder(b1.root)
print("\nPreorder")
b1.preorder(b1.root)
print("\npostorder")
b1.postorder(b1.root)
b1.minimum()
b1.maximum()
if b1.search(40):
    print("\nFound")
else:
    print("not found")
b1.count_leaf(b1.root)
print("Total number of leaf nodes:",b1.cntl)
b1.count_nonleaf(b1.root)
print("Total number of non leaf nodes:",b1.cntnl)
b1.count(b1.root)
print("\nTotal number of nodes in BST :",b1.cnt)
b1.count(b1.root.left)
print("\nTotal number of nodes in left subtree  :",b1.cnt)
b1.count(b1.root.right)
print("\nTotal number of nodes in right subtree  :",b1.cnt)
print("\nlevel order is:")
b1.level_order(b1.root)






           