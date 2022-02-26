# Code Challenge 33:  Hashmap Left Join

Write a function that LEFT JOINs two hashmaps into a single data structure

## Challenge

- Write a function called `left_join`

  - Arguments: Two hashmaps
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values
  - Return: The returned data structure that holds the results is up to you. It doesn't need to exactly match the output below, so long as it achieves the LEFT JOIN logic.

## Approach & Efficiency

- Combine the key and corresponding values (if they exist) into a new data structure according to the LEFT JOIN logic

- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the "right" hashmap, they are appended to the result row.

- If no values exist in the right hashmap, then some flavor of `NULL` should be appended to the result row

I chose to use an object as the underlying data structur, which made it a bit more sticky, but was fun. Now the list it returns is full of objects. that have the original key word as the key. within that key's value is another object so that i can show what is the synonym and what is the antonym