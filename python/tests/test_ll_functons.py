from ll_functions.ll_functions import zipped_list#, merge_sorted_list
from linked_list.linked_list import LinkedList, Node

def test_zipped_list():
    ll1 = LinkedList(Node('a', Node('b', Node('c'))))
    ll2 = LinkedList(Node('1', Node('2', Node('3'))))
    zipped_list(ll1,ll2)
    actual = ll1.__str__()
    expected = "{'a'} -> {'1'} -> {'b'} -> {'2'} -> {'c'} -> {'3'} -> NULL"
    assert actual == expected

# def test_merge_sorted_list():
#     ll1 = LinkedList()
#     ll1.insert(1)
#     ll1.insert(2)
#     ll1.insert(3)
#     ll2 = LinkedList(Node(2, Node(4, Node(6))))
#     actual = merge_sorted_list(ll1,ll2)
#     expected = "{1} -> {2} -> {3} -> {4} -> {5} -> {6} -> NULL"
#     assert actual == expected
