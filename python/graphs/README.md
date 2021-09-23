# Graphs

Graphs are a non linear data structure. It consists of nodes with values and edges with weights that connect the nodes

## Challenge

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node to add a new node to the graph

- add edge to add a new edge to the graph

- get nodes to return a list of all nodes in the graphs

- get neighbors that takes in a node and returns a dictionary with all of that nodes edge neighbors along with the weights that correspond with those edges.

- size which returns the total number of nodes in the graph

## Approach & Efficiency

created a graph with a dictionary to hold all the nodes and their edges. added a node to the graph is basically just adding a new key to the dictionary and adding edges to a node is just adding values to that nodes values list.

## Challenge 36 Breadth First Traversal

- write a function for the Graph class that traverses bread first, takes in a Node as as argument and returs a list of the nodes in the order they were visited along with displating the list

### Approach & Efficiency

Used a queue along with a "visited nodes" set to go through the every node in the graph and all of its neighbors.
