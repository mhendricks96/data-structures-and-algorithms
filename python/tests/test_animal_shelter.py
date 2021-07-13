from animal_shelter.animal_shelter import AnimalShelter
from linked_list.linked_list import LinkedList, Node

def test_adding_and_removing_one_dog():
  my_shelter = AnimalShelter()
  my_shelter.enqueue("dog")
  actual = my_shelter.dequeue("dog")
  expected = "dog"
  assert actual == expected

def test_adding_and_removing_one_cat():
  my_shelter = AnimalShelter()
  my_shelter.enqueue("cat")
  actual = my_shelter.dequeue("cat")
  expected = "cat"
  assert actual == expected

def test_trying_to_dequeue_nonexistent():
  my_shelter = AnimalShelter()
  my_shelter.enqueue("cat")
  actual = my_shelter.dequeue("dog")
  expected = "Null"
  ectual2 = my_shelter.dequeue("cat")
  expected2 = "cat"
  assert actual == expected
  assert actual == expected

def test_find_a_cat():
  my_shelter = AnimalShelter()
  my_shelter.enqueue("dog")
  my_shelter.enqueue("dog")
  my_shelter.enqueue("dog")
  my_shelter.enqueue("cat")
  actual1 = my_shelter.rear.value
  expected1 = "cat"
  actual = my_shelter.dequeue("cat")
  expected = "cat"
  assert actual1 == expected1
  assert actual == expected

def check_order():
  my_shelter = AnimalShelter()
  my_shelter.enqueue("dog1")
  my_shelter.enqueue("dog2")
  my_shelter.enqueue("dog3")
  my_shelter.enqueue("cat")
  my_shelter.dequeue("cat")
  actual = my_shelter.front.value
  expected = "dog1"
  assert actual == expected
  