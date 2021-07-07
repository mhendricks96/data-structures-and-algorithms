from linked_list.linked_list import LinkedList, Node

## Linked List Stack

#class isEmptyError(Exception):
    #pass

class LL_Stack:
    """
    creates a stack based on a linked list
    """
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, top=None):
        self.top = top
        self.stack_size = 0

    def __len__(self):
        """
        keeps track of length of stack
        """
        return self.stack_size

    def is_empty(self):
        """
        checks to see if stack is empty
        """
        #Shorthand
        #return self.stack_size == 0
        if self.stack_size == 0:
            return True
        else:
            return False

    def peek(self):
        """
        returns value of node at top of stack
        """
        if self.is_empty():
            return ("Sorry, the stack is empty")
        return self.top.value
    
    def push(self, value):
        """
        adds new node to top of stack
        """
        self.top = self.Node(value, self.top)
        self.stack_size += 1

    def pop(self):
        """
        removes top node from stack and returns its value
        """
        if self.is_empty():# is True:
            return ("Sorry, the stack is empty")
        
        popped = self.top.value
        self.top = self.top.next
        self.stack_size -= 1
        return popped