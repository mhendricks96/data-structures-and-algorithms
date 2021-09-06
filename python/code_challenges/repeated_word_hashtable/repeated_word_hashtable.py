from hash_table.hash_table import HashTable
from hash_table_dict.hash_table_dict import HashTableDict
from linked_list.linked_list import LinkedList, Node

def repeated_word(string):
  """Function that takes in a string and returns the first word to occur mor than once in the string."""
  my_hash = HashTable()
  for word in string.split(' '):
    count = 1
    
    if my_hash.contains(word):
      index = my_hash.hash(word)
      bucket = my_hash.buckets[index]
      current = bucket.head
      while current is not None:
        if current.value[0] == word:
          current.value[1] += 1
        current = current.next
      return word
    
    else:
      my_hash.add(word, count)


def repeated_word_dict_hash(string):
  """Function that takes in a string and returns the first word to occur mor than once in the string. This hashtable uses a dictianary within it"""
  my_hash = HashTableDict()
  for word in string.split(' '):

    if my_hash.contains(word):
      index = my_hash.hash(word)
      bucket = my_hash.buckets[index]
      current = bucket.head
      while current is not None:
        if word in current.value:
          current.value[word][0] += 1
          return word
        current = current.next
    
    else:
      my_hash.add(word, 1)