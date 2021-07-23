from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree

def test_empty_tree():
  my_tree = BinaryTree()
  assert my_tree

def test_empty_search():
  my_search = BinarySearchTree()
  assert my_search

def test_search_tree_with_root():
  my_search = BinarySearchTree()
  my_search.add(15)
  actual = my_search.root.value
  expected = 15
  assert actual == expected

def test_adding_nodes_to_root():
  my_search = BinarySearchTree()
  my_search.add(15)
  my_search.add(1)
  my_search.add(32)
  actual = my_search.root.value
  expected = 15
  assert actual == expected

def test_adding_many_nodes():
  my_search = BinarySearchTree()
  my_search.add(19)
  my_search.add(1)
  my_search.add(32)
  my_search.add(17)
  my_search.add(6)
  my_search.add(18)
  actual = my_search.root.value
  expected = 19
  assert actual == expected

