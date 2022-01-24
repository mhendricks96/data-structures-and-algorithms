# Stacks and Queues

- Stacks are data structures that follow the Last-In-First-Out (LIFO) principle, meaning the last item inserted into a stack is the first one to be deleted.

- A queue is an ordered list of elements where an element is inserted at the end of the queue and is removed from the front of the queue. A queue works based on the first-in, first-out (FIFO) principle.

- A PsudoQueue is a queue that is implemented using 2 stacks.

## Challenge

- Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

- Impement a Queue using 2 Stacks

## API

### Stack

#### push()

- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.

#### pop()

- Arguments: none

- Returns: the value from node from the top of the stack

- Removes the node from the top of the stack

- Should raise exception when called on empty stack

#### peek()

- Arguments: none

- Returns: Value of the node located at the top of the stack

- Should raise exception when called on empty stack

#### is_empty()

- Arguments: none

- Returns: Boolean indicating whether or not the stack is empty.

### Queue

#### enqueue()

- Arguments: value

- adds a new node with that value to the back of the queue with an O(1) Time performance.

#### dequeue()

- Arguments: none

- Returns: the value from node from the front of the queue

- Removes the node from the front of the queue

- Should raise exception when called on empty queue

#### peek ()

- Arguments: none

- Returns: Value of the node located at the front of the queue

- Should raise exception when called on empty queue

#### is_empty ()

- Arguments: none

- Returns: Boolean indicating whether or not the queue is empty.

### PsudoQueue

#### enqueue ()

- Arguments: value

- Inserts value into the PseudoQueue, using a first-in, first-out approach.

#### dequeue ()

- Arguments: none

- Extracts a value from the PseudoQueue, using a first-in, first-out approachh.
