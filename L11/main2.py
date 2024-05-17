class TreeNode:
    def __init__(self, x):
        self.data = x
        self.leftChild = None
        self.rightChild = None

def InOrderTraversal(root):  # Left, Root, Right
    if root is not None:
        InOrderTraversal(root.leftChild)
        print(root.data, end=" ")
        InOrderTraversal(root.rightChild)
        #print(root.data, end=" ")
def Insert(root, k):
    if root is None:
        return TreeNode(k)
    if root.data > k:
        root.leftChild = Insert(root.leftChild, k)
    else:
        root.rightChild = Insert(root.rightChild, k)
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.leftChild = delete(root.leftChild, key)
    elif key > root.data:
        root.rightChild = delete(root.rightChild, key)
    else:
        # Case 1: Node with no child
        if root.leftChild is None and root.rightChild is None:
            return None  # Return None to indicate that this node should be removed

        # Case 2: Node with one child
        elif root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp

        # Case 3: Node with two children
        
        temp = minValueNode(root.rightChild)
        root.data = temp.data
        root.rightChild = delete(root.rightChild, temp.data)

    return root

def minValueNode(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current

# Taking user input for BST creation
n = int(input("Enter the number of elements you want in the tree: "))
root = None
for i in range(n):
    x = int(input(f"Enter element {i + 1} to insert: "))
    root = Insert(root, x)

# Printing the BST before deletion
print("\nBST structure before deletion:")
InOrderTraversal(root)

# Taking user input for node deletion
key_to_delete = int(input("\nEnter the key to be deleted: "))
root = delete(root, key_to_delete)

# Printing the BST after deletion
print("\nBST structure after deletion:")
InOrderTraversal(root)
