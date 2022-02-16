# Quick Sort

## Description

In a quick sort function, we choose a pivot item and seperate everything according to that. We then run the function recursively on each side of the pivot.

## Quick Sort Pseudocode

define find pivot place function (array, first, last)

    define pivot as first element (could be any, but i'm choosing first)

    define 'left' as item to the right of pivot

    define 'right' as the element passed in as last

    while loop set to true
        
        see if 'left' element is less than 'right' element and pivot element. if so, make the next element 'left'

        see if 'left' element is less than 'right' element and 'right' element is greater than pivot element. if so, make the previous element 'right'

        once 'right' and 'left' meet, break out of while loop

        with each loop switch the left and right elements

    once the while loop is broken out of, switch the 'first' and 'right' elements

    return 'right'

define main function(array, first, last)

    run until first == last which means the array only has one item

        call find pivot place function on array

        recursively run function on left side of array

        recursively run function on right side of array

define quick sort function (array)

    start function off by finding the first and last elements and sending them to the main function

## Quick Sort Example

sample_array = [8,4,23,42,16,15]

- we declare 8 as the pivot

- use first function to find the appropriate index spot for 8

- [4,8,23,42,16,15]

- since there is only 1 item to the left of the pivot, that side is fine.

- we need to recursively run our functionon everything to the right of 8, with 23 as the pivot.

- use first function to find the appropriate index spot for 23

- [4,8,16,15,23,42]

- since there is only 1 item to the right of the pivot, that side is fine.

- the function is run one more time to flip 15 and 16

- [8,4,23,42,16,15]

- done! quick sorted!
