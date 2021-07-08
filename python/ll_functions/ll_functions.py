from linked_list.linked_list import LinkedList, Node
from ll_stack.ll_stack import LL_Stack

def zipped_list(list1, list2):
    """
    function takes in 2 linked lists and returns a list with both link lists zippered together
    """
    list1_curr = list1.head
    list2_curr = list2.head
  
    while list1_curr != None and list2_curr != None:   
        list1_next = list1_curr.next
        list2_next = list2_curr.next
           
        list2_curr.next = list1_next 
        list1_curr.next = list2_curr 
      
        list1_curr = list1_next
        list2_curr = list2_next
    list2.head = list2_curr

class PsuedoQueue:
    """creates  queue from 2 stacks"""
    def __init__(self):#, front=None, rear=None):
        # self.front = front
        # self.rear = rear
        self.queue_size = 0
        # self.in_stack = self.LL_Stack()
        # self.out_stack = self.LL_Stack()
        self.in_stack = LL_Stack()
        self.out_stack = LL_Stack()

    def __len__(self):
        """keeps tack of length of queue"""
        return self.queue_size


    def enqueue(self, value):
        """adds new node to the top of in_stack"""
        self.in_stack.push(value)
        self.queue_size += 1 
    
    def dequeue(self):
        """removes node from rear of Psuedocode"""
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        self.queue_size -= 1
        popped = self.out_stack.pop()
        return popped
        

 






        # if self.is_empty():
        #     return ("Sorry, the queue is empty")
        # result = self.front.value
        # self.front = self.front.next
        # self.queue_size -= 1
        # return result


# def merge_sorted_list(list1, list2):
    
#     """
#     function takes in 2 ordered linked lists and returns an ordered link list containing all the nodes from both lists
#     (recursive)
#     """
#     current1 = list1.head
#     current2 = list2.head
#     if current1 is None:
#         return list2
#     if current2 is None:
#         return list1

#     if (current1.value < current2.value):
#         current1.next = merge_sorted_list(current1.next, list2)
#         return list1
#     else:
#         current2.next = merge_sorted_list(current2.next, list1)
#         return list2