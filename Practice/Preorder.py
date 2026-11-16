class Node:
    def __init__(self, value=None, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

    def Preorder(self):
        print(self.data,end=" ")
        if self.left is not None:
            self.left.Preorder()
        if self.right is not None:
            self.right.Preorder()

    def Inorder(self):
        if self.left is not None:
            self.left.Inorder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.Inorder()

    def Postorder(self):
        if self.left is not None:
            self.left.Postorder()
        if self.right is not None:
            self.right.Postorder()
        print(self.data,end=" ")

l1 = Node(4)
l2 = Node(7)
c2 = Node(6,l1,l2)
l3 = Node(1)
c1 = Node(3,l3,c2)
l4 = Node(10)
root = Node(8,c1,l4)
print("PreOrder:",end=" ")
root.Preorder()
print()
print("Inorder:",end=" ")
root.Inorder()
print()
print("Postorder:",end=" ")
root.Postorder()
