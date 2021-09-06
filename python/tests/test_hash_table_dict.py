from linked_list.linked_list import LinkedList, Node
from hash_table_dict.hash_table_dict import HashTableDict

def test_create_empty_hash_table():
  my_hashtable = HashTableDict()
  assert my_hashtable

def test_hash():
  my_hashtable = HashTableDict()
  key = "popcorn"
  index = my_hashtable.hash(key)
  actual = my_hashtable.hash(key)
  expected = 855
  assert index == expected
  assert actual == expected
  assert index == actual

def test_hash_wrong():
  my_hashtable = HashTableDict()
  key = "popcorn"
  actual = my_hashtable.hash(key)
  expected = 1738
  assert actual != expected

def test_same_index():
  my_hashtable = HashTableDict()
  key_a = "biblioteca"
  key_b = "tecaiobibl"
  assert my_hashtable.hash(key_a) == my_hashtable.hash(key_b)

def test_different_index():
  my_hashtable = HashTableDict()
  key_a = "biblioteca"
  key_b = "biblioteco"
  assert my_hashtable.hash(key_a) != my_hashtable.hash(key_b)

def test_always_within_range():
  my_hashtable = HashTableDict()
  key_a = "biblioteca"
  key_b = "gtowepjafp"
  key_c = "aioersjarf"
  key_d = "gggggggggg"
  key_e = "zxzxzxzxzx"
  key_f = "sxdkljafsi"
  key_g = "qwertyuiop"
  key_h = "jgjgjgjgjg"
  assert my_hashtable.hash(key_a) < 1024
  assert my_hashtable.hash(key_b) < 1024
  assert my_hashtable.hash(key_c) < 1024
  assert my_hashtable.hash(key_d) < 1024
  assert my_hashtable.hash(key_e) < 1024
  assert my_hashtable.hash(key_f) < 1024
  assert my_hashtable.hash(key_g) < 1024
  assert my_hashtable.hash(key_h) < 1024

def test_add_1():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "blue")
  index = my_hashtable.hash("color")
  bucket = my_hashtable.buckets[index]
  assert len(bucket) == 1

def test_add_2_same_bucket():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "blue")
  my_hashtable.add("oolcr", "red")
  index = my_hashtable.hash("color")
  bucket = my_hashtable.buckets[index]
  assert len(bucket) == 2

# def test_add_key_exists_already():
#   my_hashtable = HashTableDict()
#   my_hashtable.add("color", "black")
#   actual = my_hashtable.add("color", "black")
#   expected = "sorry, can only accept 1 value per key"
#   assert actual == expected

def test_contains():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "black")
  my_hashtable.add("size", "large")
  my_hashtable.add("age", "old")
  assert my_hashtable.contains("color")
  assert my_hashtable.contains("size")
  assert my_hashtable.contains("age")

def test_doesnt_contains():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "black")
  my_hashtable.add("size", "large")
  my_hashtable.add("age", "old")
  assert my_hashtable.contains("height") == False

def test_get_nonexistent():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "black")
  my_hashtable.add("size", "large")
  actual = my_hashtable.get("age")
  expected = "sorry, key not found"
  assert actual == expected

def test_get_working():
  my_hashtable = HashTableDict()
  my_hashtable.add("color", "black")
  my_hashtable.add("size", "large")
  actual = my_hashtable.get("color")
  expected = ["black"]
  actual2 = my_hashtable.get("size")
  expected2 = ["large"]
  assert actual == expected
  assert actual2 == expected2

# Stretch Goal

def test_add_same_keys():
    hashtable = HashTableDict()
    hashtable.add("a", "apple")
    hashtable.add("a", "alfalfa")
    actual = hashtable.get("a")
    expected = ["apple","alfalfa"]
    assert actual == expected

