class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_left(self, parent, k):
        parent.left = self._insert(parent.left, k)

    def insert_right(self, parent, k):
        parent.right = self._insert(parent.right, k)

    def _insert(self, root, k):
        if root is None:
            return TreeNode(k)
        if root.val > k:
            root.left = self._insert(root.left, k)
        else:
            root.right = self._insert(root.right, k)
        return root

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.val, end=" ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root:
            print(root.val, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.val, end=" ")

    def search(self, key, root=None):
        if root is None:
            root = self.root
        if root is None or root.val == key:
            return root
        elif root.val > key:
            return self.search(key, root.left)
        else:
            return self.search(key, root.right)

    def find_min(self, root=None):
        if root is None:
            root = self.root
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.val

# Create a BinarySearchTree instance
bst = BinarySearchTree()

# Insert elements into the BST
bst.root = TreeNode(10)
bst.insert_left(bst.root, 5)
bst.insert_right(bst.root, 15)

# In-order traversal
print("In-order Traversal:")
bst.in_order_traversal(bst.root)
print()

# Pre-order traversal
print("Pre-order Traversal:")
bst.pre_order_traversal(bst.root)
print()

# Post-order traversal
print("Post-order Traversal:")
bst.post_order_traversal(bst.root)
print()

# Search for a key
key = 5
result = bst.search(key)
if result:
    print(f"Key {key} found in the tree.")
else:
    print(f"Key {key} not found in the tree.")

# Find the minimum value in the tree
min_value = bst.find_min()
if min_value is not None:
    print(f"Minimum value in the tree: {min_value}")
else:
    print("Tree is empty.")
