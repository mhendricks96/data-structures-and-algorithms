# Sorting Algorithms

## Insertion Sort

Insertion Sort is a sorting algorithm that traverses a list and places each element in order by comparing it to the element preceding it.

### Insertion Sort Pseudocode

define insertion_sort(array)
  
  for loop that starts at index 1 and goes length of list

    define current spot
    
    define current position
    
    while loop than continues as long as current item is less than item before it and not the 0 index
      if so, flip current item with item before it

### Insertion Sort Example

sample_list = [8,4,23,42,16,15]

- first we start with '4' because it is the 1 index.

- compare '4' to what is behind it: 4 < 8. so we swap them

- result: [4,8,23,42,16,15]

- '4' is now at the 0 index, so we move to the 2 index

- compare '23' to what is behind it: 23 !< 8 so we leave them in place

- result: [4,8,23,42,16,15]

- now at the 3 index, we compare '42' to what is behind it: 42 !< 23 so we leave them in place

- result: [4,8,23,42,16,15]

- now at the 4 index, we compare '16' to what is behind it: 16 < 42 so we swap them

- result: [4,8,23,16,42,15]

- next we compare '16' to what is behind it: 16 < 23 so we swap them

- result: [4,8,16,23,42,15]

- next we compare '16' to what is behind it: 16 !< 8 so we leave them in place

- result: [4,8,16,23,42,15]

- now at the 5 index, we compare '15' to what is behind it: 15 < 42 so we swap them

- result: [4,8,16,23,15,42]

- next we compare '15' to what is behind it: 15 < 23 so we swap them

- result: [4,8,16,15,23,42]

- next we compare '15' to what is behind it: 15 < 16 so we swap them

- result: [4,8,15,16,23,42]

- next we compare '15' to what is behind it: 15 !< 8 so we leave them in place

We have now completed our original for-loop through the list and have our ordered list: [4,8,15,16,23,42]

### Links to Insertion Sort function and tests

[link to function](./insertionSort.js)

[link to tests](./insertionSort.test.js)