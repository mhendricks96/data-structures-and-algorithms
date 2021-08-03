# Challenge Summary

- Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![code challenge 18 whiteboard](https://user-images.githubusercontent.com/75649765/128054224-571cdda5-3961-4288-8e55-f805415e02a3.png)

## Approach & Efficiency

pushed values into queue and dequeued in oder while changing values with a helper function

## Solution

![Link to code](python/k_ary_tree/k_ary_tree.py)
