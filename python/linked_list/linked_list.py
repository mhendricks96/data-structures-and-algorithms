class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    creating a new Linked List with a head property
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += f"{ {current.value} } -> "
            current = current.next

        string += f"NULL"
        return string
        

    def insert(self, value):
        """
        adds new node to the head of list
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node


    def append_to_end(self, value):
       new_node = Node(value)
       current = self.head
       if current is None:
          current = new_node
       else:
          while current.next is not None:
             current = current.next
          current.next = new_node

    def append_after_value(self, value, new_value):
        current = self.head
        while current.next is not None:
            if value == current.value:
                break
            current = current.next
        if current is None:
            print("cant find it")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node 
        
    def append_before_value(self, value, new_value):
        current = self.head
        while current.next is not None:
            if value == current.next.value:
                break
            current = current.next
        if current is None:
            print("cant find it")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node 
    
    
    def includes(self, key):
        """
        returns a boolean depending on whether value exists in a nodes value somewhere in the list
        """
        current = self.head
        while current.value is not None:
            if current.value == key:
                return True
            current = current.next
    

    def kth_from_end(self, k):
        """
        takes in an integer and returns the value of the node that many spots from the end of the linked list
        """
        
        length = -1
        temp = self.head
        while temp is not None:
            temp = temp.next
            length += 1
        if length < 2:
            return 'omg this is embarassing but the list only has 1 item....awkward'
        elif k < 0:
            return 'what is this calculus? choose a positive number'
        elif k >= length:
            return 'the list is not that long. choose a smaller number'
        else:
            temp = self.head
            target = length - k
            for i in range(0, target):
                temp = temp.next
            return temp.value

    def find_middle_node(self):
        """
        returns the value of the node at the middle voue (rounding down) of the linked list
        """
        length = -1
        temp = self.head
        while temp is not None:
            temp = temp.next
            length += 1
        if length < 2:
            return 'omg this is embarassing but the list only has 1 item....awkward'
        else:
            temp = self.head
            target = int(length/2)
            for i in range(0, target):
                temp = temp.next
            return temp.value



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

## Linked List Stack

#class isEmptyError(Exception):
    #pass

class LL_Stack:
    
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, top=None):
        self.top = top
        self.stack_size = 0

    def __len__(self):
        return self.stack_size

    def is_empty(self):
        #Shorthand
        #return self.stack_size == 0
        if self.stack_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return ("Sorry, the stack is empty")
        return self.top.value
    
    def push(self, value):
        self.top = self.Node(value, self.top)
        self.stack_size += 1

    def pop(self):
        if self.is_empty():# is True:
            return ("Sorry, the stack is empty")
        
        popped = self.top.value
        self.top = self.top.next
        self.stack_size -= 1
        return popped



# Linked List Queue

class LL_Queue:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
    
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.queue_size = 0

    def __len__(self):
        return self.queue_size

    def is_empty(self):
        #Shorthand
        return self.queue_size == 0
        # if self.stack_size == 0:
        #     return True
        # else:
        #     return False

    def peek(self):
        if self.is_empty():
            return ("Sorry, the queue is empty")
        return self.front.value

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.queue_size += 1

    def dequeue(self):
        if self.is_empty():
            return ("Sorry, the queue is empty")
        result = self.front.value
        self.front = self.front.next
        self.queue_size -= 1
