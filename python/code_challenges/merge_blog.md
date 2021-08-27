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
