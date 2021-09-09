from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree
from hash_table.hash_table import HashTable
from hash_table_dict.hash_table_dict import HashTableDict
from code_challenges.common_binarytree_values.common_binarytree_values import tree_intersection, solve_it_with_sets
import pytest


def test_sets_solution():
  this_tree = BinarySearchTree()
  that_tree = BinarySearchTree()

  values_list = [17,1738,77,16,9,80]
  for number in values_list:
    this_tree.add(number)

  values_list2 = [17,55,52,16,6,80]
  for number in values_list2:
    that_tree.add(number)
  
  actual = solve_it_with_sets(this_tree, that_tree)
  expected = [16,17,80]
  assert actual == expected

