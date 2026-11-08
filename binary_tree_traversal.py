# Program to demonstrate preorder, inorder, and postorder tree traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Create a sample binary tree
#          1
#        /   \
#       2     3
#      / \   /
#     4   5 6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Preorder traversal:")
preorder(root)

print("\nInorder traversal:")
inorder(root)

print("\nPostorder traversal:")
postorder(root)
print()
