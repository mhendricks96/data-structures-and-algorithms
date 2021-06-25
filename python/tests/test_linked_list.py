from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_node_instance():
    node = Node('apples',None)
    actual = node.value
    expected = 'apples'
    assert actual == expected

def test_empty_list():
    my_list = LinkedList()
    assert my_list



def test_insert():
    my_list = LinkedList()
    my_list.insert('apples')
    actual = my_list.head.value
    expected = 'apples'
    assert actual == expected

def test_head():
    my_list = LinkedList()
    my_list.insert('banana')
    my_list.insert('tulip')
    actual = my_list.head.value
    expected = 'tulip'
    assert actual == expected


def test_multiple():
    my_list = LinkedList()
    my_list.insert('matthew')
    my_list.insert('mark')
    my_list.insert('luke')
    my_list.insert('john')
    actual = my_list.head.next.value
    expected = 'luke'
    assert actual == expected

def test_includes():
    my_list = LinkedList(Node('michael', Node('david', Node('BJ'))))
    actual = my_list.includes('david')
    expected = True
    assert actual == expected

def test_str():
    my_list = LinkedList(Node('a', Node('b', Node('c'))))
    actual = my_list.__str__()
    expected = "{'a'} -> {'b'} -> {'c'} -> NULL"
    assert actual == expected

def test_append_to_end():
    my_list = LinkedList(Node('a', Node('b', Node('c'))))
    my_list.append_to_end('d')
    actual = my_list.__str__()
    expected = "{'a'} -> {'b'} -> {'c'} -> {'d'} -> NULL"
    assert actual == expected

def test_append_after_value():
    my_list = LinkedList(Node('a', Node('b', Node('c'))))
    my_list.append_after_value('b','d')
    actual = my_list.__str__()
    expected = "{'a'} -> {'b'} -> {'d'} -> {'c'} -> NULL"
    assert actual == expected

def test_append_before_value():
    my_list = LinkedList(Node('a', Node('b', Node('c'))))
    my_list.append_before_value('b','d')
    actual = my_list.__str__()
    expected = "{'a'} -> {'d'} -> {'b'} -> {'c'} -> NULL"
    assert actual == expected

def test_kth_from_end_works():
    my_list = LinkedList(Node('z',(Node('a', Node('b', Node('c'))))))
    actual = my_list.kth_from_end(2)
    expected = 'a'
    assert actual == expected

def test_kth_from_end_k_too_large():
    my_list = LinkedList(Node('z',(Node('a', Node('b', Node('c'))))))
    actual = my_list.kth_from_end(4)
    expected = 'the list is not that long. choose a smaller number'
    assert actual == expected

def test_kth_from_end_k_negative():
    my_list = LinkedList(Node('z',(Node('a', Node('b', Node('c'))))))
    actual = my_list.kth_from_end(-2)
    expected = 'what is this calculus? choose a positive number'
    assert actual == expected

def test_kth_from_end_list_only_1():
    my_list = LinkedList()
    my_list.insert('matthew')
    actual = my_list.kth_from_end(2)
    expected = 'omg this is embarassing but the list only has 1 item....awkward'
    assert actual == expected

def test_find_middle_node_even():
    my_list = LinkedList(Node('z',(Node('a', Node('b', Node('c'))))))
    actual = my_list.find_middle_node()
    expected = 'a'
    assert actual == expected

def test_find_middle_node_odd():
    my_list = LinkedList(Node('a', Node('b', Node('c'))))
    actual = my_list.find_middle_node()
    expected = 'b'
    assert actual == expected