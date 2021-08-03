from k_ary_tree.k_ary_tree import KaryTree
import pytest


def test_tree_with_single_node():
  my_tree = KaryTree(8)
  #my_tree.children.append(KaryTree(9))
  assert my_tree.count == 1

def test_level_order_traversal():
  my_tree = KaryTree(8)
  my_tree.children.append(KaryTree(9))
  my_tree.children.append(KaryTree(10))
  actual = my_tree.level_order()
  expected = [8,9,10]
  assert actual == expected

# def test_pre_order_1_node():
#   my_tree = KaryTree()
#   my_tree.insert(8)
#   actual = my_tree.pre_order_traversal()
#   expected = [8]
#   assert actual == expected

# def test_adding_many_nodes():
#   my_k_tree = KaryTree()
#   my_k_tree.insert(15)
#   my_k_tree.insert(88,15)
#   my_k_tree.insert(123,15)
#   my_k_tree.insert(2,88)
#   assert my_k_tree.count == 4

# def test_pre_order_traversal():
#   my_k_tree = KaryTree()
#   my_k_tree.insert(15)
#   my_k_tree.insert(88,15)
#   my_k_tree.insert(123,15)
#   my_k_tree.insert(2,88)
#   actual = my_k_tree.pre_order_traversal()
#   expected = [15, 88, 2, 123]
#   assert actual == expected


# def test_adding_fixture(my_tree):
#   assert my_tree.count == 6

# def test_pre_order_traversal(my_tree):
#   actual = my_tree.pre_order_traversal
#   expected = []




##########
# Fixtures
##########

@pytest.fixture
def my_tree():
  my_tree = KaryTree()
  my_tree.insert(17)
  my_tree.insert(99,17)
  my_tree.insert(123,99)
  # my_tree.insert(2,99)
  # my_tree.insert(15,17)
  # my_tree.insert(88,17)
  return my_tree


  @pytest.fixture(autouse=True)
  def clean():
    my_tree = None