import pytest
from code_challenges.sorting_algorithms.insertion_sort import insertion_sort
from code_challenges.sorting_algorithms.merge_sort import merge_sort
from code_challenges.sorting_algorithms.quick_sort import quick_sort



def test_insertion_sort():
  my_list = [4,7,3,8,1,17,11,5]
  insertion_sort(my_list)
  assert my_list == [1,3,4,5,7,8,11,17]

def test_insertion_sort_2():
  my_list = [400,79,39,28,19,17,11,5]
  insertion_sort(my_list)
  assert my_list == [5,11,17,19,28,39,79,400]

def test_merge_sort():
  my_list = [4,7,3,8,1,17,11,5]
  merge_sort(my_list)
  assert my_list == [1,3,4,5,7,8,11,17]

def test_merge_sort_2():
  my_list = [400,79,39,28,19,17,11,5]
  merge_sort(my_list)
  assert my_list == [5,11,17,19,28,39,79,400]

def test_quick_sort():
  my_list = [4,7,3,8,1,17,11,5]
  quick_sort(my_list)
  assert my_list == [1,3,4,5,7,8,11,17]

def test_quick_sort_2():
  my_list = [400,79,39,28,19,17,11,5]
  quick_sort(my_list)
  assert my_list == [5,11,17,19,28,39,79,400]

