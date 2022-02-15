# Merge Sort

## Description

In a merge sort function, the array elements are split into 2 halves over and over again, until each item is a "sub-array" of only 1 or 2.

At that point the "sub-arrays" are merged back together by comparing each element from left to right  until the array is back together.

## Merge sort psuedocode

define merge sort (array)

  if statement to run function recursively until every subarray
 is only 1 element
  
      find middle point of arrays

      create left subarray with everything before the middle

      create right subarray with everything middle and after

      recursively run function on right subarray
    

      recursively run function on left subarray
    

      create variables to hold indexes of left,right, and starting arrays respectively

      while loop to that goes until array is merged

          check if current index in left subarray is less than current index in right subarray

            if true - 
              move element to current index in starting array

              move to next index in left subarray
            
              move to next index in starting subarray
            
            if false - 
              move element from right subarray to starting array
            
              move to next index in left subarray
            
              move to next index in starting subarray
            
      
      add anything left on either array to the end of the start array

## Merge Sort Example

sample_array = [8,4,23,42,16,15]

- first we find the middle index of the array by dividing the length of the array by 2. 6/2 = 3(number '42')

- we use that to separate the array into 2 subarrays

[8,4,23] [42,16,15]

- recursively find the middle index of the left subarray by dividing its length by 2. 3/2 = 1(number '4')

- we use that to separate the array into 2 subarrays

[8] [4,23] [42,16,15]

- recursively find the middle index of the rest of the left subarray by dividing its length by 2. 2/2 = 1(number '23')

- we use that to separate the array into 2 subarrays

[8] [4] [23] [42,16,15]

- recursively find the middle index of the right subarray by dividing its length by 2. 3/2 = 1(number '16')

- we use that to separate the array into 2 subarrays

[8] [4] [23] [42] [16,15]

- recursively find the middle index of the rest of the right subarray by dividing its length by 2. 2/2 = 1(number '15')

- we use that to separate the array into 2 subarrays

[8] [4] [23] [42] [16] [15]

- all of our subarrays are only 1 element, so we are ready to start merging.

- first we check if 8 < 4. it is not, so 4 is put to the 0 index of their subarray

[4,8] [23] [42] [16] [15]

- next we check if 23 < 42. it is , so 23 is put to the 0 index of their subarray

[4,8] [23,42] [16] [15]

- first we check if 16 < 15. it is not, so 15 is put to the 0 index of their subarray

[4,8] [23,42] [15,16]

- now we can compare and merge the [4,8] [23,42] subtrees

- first we compare the 0 index of each subarray to see if 4 < 23. it is, so it becomes the 0 index of their subarray

[4] [8] [23,42] [15,16]

- next we compare the 0 index of each subarray to see if 8 < 23. it is, so it becomes the 1 index of their subarray

[4,8] [23,42] [15,16]

- since that subarray is now empty, we add the leftovers to the end of the new subarray

[4,8,23,42] [15,16]

- now we only have 2 ordered subarrays left and we can merge them

- first we compare the 0 index of each subarray to see if 4 < 15. it is, so it becomes the 0 index of the final array

[4]
[8,23,42] [15,16]

- next we compare the 0 index of each subarray to see if 8 < 15. it is, so it becomes the 1 index of the final array

[4,8]
[23,42] [15,16]

- next we compare the 0 index of each subarray to see if 23 < 15. it is not, so 15 becomes the 2 index of the final array

[4,8,15]
[23,42] [16]

- next we compare the 0 index of each subarray to see if 23 < 16. it is not, so 16 becomes the 3 index of the final array

[4,8,15,16]
[23,42]

- since that subarray is now empty, we add the leftovers to the end of the final array

[4,8,15,16,23,42]

And we have a merge sorted array!!
