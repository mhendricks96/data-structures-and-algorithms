from ll_stack.ll_stack import LL_Stack
from linked_list.linked_list import LinkedList, Node
# Linked List Stack Tests

def test_create_empty_stack():
    my_stack = LL_Stack()
    actual = len(my_stack)
    expected = 0
    assert actual == expected

def test_push_one_into_stack():
    my_stack = LL_Stack()
    my_stack.push("yea, mike")
    actual = len(my_stack)
    expected = 1
    assert actual == expected

def test_push_three_into_stack():
    my_stack = LL_Stack()
    my_stack.push("yea, mike")
    my_stack.push("happy 4th!")
    my_stack.push(15)
    actual = len(my_stack)
    expected = 3
    assert actual == expected

def test_pop_1_from_stack():
    my_stack = LL_Stack()
    my_stack.push("yea, mike")
    my_stack.push("happy 4th!")
    my_stack.push(15)
    my_stack.pop()
    actual = len(my_stack)
    expected = 2
    assert actual == expected

def test_pop_all_from_stack():
    my_stack = LL_Stack()
    my_stack.push("yea, mike")
    my_stack.push("happy 4th!")
    my_stack.push(15)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    actual = len(my_stack)
    expected = 0
    assert actual == expected

def test_peek_into_stack():
    my_stack = LL_Stack()
    my_stack.push("yea, mike")
    my_stack.push("happy 4th!")
    my_stack.push(15)
    actual = my_stack.peek()
    expected = 15
    assert actual == expected

def test_empty_exception_in_stack():
    my_stack = LL_Stack()
    actual = my_stack.peek()
    expected = "Sorry, the stack is empty"
    assert actual == expected