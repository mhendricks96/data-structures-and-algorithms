from linked_list.linked_list import LinkedList, Node

class HashTable:

  def __init__(self, size=1024):
    self.size = size
    self.buckets = [None] * self.size

  def add(self, key, value):
    """
    addsnew key-value pair to hash table. can only input 1 value per key
    """
    index = self.hash(key)

    if self.contains(key):
      return "sorry, can only accept 1 value per key"

    if not self.buckets[index]:
      self.buckets[index] = LinkedList()

    bucket = self.buckets[index]
    bucket.insert([key, value])

  def get(self, key):
    """
    returns the value of a given key
    """
    if self.contains(key) == False:
      return "sorry, key not found"
    index = self.hash(key)
    bucket = self.buckets[index]
    
    current = bucket.head
    while current is not None:
      if current.value[0] == key:
        return current.value[1]
      current = current.next

  def contains(self, key):
    """
    returns a boolean depending on wheter or not the given key is present in the hash table
    """
    index = self.hash(key)
    bucket = self.buckets[index]

    if bucket:
      current = bucket.head
      while current is not None:
        if current.value[0] == key:
          return True
        current = current.next
    
    return False

  def hash(self, key):
    """
    finds the index position of a given key
    """
    char_val_total = 0
    for char in key:
      char_val = ord(char)
      char_val_total += char_val

    product = char_val_total * 599
    index = product % self.size
    
    return index





#These are all for using a dictionary as the underlying data structure in  the linked lists

  
  # def add(self, key, value):
  #   index = self.hash(key)

  #   if not self.buckets[index]:
  #     self.buckets[index] = LinkedList()

  #   bucket = self.buckets[index]
  #   #bucket.insert([key, value])
  #   bucket.insert({key: value})
  
  
  # def contains(self, key):
  #   index = self.hash(key)
  #   bucket = self.buckets[index]

  #   if bucket:
  #     current = bucket.head
  #     while current is not None:
  #       if key in current.value:
  #         return True
  #       current = current.next
    
  #   return False