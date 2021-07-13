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