class TreeNode:
    def __init__(self, x):
        self.data = x
        self.leftChild = None
        self.rightChild = None

def InOrderTraversal(root):
    if root is not None:
        InOrderTraversal(root.leftChild)
        print(root.data, end=" ")
        InOrderTraversal(root.rightChild)

def PreOrderTraversal(root):
    if root is not None:
        print(root.data, end=" ")
        PreOrderTraversal(root.leftChild)
        PreOrderTraversal(root.rightChild)

def PostOrderTraversal(root):
    if root is not None:
        PostOrderTraversal(root.leftChild)
        PostOrderTraversal(root.rightChild)
        print(root.data, end=" ")

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
        # Case 1: Node with no child or one child
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp

        # Case 2: Node with two children
        temp = minValueNode(root.rightChild)
        root.data = temp.data
        root.rightChild = delete(root.rightChild, temp.data)

    return root

def minValueNode(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current

def Search(root, key):
    if root is None or root.data == key:
        return root

    if root.data < key:
        return Search(root.rightChild, key)

    return Search(root.leftChild, key)

# Initialize an empty BST
root = None

while True:
    print("\nMenu:")
    print("1. Insert a node")
    print("2. Delete a node")
    print("3. In-Order Traversal")
    print("4. Pre-Order Traversal")
    print("5. Post-Order Traversal")
    print("6. Search for a node")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the value to insert: "))
        root = Insert(root, data)
        print(f"{data} inserted into the tree.")
    elif choice == 2:
        data = int(input("Enter the value to delete: "))
    # Check if the value to be deleted exists in the tree before attempting deletion
        if Search(root, data):
            root = delete(root, data)
            print(f"{data} deleted from the tree.")
        else:
            print(f"{data} not found in the tree. Deletion failed.")
    elif choice == 3:
        print("In-Order Traversal:", end=" ")
        InOrderTraversal(root)
        print()
    elif choice == 4:
        print("Pre-Order Traversal:", end=" ")
        PreOrderTraversal(root)
        print()
    elif choice == 5:
        print("Post-Order Traversal:", end=" ")
        PostOrderTraversal(root)
        print()
    elif choice == 6:
        data = int(input("Enter the value to search: "))
        if Search(root, data):
            print(f"{data} found in the tree.")
        else:
            print(f"{data} not found in the tree.")
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
