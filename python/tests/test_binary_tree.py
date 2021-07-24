from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree

"""
My Tests
"""
def test_pre_order_search():
  my_search = BinarySearchTree()
  my_search.add(15)
  my_search.add(1)
  my_search.add(32)
  my_search.add(10)
  actual = my_search.pre_order_traverse()
  expected = [15,1,10,32]
  assert actual == expected

def test_in_order_search():
  my_search = BinarySearchTree()
  my_search.add(12)
  my_search.add(15)
  my_search.add(87)
  my_search.add(5)
  my_search.add(10)
  actual = my_search.in_order_traverse()
  expected = [5,10,12,15,87]
  assert actual == expected

def test_post_order_search():
  my_search = BinarySearchTree()
  my_search.add(60)
  my_search.add(64)
  my_search.add(87)
  my_search.add(5)
  my_search.add(70)
  my_search.add(18)
  my_search.add(56)
  actual = my_search.post_order_traverse()
  expected = [56,18,5,70,87,64,60]
  assert actual == expected

def test_empty_tree():
  my_tree = BinaryTree()
  assert my_tree
  assert my_tree.count == 0

def test_empty_search():
  my_search = BinarySearchTree()
  assert my_search
  assert my_search.count == 0

def test_search_tree_with_root():
  my_search = BinarySearchTree()
  my_search.add(15)
  actual = my_search.root
  expected = 15
  assert actual == expected
  assert my_search.count == 1

def test_adding_nodes_to_root():
  this_search = BinarySearchTree()
  this_search.add(15)
  this_search.add(1)
  this_search.add(32)
  actual = this_search.root
  expected = 15
  assert this_search.count == 3
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

  """"
  starter code tests
  """


def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"

def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left_child is None

def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right_child is None

def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None

def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree