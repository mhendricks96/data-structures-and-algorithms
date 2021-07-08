from linked_list.linked_list import LinkedList, Node

# Linked List Queue

class LL_Queue:
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
        self.queue_size = 0

    def __len__(self):
        """keeps tack of length of queue"""
        return self.queue_size

    def is_empty(self):
        """checks to see if queue is empty"""
        #Shorthand
        return self.queue_size == 0
        # if self.stack_size == 0:
        #     return True
        # else:
        #     return False

    def peek(self):
        """
        returns the value of the front node of the queue
        """
        if self.is_empty():
            return ("Sorry, the queue is empty")
        return self.front.value

    def enqueue(self, value):
        """adds new node to rear of queue"""
        new_node = self.Node(value)
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
