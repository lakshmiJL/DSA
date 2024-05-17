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

def create_tree():
    root_val = input("Enter the value for the root node: ")
    root = TreeNode(root_val)
    return root

def insert_node(node, sequence):
    current_node = node

    for position in sequence:
        if position == "left":
            if not current_node.left:
                value = input(f"Enter the value for the left child of node {current_node.val}: ")
                current_node.left = TreeNode(value)
            current_node = current_node.left
        elif position == "right":
            if not current_node.right:
                value = input(f"Enter the value for the right child of node {current_node.val}: ")
                current_node.right = TreeNode(value)
            current_node = current_node.right

    print(f"Nodes inserted successfully.")

def main():
    root = None

    while True:
        print("\nMenu:")
        print("1. Create a Tree")
        print("2. Insert Nodes")
        print("3. Preorder Traversal")
        print("4. Inorder Traversal")
        print("5. Postorder Traversal")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            root = create_tree()
            print("Tree created successfully!")

        elif choice == "2":
            if root:
                sequence = input("Enter the sequence of nodes to insert (e.g., 'left left left right'): ").split()
                insert_node(root, sequence)
            else:
                print("Please create a tree first.")

        elif choice == "3":
            if root:
                print("Preorder Traversal:")
                preorder_traversal(root)
            else:
                print("Please create a tree first.")

        elif choice == "4":
            if root:
                print("Inorder Traversal:")
                inorder_traversal(root)
            else:
                print("Please create a tree first.")

        elif choice == "5":
            if root:
                print("Postorder Traversal:")
                postorder_traversal(root)
            else:
                print("Please create a tree first.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
