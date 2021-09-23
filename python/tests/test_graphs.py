from graphs.graphs import Graph, Edge, Vertex
from ll_queue.ll_queue import LL_Queue

def test_empty_graph():
  my_graph = Graph()
  assert my_graph

def test_singe_vertex():
  my_vertex = Vertex("michael")
  assert my_vertex.value == "michael"

def test_singe_edge():
  my_vertex = Vertex("michael")
  my_edge = Edge(my_vertex)
  assert Edge

def test_add_node():
  my_graph = Graph()
  new = my_graph.add_node("lexi")
  assert new.value == "lexi"

def test_get_nodes():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(2)
  actual = my_graph.get_nodes()
  expected = [node1, node2, node3, node4]
  assert actual == expected

def test_get_size():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(2)
  actual = my_graph.size()
  expected = 4
  assert actual == expected

def test_get_neighbors():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(2)
  my_graph.add_edge(node1, node2)
  my_graph.add_edge(node1, node3)
  my_graph.add_edge(node1, node4, 257)
  actual = my_graph.get_neighbors(node1)
  expected = {node2: 0, node3: 0, node4: 257}
  assert actual == expected

def test_breadth_first_traversal():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(8)
  node5 = my_graph.add_node(6)
  node6 = my_graph.add_node(4)
  node7 = my_graph.add_node(2)
  my_graph.add_edge(node1, node2)
  my_graph.add_edge(node2, node3)
  my_graph.add_edge(node3, node4, 257)
  my_graph.add_edge(node3, node5, 257)
  my_graph.add_edge(node4, node6)
  my_graph.add_edge(node5, node7)

  actual = my_graph.breadth_first(node1)
  expected = [node1, node2, node3, node4, node5, node6, node7]
  assert actual == expected

def test_breadth_first_2():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(8)
  node5 = my_graph.add_node(8)
  my_graph.add_edge(node1, node2)
  my_graph.add_edge(node1, node3)
  my_graph.add_edge(node1, node4)
  my_graph.add_edge(node1, node5)

  actual = my_graph.breadth_first(node1)
  expected = [node1, node2, node3, node4, node5]
  assert actual == expected

def test_breadth_first_from_middle():
  my_graph = Graph()
  node1 = my_graph.add_node(8)
  node2 = my_graph.add_node(6)
  node3 = my_graph.add_node(4)
  node4 = my_graph.add_node(8)
  node5 = my_graph.add_node(6)
  node6 = my_graph.add_node(4)
  node7 = my_graph.add_node(2)
  my_graph.add_edge(node1, node2)
  my_graph.add_edge(node2, node1)
  my_graph.add_edge(node2, node3)
  my_graph.add_edge(node3, node2)
  my_graph.add_edge(node3, node4)
  my_graph.add_edge(node3, node5)
  my_graph.add_edge(node4, node6)
  my_graph.add_edge(node5, node7)

  actual = my_graph.breadth_first(node3)
  expected = [node3, node2, node4, node5, node1, node6, node7]
  assert actual == expected

  