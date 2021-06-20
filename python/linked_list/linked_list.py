class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here

    "{ a } -> { b } -> { c } -> NULL"
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return f"{ self.head.value } -> { self.head.next.value } -> { self.head.next.next.value } -> NULL"

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
