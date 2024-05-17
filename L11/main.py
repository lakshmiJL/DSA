class TreeNode:
  def __init__(self, x):
    self.data = x
    self.leftChild = None
    self.rightChild = None

def InOrderTraversal(root):  #Left, Root, Right
    if root is not None:
      if root.leftChild is not None:
          InOrderTraversal(root.leftChild)
      print(root.data)
      if root.rightChild is not None:
          InOrderTraversal(root.rightChild)

def InOrderTraversal2(root, level=0, prefix="Root: "):  # Left, Root, Right
    if root is not None:
        InOrderTraversal2(root.rightChild, level + 1, "R:")
        print(" " * 4 * level + prefix + str(root.data))
        InOrderTraversal2(root.leftChild, level + 1, "L:") 

def Insert(root, k):
    if root == None:
        return TreeNode(k)
    if root.data > k:
        root.leftChild = Insert(root.leftChild, k)
    else:
        root.rightChild = Insert(root.rightChild, k)
    return root

def InorderSuccesor(root):
  current = root
  while current.leftChild is not None:
    current = current.leftChild
  return current


def delete(root, key):
  if root is None:
    return root
  if key < root.data:
    root.leftChild = delete(root.leftChild, key)
  elif key > root.data:
    root.rightChild = delete(root.rightChild, key)
  else:  
    # Root has only 1 child
    if root.leftChild is None:
      temp = root.rightChild
      root = None
      return temp
    # Root has only one child
    elif root.rightChild is None:
      temp = root.leftChild
      root = None
      return temp
    # Root has 2 child
    
    temp = InorderSuccesor(root)
    print("Hello", temp.data)
    t = root.data
    root.data = temp.data
    temp.data = t
    root.rightChild = delete(root.rightChild, temp.data)

def is_empty(root):
    return root is None

n = int(input("Enter the number of elements you want in the tree - "))
root = None
for i in range(n):
    x = int(input("Enter the node value - "))
    root = Insert(root, x)

InOrderTraversal(root)

# Call the delete function with respect to the tree created by you above, Make sure that each of the 3 cases are demonstrated during the session
print("BST structure before deletion:")
InOrderTraversal2(root)
print()

key_to_delete = int(input("Enter the key to be deleted - "))



# Delete the node and demonstrate each case
root = delete(root, key_to_delete)

# Print the BST structure before deletion
#print("\nBST structure after deletion:")
#InOrderTraversal2(root)

# Print the BST structure after deletion
print("\nBST structure after deletion:")
if root is not None:
    InOrderTraversal2(root)
else:
    print("BST is empty after deletion.")