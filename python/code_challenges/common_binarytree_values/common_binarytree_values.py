from hash_table.hash_table import HashTable
from hash_table_dict.hash_table_dict import HashTableDict
#from linked_list.linked_list import LinkedList, Node
from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree



def tree_intersection(tree1, tree2):
  my_hashtable = HashTable()
  common_values = []
  tree1_set = set(tree1.post_order_traverse([]))
  tree2_set = set(tree2.post_order_traverse([]))
  common_list = list(tree2_set & tree1_set)
  
  return common_list



def solve_it_with_sets(tree1, tree2):
  tree1_set = set(tree1.post_order_traverse([]))
  tree2_set = set(tree2.post_order_traverse([]))

  common_values = list(tree2_set & tree1_set)
  
  return common_values

