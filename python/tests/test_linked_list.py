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