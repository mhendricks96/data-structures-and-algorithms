from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree

import pytest

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
  #yield my_search

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

def test_delete_node():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,32,16,6]
  for number in values_list:
    my_search.add(number)
  assert my_search.contains(17)

  my_search.delete_node(17)
  assert not my_search.contains(17)

def test_delete_node_with_2_children():
  my_searchTree = BinarySearchTree()
  my_searchTree.add(12)
  my_searchTree.add(15)
  my_searchTree.add(87)
  my_searchTree.add(5)
  my_searchTree.add(20)
  
  assert my_searchTree.contains(15)
  
  my_searchTree.delete_node(15)
  assert not my_searchTree.contains(15)
  assert my_searchTree.contains(20)
  assert my_searchTree.contains(87)

def test_find_minimum_value():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,10,52,16,6,18]
  for number in values_list:
    my_search.add(number)
  
  actual = my_search.minimum_value()
  expected = 6
  assert actual == expected

def test_find_maximum_value():
  my_search = BinarySearchTree()
  my_search.add(50)
  values_list = [17,1738,52,16,6,888]
  for number in values_list:
    my_search.add(number)
  
  actual = my_search.maximum_value()
  expected = 1738
  assert actual == expected

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


# @pytest.fixture(autouse=True)
# def clean():
#   """runs before each test automatically
#   There's also a more advanced way to run code after each test as well
#   Check the docs for that. Hint: it uses yield
#   """
#   BinarySearchTree.node_list =[]
#   BinaryTree.node_list =[]
#   yield
#   BinarySearchTree.node_list =[]
#   BinaryTree.node_list =[]

