from bracket_validation.bracket_validation import validate_brackets
from linked_list.linked_list import LinkedList, Node

def test_check_correct_1():
  #string = "{}(){}"
  actual = validate_brackets("{}(){}")
  expected = True
  assert actual == expected

def test_check_correct_2():
  actual = validate_brackets("(){}[[]]")
  expected = True
  assert actual == expected

def test_check_correct_with_words():
  actual = validate_brackets("(hello){}[[how was vacation?]]")
  expected = True
  assert actual == expected

def test_check_wrong_1():
  string = "[({}]"
  actual = validate_brackets(string)
  expected = False
  assert actual == expected

def test_check_wrong_2():
  string = "{(})"
  actual = validate_brackets(string)
  expected = False
  assert actual == expected

def test_check_wrong_with_words():
  string = "{(thank you for grading})"
  actual = validate_brackets(string)
  expected = False
  assert actual == expected
