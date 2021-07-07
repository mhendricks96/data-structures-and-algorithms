class Node:
    """
    Created empty node with the next set to none
    """
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
        """
        adds neew node to end of linked list
        """
        new_node = Node(value)
        current = self.head
        if current is None:
          current = new_node
        else:
          while current.next is not None:
             current = current.next
          current.next = new_node

    def append_after_value(self, value, new_value):
        """
        adds new node after a given value
        """
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
        """
        adds new node before a given value
        """
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
        returns a boolean depending on whether value exists in a node's value somewhere in the list
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

