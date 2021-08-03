#from ll_queue.ll_queue import LL_Queue

class Node:
  def __init__(self, value=None, next=None, children=[]):
    self.value = value
    self.children = children
    self.next = next

class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.queue_size = 0

    def __len__(self):
        """keeps tack of length of queue"""
        return self.queue_size

    def is_empty(self):
        """checks to see if queue is empty""" 
        return self.queue_size == 0


    def enqueue(self, value):
        """adds new node to rear of queue"""
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.queue_size += 1

    def dequeue(self):
        """
        removes node from front of queue and returns the result
        """
        if self.is_empty():
            return ("Sorry, the queue is empty")
        result = self.front.value
        self.front = self.front.next
        self.queue_size -= 1
        return result



class KaryTree:
  def __init__(self, root=None, children=[]):
    self.root = root
    self.children = children
    self.count = 1
 
  def level_order(self):
    values_list = [self.root]
    queue = Queue()

    queue.enqueue(self)
    while not queue.is_empty():

      front = queue.front
      if front == None:
            continue
      for child in front.children:
        queue.enqueue(child.root)
      values_list.append(front.value.root)
      queue.dequeue()

    return values_list

