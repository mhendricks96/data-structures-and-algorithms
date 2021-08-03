from ll_queue.ll_queue import LL_Queue

# class Node:
#   def __init__(self, value=None, children=[]):
#     self.value = value
#     self.children = children

class KaryTree:
  def __init__(self, root=None, children=[]):
    self.root = root
    self.children = children
    self.count = 1
 
  def level_order(self):
    values_list = [self.root]
    queue = LL_Queue()

    queue.enqueue(self)
    while queue:
      front=queue.dequeue()
      if front==None:
            continue
      for child in front.children:
        values_list.append(child.root)

    return values_list

