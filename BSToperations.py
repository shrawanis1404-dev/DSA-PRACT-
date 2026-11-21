#BST using linked ist
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
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




           