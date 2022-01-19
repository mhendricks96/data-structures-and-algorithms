# Singly Linked List

A linked list is a set of connected nodes. each node has a value and knows what the next node is.

## Implementaion- CC 5

Implement a singly linked list with a node class and a linkedlist class. the linkes list class should have the following methods: insert, includes, and to_string.

## Insertions CC 6

Write the following methods for the Linked List class: append, insert before, insert after.

## Kth from the end

write the following methods for the Linked List class: kth from end

## API

### insert()

Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.

### includes()

Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.

### to_string()

Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

### append()

Arguments: new value
Adds a new node with the given value to the end of the list

## insertBefore()

Argument: value, new value
adds a new node with the given new value immediately befor the first node that has the value specified.

## insertAfter()

Argument: value, new value
adds a new node with the given new value immediately afer the first node that has the value specified.

## kth from end()

argument: a number, k, as a parameter.
Returna the node’s value that is k places from the tail of the linked list.
