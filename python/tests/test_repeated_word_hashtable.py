from hash_table.hash_table import HashTable
from hash_table_dict.hash_table_dict import HashTableDict
from linked_list.linked_list import LinkedList, Node
from code_challenges.repeated_word_hashtable.repeated_word_hashtable import repeated_word, repeated_word_dict_hash

def test_output():
  actual  = repeated_word("some days are just the perfect weather days")
  expected = "days"
  assert actual == expected

def test_output_first_only():
  actual  = repeated_word("some days just have the perfect weather and some days dont")
  expected = "some"
  assert actual == expected

def test_output_long():
  actual = repeated_word("It was a queer, sultry summer the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
  expected = "summer"
  assert actual == expected

def test_output_dict():
  actual  = repeated_word_dict_hash("some days are just the perfect weather days")
  expected = "days"
  assert actual == expected

def test_output_first_only_dict():
  actual  = repeated_word_dict_hash("some days just have the perfect weather and some days dont")
  expected = "some"
  assert actual == expected

def test_output_long_dict():
  actual = repeated_word_dict_hash("It was a queer, sultry summer the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
  expected = "summer"
  assert actual == expected