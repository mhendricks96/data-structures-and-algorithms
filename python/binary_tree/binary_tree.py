class Node:

  def __init__(self, value=None, left_child=None, right_child=None):
    self.value = value
    self.left_child = left_child
    self.right_child = right_child

class BinaryTree:
  
  # def __init__(self, root=None):
  #   self.root = root

  
  
  def pre_order_traverse():
    pass

  def in_order_traverse():
    pass

  def post_order_traverse():
    pass

  def level_order_traverse():
    pass


class BinarySearchTree(BinaryTree):
  
  def __init__(self, root=None,):
    # super().__init__(root=None,)
    self.root = root
    self.left_child = None
    self.right_child = None

  def add(self, value):
    """
    Adds a new node with that value in the correct location in the binary search tree.
    """
    # check if tree is empty
    if self.root is None:
      #if so, new node becomes the root
      self.root = value
      return

    if self.root == value:
      # not sure what to do with duplicates yet
      #can change below comparison to "less than or equal to, or use a counter"
      pass
      return

      
    if self.root > value:
      #got to left subtree
      #check if left subtree is empty
      #run add() recursively on the left subtree
      if self.left_child:
        self.left_child.add(value)
      else:
        self.left_child = BinarySearchTree(value)

    else:
      #go to right subtree
      #run add() recursevly on right subtree
      if self.right_child:
        self.right_child.add(value)
      else:
        self.right_child = BinarySearchTree(value)


  def contains(self, value):
    """
    Returns: boolean indicating whether or not the value is in the tree at least once.

    """
    if self.root == value:
      return True

    if self.root > value:
      if self.left_child:
        return self.left_child.contains(value)
      else:  
        return False
      
    else:
      if self.right_child:
        return self.right_child.contains(value)
      else:
        return False
