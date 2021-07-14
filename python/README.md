# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`

## Reverse an List

Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

### Whiteboard Process for reverse List

![Python Code Challenge 1](https://user-images.githubusercontent.com/75649765/121122214-e04c7280-c7d5-11eb-97bb-9d1a292966cd.png)

### Approach & Efficiency for reverse list

we used a while loop to iterate through our array and return the last index to new array

## Insert to Middle of an list

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

### Whiteboard Process for insert to middle of list

![Python Code Challenge 1](https://user-images.githubusercontent.com/75649765/121751465-0c604000-cac3-11eb-9b3b-d15faeb52395.png)

### Approach & Efficiency for insert to middle

divided the len of the list by 2 to get the middle index and inserted the inputed calue there.

## Binary Search of Sorted Array

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

### Whiteboard Process for binary search

![Python Code Challenge 3](https://github.com/mhendricks96/data-structures-and-algorithms/files/6652669/challenge.3.whiteboard.pdf)

### Approach & Efficiency for binary search

using a recursive function awe found the middle of the list that compared that value to out key to decide which side of the list to contue our function on

## Singly Linked List

Using functions to create a singly linked list full of custom nodes

### Singly Linked List Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

### Approach & Efficiency for singly linked lists

used test driven development to full linked list class with functions



## Challenge Summary for singly lists continued

Write the following methods for the Linked List class:

.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

### Whiteboard Process for more singly linked lists

![Screen Shot 2021-06-21 at 10 17 05 PM 2](https://user-images.githubusercontent.com/75649765/122870320-5d9dda00-d2e2-11eb-8808-561f3c0a64dd.png)

### Approach & Efficiency for more singly linked lists

traversed through linked list and changed pointers to insert new values.

Collaborated with Marie Marcos

## Challenge Summary for code challenge 7

write a function that takes in a integer(k) as an argument and returns the node's value that is k places from the end of a linked list

### Whiteboard Process for code challenge 7

![challenge 7 whiteboard](https://user-images.githubusercontent.com/75649765/123350825-a1762680-d510-11eb-82e6-08b6443806e8.png)

### Approach & Efficiency for code challenge 7

taversed through the linked list to find the length, then subtracted the inputed number from the length to figure out which node was to be returned 

### Solution for code challenge 7

[link to function](python/linked_list/linked_list.py)

## Challenge Summary for code challenge 8

Write a function called zip lists, that takes in two linked lists as arguments and returns a linked list zipped. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list

### Whiteboard Process for code challenge

![challenge 8 whiteboard](https://github.com/mhendricks96/data-structures-and-algorithms/files/6730914/linked-list-zip.pdf)

### Approach & Efficiency for code challenge 8

used pointers to switch between lists

### Solution for code challenge 8

[link to function](python/linked_list/linked_list.py)

## Stacks and Queues

Stacks and queues are both data structures. I created a class for each one

### Stacks and Queues Challenge

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Challenge Summary CC 12

create a first in, first out animal shelter 

### Whiteboard Process

[whitboard](https://github.com/mhendricks96/data-structures-and-algorithms/issues/60)

### Approach & Efficiency

traversed through array and returned any node matching the preference. any node that was not matching was added to the end of the queue. after the correct node was found, the queue was rotated to bring the appropriate nodes to the fron

### Solution

[link to function](python/animal_shelter/animal_shelter.py)
