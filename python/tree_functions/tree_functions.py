from binary_tree.binary_tree import BinarySearchTree

from ll_queue.ll_queue import LL_Queue


def breadth_first(BinarySearchTree):
  queue = LL_Queue()
  tree_values = []
  binary_tree = BinarySearchTree
  queue.enqueue(binary_tree.root)
  while queue.peek():
    front = queue.dequeue()
    if binary_tree.left_child:
      queue.enqueue(binary_tree.left_child)

    if binary_tree.right_child:
      queue.enqueue(binary_tree.right_child)
    
    current = front
    while current is not None:
      for number in current.value:
        tree_values.append(number)
      current = current.next

    

  return tree_values
