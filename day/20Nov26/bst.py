class Node:
    def __init__(self, value):
        self.left=None
        self.data = value
        self.right =None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, new_node):
        if self.root is None: #BST IS EMPTY
            self.root = new_node
        else:
            temp = self.root #FOR COMPARISON and traversal
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
            if rt is None:
                return
            else:
                print(rt.data, end= " ")
                self.preorder(rt.left)
                self.preorder(rt.right)

    def postorder(self, rt):
                if rt is None:
                    return
                else:
                    self.postorder(rt.left)
                    self.postorder(rt.right)
                    print(rt.data, end= " ")


b1= BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.inorder(b1.root)

print("\npreorder: ")
b1.preorder(b1.root)

print("\npostorder: ")
b1.postorder(b1.root)

