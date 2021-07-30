from tree_functions.tree_functions import breadth_first
from ll_queue.ll_queue import LL_Queue
from binary_tree.binary_tree import BinarySearchTree

def test_breadth_first():
  my_tree = BinarySearchTree()
  values_list = [17,1738,52,16,6,888]
  for number in values_list:
     my_tree.add(number)
  actual = breadth_first(my_tree)
  expected = [17,16,1738,6,52,888]
  assert actual == expected






##########
# Fixtures
##########

# @pytest.fixture
# def my_tree():
#   my_tree = BinarySearchTree()
#   values_list = [17,1738,52,16,6,888]
#   for number in values_list:
#     my_tree.add(number)
#   return my_tree


#   @pytest.fixture(autouse=True)
#   def clean():
#     my_tree = None