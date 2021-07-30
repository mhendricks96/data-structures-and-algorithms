from binary_tree.binary_tree import BinarySearchTree

from ll_queue.ll_queue import LL_Queue


def breadth_first(tree):
    values_list = []
    queue = LL_Queue()

    queue.enqueue(tree)
    while queue:
        front=queue.dequeue()
        if front==None:
            continue
        values_list.append(front.root)
        queue.enqueue(front.left_child)
        queue.enqueue(front.right_child)
    
    return values_list