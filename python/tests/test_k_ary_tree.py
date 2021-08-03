from k_ary_tree.k_ary_tree import KaryTree, KNode
from ll_queue.ll_queue import LL_Queue
import pytest


def test_single_node():
  node = KNode(8)
  assert node
  assert node.value == 8

def test_empty_tree():
  new_tree = KaryTree()
  assert new_tree
  assert new_tree.root == None

def test_tree_with_single_node():
  my_tree = KaryTree(8)
  assert my_tree.count == 1
  assert my_tree.root == 8


def test_level_order_traversal(my_tree):
  
  actual = my_tree.level_order()
  expected = [12,17, 21, 5, 8, 30, 15, 10]
  assert actual == expected

# def test_level_order_traversal_2(my_big_tree):
  
#   actual = my_big_tree.level_order()
#   expected = [8,12,10,7,15,99,50]
#   assert actual == expected






##########
# Fixtures
##########

@pytest.fixture
def my_tree():
  node3 = KNode(30)
  node4 = KNode(17)
  node5 = KNode(10)
  node6 = KNode(15)
  node7 = KNode(5,[node3, node6])
  node8 = KNode(8,[node5])
  node2 = KNode(21,[node7, node8])
  node1 = KNode(12,[node4, node2])
  my_tree = KaryTree(node1)
  return my_tree

@pytest.fixture
def my_big_tree():
  my_big_tree = KaryTree(8)
  my_big_tree.value.children.append(KNode(12))
  my_big_tree.children.append(KNode(10))
  my_big_tree.children.append(KNode(7))
  my_big_tree.children.append(KNode(15))
  my_big_tree.children[0].children.append(KNode(99))
  my_big_tree.children[2].children.append(KNode(50))
  return my_big_tree

  @pytest.fixture(autouse=True)
  def clean():
    my_tree = None
    my_big_tree = None