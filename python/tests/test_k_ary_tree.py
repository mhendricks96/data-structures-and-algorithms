from k_ary_tree.k_ary_tree import KaryTree, Node, Queue
import pytest


def test_tree_with_single_node():
  my_tree = KaryTree(8)
  #my_tree.children.append(KaryTree(9))
  assert my_tree.count == 1


# def test_level_order_traversal(my_tree):
  
#   actual = my_tree.level_order()
#   expected = [8,12,10,7,15]
#   assert actual == expected

def test_level_order_traversal_2(my_big_tree):
  
  actual = my_big_tree.level_order()
  expected = [8,12,10,7,15,99,50]
  assert actual == expected






##########
# Fixtures
##########

@pytest.fixture
def my_tree():
  my_tree = KaryTree(8)
  my_tree.children.append(KaryTree(12))
  my_tree.children.append(KaryTree(10))
  my_tree.children.append(KaryTree(7))
  my_tree.children.append(KaryTree(15))
  return my_tree

@pytest.fixture
def my_big_tree():
  my_big_tree = KaryTree(8)
  my_big_tree.children.append(KaryTree(12))
  my_big_tree.children.append(KaryTree(10))
  my_big_tree.children.append(KaryTree(7))
  my_big_tree.children.append(KaryTree(15))
  my_big_tree.children[0].children.append(KaryTree(99))
  my_big_tree.children[2].children.append(KaryTree(50))
  return my_big_tree

  @pytest.fixture(autouse=True)
  def clean():
    my_tree = None
    my_big_tree = None