# Merge Sort

## Description

In a merge sort function, the list elements are split into 2 halves over and over again, until each item is a "sub-list of only 1 or 2.

At that point the "sub-lists" are merged back together by comparing each element from left to right  until the list is back together.

## Merge sort psuedocode

define merge sort (list)

  if statement to run function recursively until every sublist is only 1 element
  
      find middle point of lists

      create left sublist with everything before the middle

      create right sublist with everything middle and after

      recursively run function on right sublist

      recursively run function on left sublist

      create variables to hold indexes of left,right, and starting lists respectively

      while loop to that goes until list is merged

        check if current index in left sublist is less than current index in right sublist

          if true - 
              move element to current index in starting list

              move to next index in left sublist

              move to next index in starting sublist

          if false - 
              move element from right sublist to starting list

              move to next index in left sublist

              move to next index in starting sublist
      
      add anything left on either list to the end of the start list

## Merge Sort Example

sample_list = [8,4,23,42,16,15]

- first we find the middle index of the list by dividing the length of the list by 2. 6/2 = 3(number '42')

- we use that to separate the list into 2 sublists

[8,4,23] [42,16,15]

- recursively find the middle index of the left sublist by dividing its length by 2. 3/2 = 1(number '4')

- we use that to separate the list into 2 sublists

[8] [4,23] [42,16,15]

- recursively find the middle index of the rest of the left sublist by dividing its length by 2. 2/2 = 1(number '23')

- we use that to separate the list into 2 sublists

[8] [4] [23] [42,16,15]

- recursively find the middle index of the right sublist by dividing its length by 2. 3/2 = 1(number '16')

- we use that to separate the list into 2 sublists

[8] [4] [23] [42] [16,15]

- recursively find the middle index of the rest of the right sublist by dividing its length by 2. 2/2 = 1(number '15')

- we use that to separate the list into 2 sublists

[8] [4] [23] [42] [16] [15]

- all of our sublists are only 1 element, so we are ready to start merging.

- first we check if 8 < 4. it is not, so 4 is put to the 0 index of their sublist

[4,8] [23] [42] [16] [15]

- next we check if 23 < 42. it is , so 23 is put to the 0 index of their sublist

[4,8] [23,42] [16] [15]

- first we check if 16 < 15. it is not, so 15 is put to the 0 index of their sublist

[4,8] [23,42] [15,16]

- now we can compare and merge the [4,8] [23,42] subtrees

- first we compare the 0 index of each sublist to see if 4 < 23. it is, so it becomes the 0 index of their sublist

[4] [8] [23,42] [15,16]

- next we compare the 0 index of each sublist to see if 8 < 23. it is, so it becomes the 1 index of their sublist

[4,8] [23,42] [15,16]

- since that sublist is now empty, we add the leftovers to the end of the new sublist

[4,8,23,42] [15,16]

- now we only have 2 ordered sublists left and we can merge them

- first we compare the 0 index of each sublist to see if 4 < 15. it is, so it becomes the 0 index of the final list

[4]
[8,23,42] [15,16]

- next we compare the 0 index of each sublist to see if 8 < 15. it is, so it becomes the 1 index of the final list

[4,8]
[23,42] [15,16]

- next we compare the 0 index of each sublist to see if 23 < 15. it is not, so 15 becomes the 2 index of the final list

[4,8,15]
[23,42] [16]

- next we compare the 0 index of each sublist to see if 23 < 16. it is not, so 16 becomes the 3 index of the final list

[4,8,15,16]
[23,42]

- since that sublist is now empty, we add the leftovers to the end of the final list

[4,8,15,16,23,42]

And we have a merge sorted list!!