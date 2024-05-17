class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Preorder Traversal (Root-Left-Right)
def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Inorder Traversal (Left-Root-Right)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

# Postorder Traversal (Left-Right-Root)
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")

# Creating a sample tree
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

# Perform tree traversals
print("Preorder Traversal:")
preorder_traversal(root)

print("\nInorder Traversal:")
inorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)
