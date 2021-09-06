# Hashtables

A hashtable is a table that is designed to efficiently store non-contiguous keys along with their respective values

## Challenge

Implement a Hashtable Class with the following methods:

### add

Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

### get

Arguments: key
Returns: Value associated with that key in the table

### contains

Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

### hash

Arguments: key
Returns: Index in the collection for that key

## Approach & Efficiency

I created a hashtable that is a collection of linked lists. each linked list contains all the items with the same index number. within the nodes of the linked lists are lists that contain a key and the value associated with that key
