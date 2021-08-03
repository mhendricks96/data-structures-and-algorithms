from ll_queue.ll_queue import LL_Queue

class KNode:
  def __init__(self, value=None, children=[]):
    self.value = value
    self.children = children


class KaryTree:
  def __init__(self, root=None):
    self.root = root
    self.count = 1
 
  def level_order(self):
    values_list = []
    queue = LL_Queue()

    queue.enqueue(self.root)
    while not queue.is_empty():

      front = queue.dequeue()
      # if front == None:
      #       continue
      for child in front.children:
        queue.enqueue(child)
      values_list.append(front.value)
      

    return values_list

