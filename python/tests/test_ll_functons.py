from ll_functions.ll_functions import zipped_list, PsuedoQueue#, merge_sorted_list
from linked_list.linked_list import LinkedList, Node

def test_zipped_list():
    ll1 = LinkedList(Node('a', Node('b', Node('c'))))
    ll2 = LinkedList(Node('1', Node('2', Node('3'))))
    zipped_list(ll1,ll2)
    actual = ll1.__str__()
    expected = "{'a'} -> {'1'} -> {'b'} -> {'2'} -> {'c'} -> {'3'} -> NULL"
    assert actual == expected


def test_empty_que_from_two_stacks():
    my_pQueue = PsuedoQueue()
    assert len(my_pQueue) == 0

def test_enqueue_psuedo_queue():
    my_pQueue = PsuedoQueue()
    my_pQueue.enqueue(7)
    my_pQueue.enqueue(10)
    actual = len(my_pQueue)
    expected = 2
    assert actual == expected

def test_dequeue_one_from_psuedo_que():
    my_pQueue = PsuedoQueue()
    my_pQueue.enqueue(7)
    my_pQueue.enqueue(10)
    my_pQueue.enqueue("lil jon")
    actual = my_pQueue.dequeue()
    expected = 7
    assert actual == expected

def test_dequeing_after_enquing_twice():
    my_pQueue = PsuedoQueue()
    my_pQueue.enqueue(7)
    my_pQueue.enqueue(10)
    my_pQueue.enqueue("lil jon")
    my_pQueue.dequeue()
    my_pQueue.dequeue()
    my_pQueue.enqueue(7)
    my_pQueue.enqueue(10)
    actual = my_pQueue.dequeue()
    expected = "lil jon"
    assert actual == expected