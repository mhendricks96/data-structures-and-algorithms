class Node:
  """
  emoty node class
  """
  def __init__(self, value=None, left_child=None, right_child=None):
    self.value = value
    self.left_child = left_child
    self.right_child = right_child

class BinaryTree:
  """
  class to create empty binary tree and traverse through it
  """
  
  def __init__(self, root=None):
    self.root = root
    self.left_child = None
    self.right_child = None
    self.count = 0
    
  
  def pre_order_traverse(self, node_list=[]):
    #append root node to node_list
    node_list.append(self.root)
    #traverse left subtree
    if self.left_child:
      self.left_child.pre_order_traverse(node_list)
    #traverse right subtree
    if self.right_child:
      self.right_child.pre_order_traverse(node_list)
    return node_list

  def in_order_traverse(self, node_list=[]):
    #traverse left subtree
    if self.left_child:
      self.left_child.in_order_traverse(node_list)
    #append rood node to nodelist
    node_list.append(self.root)
    #traverse right subtree
    if self.right_child:
      self.right_child.in_order_traverse(node_list)
    return node_list

  def post_order_traverse(self, node_list=[]):
    #traverse left subtree
    if self.left_child:
      self.left_child.post_order_traverse(node_list)
    #traverse right subtree
    if self.right_child:
      self.right_child.post_order_traverse(node_list)
    #append rood node to nodelist
    node_list.append(self.root)
    return node_list


  def maximum_value(self):
    values = self.in_order_traverse()
    max_value = 0

    for value in values:
      if value > max_value:
        max_value = value
    return max_value

  def minimum_value(self):
    values = self.post_order_traverse()
    min_value = values[0]

    for value in values:
      if value < min_value:
        min_value = value
    return min_value



  def delete_node(self, value):
    """
    can be used to delete any node other than the main root
    """
    if self.root is None:
      print("The tree is empty")
      return
    if value < self.root:
      if self.left_child:
        self.left_child = self.left_child.delete_node(value)
      else:
        print(f"sorry, couldnt find {value}")
        return
    elif value > self.root:
      if self.right_child:
        self.right_child = self.right_child.delete_node(value)
      else:
        print(f"sorry, couldnt find {value}")
        return
    else:
      #after all the recursion above, this should be the node i want to delete.
      """
      these will delete any node with 0 or 1 child
      """
      if self.left_child is None:
        temp = self.right_child
        self = None
        return temp
      if self.right_child is None:
        temp = self.left_child
        self = None
        return temp

      """
      these will delete node with 2 children and replace it with largest node in left subtree or (in this case -->)smallest node in right subtree
      """

      node = self.right_child
      while node.left_child:
        node = left_child
      self.root = node.root
      self.right_child = self.right_child.delete_node(node.root)

    return self

    print(f"{value} deleted")



class BinarySearchTree(BinaryTree):
  """
  subclass of binary tree to create an empty binary search tree as well as add and contain methods
  """


  def add(self, value):
    """
    Adds a new node with that value in the correct location in the binary search tree.
    """
    # check if tree is empty
    if self.root is None:
      self.root = value
      self.count += 1
      return

    if self.root == value:
      # not sure what to do with duplicates yet
      #can change below comparison to "less than or equal to, or use a counter"
      pass
      return

      
    if self.root > value:
      #check if left subtree is empty
      #run add() recursively on the left subtree
      if self.left_child:
        self.left_child.add(value)
      else:
        self.left_child = BinarySearchTree(value)
        self.count += 1
    else:
      #run add() recursevly on right subtree
      if self.right_child:
        self.right_child.add(value)
      else:
        self.right_child = BinarySearchTree(value)
        self.count += 1

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
