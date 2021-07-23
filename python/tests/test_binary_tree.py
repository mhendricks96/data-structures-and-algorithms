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
  actual = my_search.root
  expected = 15
  assert actual == expected

def test_adding_nodes_to_root():
  my_search = BinarySearchTree()
  my_search.add(15)
  my_search.add(1)
  my_search.add(32)
  actual = my_search.root
  expected = 15
  assert actual == expected

def test_adding_many_nodes():
  my_search = BinarySearchTree()
  my_search.add(19)
  values_list = [17,1,32,16,6,18]
  for number in values_list:
    my_search.add(number)
  actual = my_search.root
  expected = 19
  assert actual == expected

def test_contains_found_1():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,32,16,6,18]
  for number in values_list:
    my_search.add(number)

  assert my_search.contains(32)

def test_contains_found_all():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,32,16,6]
  for number in values_list:
    my_search.add(number)

  assert my_search.contains(50)
  assert my_search.contains(17)
  assert my_search.contains(10)
  assert my_search.contains(32)
  assert my_search.contains(16)
  assert my_search.contains(6)

def test_contain_wrong_1():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,32,16,6,18]
  for number in values_list:
    my_search.add(number)

  assert not my_search.contains(99)

def test_contain_many_wrong():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,32,16,6]
  for number in values_list:
    my_search.add(number)

  assert not my_search.contains(7)
  assert not my_search.contains(15)
  assert not my_search.contains(33)
  assert not my_search.contains(77)
  assert not my_search.contains(86)
  assert not my_search.contains(99)