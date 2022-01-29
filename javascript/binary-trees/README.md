# Binary Trees

a binary tree is a tree data structure in which each node has at most two children

## Binary Tree

### BT API

#### pre-order()

Returns: an array of the values with the root first

#### in-order()

Returns: an array of the values with the root second

#### post-order()

Returns: an array of the values with the root last

## Binary Search Tree

a SUB_CLASS of binary tree except every node only has values less than it to the left and greater than it to the right.

### BST API

### pre-order() - inherited

Returns: an array of the values with the root first

### in-order() - inherited

Returns: an array of the values with the root second

### post-order() - inherited

Returns: an array of the values with the root last

### add()

Arguments: value
Adds a new node with the given value to the correct location in binary search tree

## contains()

Argument: value
Returns: a boolean indicating whether or not the value is in the tree at least once.
