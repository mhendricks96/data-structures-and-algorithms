from ll_queue.ll_queue import LL_Queue
from linked_list.linked_list import LinkedList, Node
# Linked List Queue Tests

def test_create_empty_queue():
    my_queue = LL_Queue()
    actual = len(my_queue)
    expected = 0
    assert actual == expected

def test_enqueue_one():
    my_queue = LL_Queue()
    my_queue.enqueue("yea, mike")
    actual = len(my_queue)
    expected = 1
    assert actual == expected

def test_enqueue_three():
    my_queue = LL_Queue()
    my_queue.enqueue("yea, mike")
    my_queue.enqueue("hola, miguel")
    my_queue.enqueue("bonjuer, mike")
    actual = len(my_queue)
    expected = 3
    assert actual == expected

def test_dequeue_one():
    my_queue = LL_Queue()
    my_queue.enqueue(22)
    my_queue.enqueue(77)
    my_queue.dequeue()
    actual = len(my_queue)
    expected = 1
    assert actual == expected

def test_dequeue_all():
    my_queue = LL_Queue()
    my_queue.enqueue(22)
    my_queue.enqueue(77)
    my_queue.enqueue("codefellows")
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    actual = len(my_queue)
    expected = 0
    assert actual == expected

def test_peek_into_queue():
    my_queue = LL_Queue()
    my_queue.enqueue(22)
    my_queue.enqueue(77)
    my_queue.enqueue("codefellows")
    actual = my_queue.peek()
    expected = 22
    assert actual == expected

def test_empty_exception_in_queue():
    my_queue = LL_Queue()
    actual = my_queue.dequeue()
    expected = "Sorry, the queue is empty"
    assert actual == expected