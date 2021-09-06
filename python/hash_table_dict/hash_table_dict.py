from linked_list.linked_list import LinkedList, Node

class HashTableDict:

  def __init__(self, size=1024):
    self.size = size
    self.buckets = [None] * self.size

  def add(self, key, value):
    index = self.hash(key)

    if not self.buckets[index]:
      self.buckets[index] = LinkedList()

    bucket = self.buckets[index]
    
    if self.contains(key):
      current = bucket.head
      while current is not None:
        if key in current.value:
          current.value[key].add(value)
        current = current.next
    else:
      bucket.insert({key: {value}})


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
      if key in current.value:
        return current.value[key]
      current = current.next

  def contains(self, key):
    index = self.hash(key)
    bucket = self.buckets[index]

    if bucket:
      current = bucket.head
      while current is not None:
        if key in current.value:
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
