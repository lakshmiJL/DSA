class Node:
  def __init__(self,v):
    self.left=None
    self.right=None
    self.data=v
    
def Inorder(root):
    if root:
      Inorder(root.left)
      print(root.data)
      Inorder(root.right)
def Postorder(root):
    if root is None:
      return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data)
def Preorder(root):
    if root is None:
      return
    print(root.data)
    Preorder(root.left)
    Preorder(root.right)
  
if __name__=="__main__":
  root=Node(100)
  root.left=Node(20)
  root.right=Node(30)
  root.left.left=Node(40)
  root.left.right=Node(70)
  root.right.left=Node(90)
  root.right.right=Node(400)
  
  print("Inorder traversal")
  Inorder(root)
  print("Postorder traversal")
  Postorder(root)
  print("Preorder traversal")
  Preorder(root)