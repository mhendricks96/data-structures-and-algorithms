# Insert and shift array at middle index

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

[code challenge 2 screenshot](https://user-images.githubusercontent.com/75649765/149020081-4f1ed80f-d22b-4380-b2a2-c3a27d7ac769.png)

## Approach & Efficiency

I found the middle index by dividing the array length by 2. I used math.ciel to make sure it would land on the left side if ther were an uneven number of items in the array. Once i found the middle index, i used slice to add the new value at that index.
