# Array Binary Search

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process

[binary search whiteboard](https://user-images.githubusercontent.com/75649765/149230794-6ab60847-e83b-400a-86c8-990a5d2039ed.png)

## Approach & Efficiency

used pointers at the beginning and end of array to check the middle, and then if that wasnt the item i was looking for, i could just move one of the pointers to check just half of the array, and keep doing that until the key is found