from ll_stack.ll_stack import LL_Stack

# class Animal:
#     def __init__(self, breed=None, name=None):
#       self.breed = breed
#       self.name = name

class AnimalShelter:
    """
    creates a queue based on a linked list
    """
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.holding_stack = LL_Stack()
        self.queue_size = 0
        self.nodes_rotated = 0

    def __len__(self):
        """keeps tack of length of queue"""
        return self.queue_size

    def is_empty(self):
        """checks to see if queue is empty"""
        return self.queue_size == 0

    def enqueue(self, animal):
        """adds new node to rear of queue"""
        new_node = self.Node(animal)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.queue_size += 1

    def dequeue(self, pref):
        """
        removes node from front of queue and returns the result
        """
        if self.is_empty():
            return ("Sorry, the queue is empty")
        next_up = self.front
        
        while next_up is not None: 
          if next_up.value == pref:
            chosen_animal = next_up.value
            next_up = next_up.next
            self.queue_size -= 1
            times_to_rotate = self.queue_size-self.nodes_rotated
            for i in range(times_to_rotate):
              temp = next_up.value
              next_up = next_up.next
              rotated_node = self.Node(temp)
              self.rear.next = rotated_node
              self.rear = rotated_node
            return chosen_animal
          else:
            wrong_animal = next_up.value
            if next_up.next is None:
              return "Null"
            next_up = next_up.next
            rotated_node = self.Node(wrong_animal)
            self.rear.next = rotated_node
            self.rear = rotated_node
            self.nodes_rotated += 1
          