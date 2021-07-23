class Node:

  def __init__(self, value=None, left_child=None, right_child=None):
    self.value = value
    self.left_child = left_child
    self.right_child = right_child

class BinaryTree:
  
  def __init__(self, root=None):
    self.root = root

  
  
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
    super().__init__(root=None,)

  def add(self, value=None,):
    """
    Adds a new node with that value in the correct location in the binary search tree.
    """
    #new_node = Node(value)
    #current = self.root
    # check if tree is empty
    if self.root is None:
      #if so, new node becomes the root
      self.root = Node(value)
      return

    elif self.root.value == value:
      # not sure what to do with duplicates yet
      pass
      return

    
    elif self.root.value < value:
      #go to right subtree
      #run add() recursevly on right subtree
      if self.root.right_child:
        self.right_child.add(value)
      

    else:
      #got to left subtree
      #check if left subtree is empty
      #run add() recursively on the left subtree
      if self.root.left_child:
        self.left_child.add(value)



  def contains(self, value=None):
    """
    Returns: boolean indicating whether or not the value is in the tree at least once.

    """
    pass