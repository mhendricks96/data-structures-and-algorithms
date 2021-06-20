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


    def includes(self, key):
        """
        returns a boolean depending on whether value exists in a nodes value somewhere in the list
        """
        current = self.head
        while current.value is not None:
            if current.value == key:
                return True
            current = current.next
