from ll_queue.ll_queue import LL_Queue

#  instances: graph, vertex, edge
# graph methods: add_node, add_edge, get_nodes, get_neighbors, size

class Vertex:
  '''creates a new vertex(node) object with a value'''
  def __init__(self, value):
    self.value = value

class Edge:
  '''creats a new edge'''
  def __init__(self, vertex, weight=0):
    self.vertex = vertex
    self.weight = weight

class Graph:
  def __init__(self):
    self._adjacency_list = {}

  def add_node(self, value):
    '''creates a node/vertex with a given value'''
    new_vertex = Vertex(value)
    self._adjacency_list[new_vertex] = []
    return new_vertex

  def add_edge(self, start_vertex, end_vertex, weight=0):
    '''creats an edge between two given vertices with optional edge weight'''
    if start_vertex not in self._adjacency_list:
      raise KeyError('start_vertex not in Graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('end_vertex not in Graph')

    new_edge = Edge(end_vertex, weight)
    start_v_adjacencies = self._adjacency_list[start_vertex]
    start_v_adjacencies.append(new_edge)

  def get_nodes(self):
    '''returns a list of all vertices/nodes in Graph'''
    return list(self._adjacency_list.keys())


  def get_neighbors(self, vertex):
    '''returns the edges connected to the given vertex along with their weights'''
    neighbor_dict = {}
    edge_list = self._adjacency_list[vertex]
    for edge in edge_list:
      neighbor_dict[edge.vertex] = edge.weight

    return neighbor_dict

  def size(self):
    '''returns the number of nodes in the graph'''
    return len(self._adjacency_list)

  
  def breadth_first(self, vertex):
    final_node_list = []
    holding_queue = LL_Queue()
    holding_queue.enqueue(vertex)

    visited_nodes = set()
    visited_nodes.add(vertex)

    while not holding_queue.is_empty():
      current = holding_queue.dequeue()
      current_neighbors = self.get_neighbors(current).keys()
      final_node_list.append(current)

      for neighbor in current_neighbors:
        if neighbor not in visited_nodes:
          visited_nodes.add(neighbor)
          holding_queue.enqueue(neighbor)
    
    print(final_node_list)
    return final_node_list
