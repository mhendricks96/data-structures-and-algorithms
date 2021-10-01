from graphs.graphs import Graph, Edge, Vertex
from code_challenges.graph_functions.graph_functions import business_trip
import pytest


def test_business_trip():
  
  my_graph = Graph()
  pandora = my_graph.add_node('Pandora')
  metroville = my_graph.add_node('Metroville')
  narnia = my_graph.add_node('Narnia')
  naboo = my_graph.add_node('Naboo')
  arendelle = my_graph.add_node('Arendelle')
  monstropolis = my_graph.add_node('Monstropolis')
  my_graph.add_edge(pandora, arendelle, 150)
  my_graph.add_edge(arendelle, pandora, 150)
  my_graph.add_edge(pandora, metroville, 82)
  my_graph.add_edge(metroville, pandora, 82)
  my_graph.add_edge(metroville, arendelle, 99)
  my_graph.add_edge(arendelle, metroville, 99)
  my_graph.add_edge(metroville, narnia, 37)
  my_graph.add_edge(narnia, metroville, 37)
  my_graph.add_edge(metroville, monstropolis, 105)
  my_graph.add_edge(monstropolis, metroville,105)
  my_graph.add_edge(metroville, naboo, 26)
  my_graph.add_edge(naboo, metroville, 26)
  my_graph.add_edge(monstropolis, naboo, 73)
  my_graph.add_edge(naboo, monstropolis, 73)
  my_graph.add_edge(narnia, naboo, 250)
  my_graph.add_edge(naboo, narnia, 250)
  my_graph.add_edge(arendelle, monstropolis, 42)
  my_graph.add_edge(monstropolis,arendelle, 42)


  actual = business_trip(my_graph, [pandora, arendelle])
  expected = True, 150
  assert actual == expected


def test_business_trip_2():
  
  my_graph = Graph()
  pandora = my_graph.add_node('Pandora')
  metroville = my_graph.add_node('Metroville')
  narnia = my_graph.add_node('Narnia')
  naboo = my_graph.add_node('Naboo')
  arendelle = my_graph.add_node('Arendelle')
  monstropolis = my_graph.add_node('Monstropolis')
  my_graph.add_edge(pandora, arendelle, 150)
  my_graph.add_edge(arendelle, pandora, 150)
  my_graph.add_edge(pandora, metroville, 82)
  my_graph.add_edge(metroville, pandora, 82)
  my_graph.add_edge(metroville, arendelle, 99)
  my_graph.add_edge(arendelle, metroville, 99)
  my_graph.add_edge(metroville, narnia, 37)
  my_graph.add_edge(narnia, metroville, 37)
  my_graph.add_edge(metroville, monstropolis, 105)
  my_graph.add_edge(monstropolis, metroville,105)
  my_graph.add_edge(metroville, naboo, 26)
  my_graph.add_edge(naboo, metroville, 26)
  my_graph.add_edge(monstropolis, naboo, 73)
  my_graph.add_edge(naboo, monstropolis, 73)
  my_graph.add_edge(narnia, naboo, 250)
  my_graph.add_edge(naboo, narnia, 250)
  my_graph.add_edge(arendelle, monstropolis, 42)
  my_graph.add_edge(monstropolis,arendelle, 42)


  actual = business_trip(my_graph, [pandora, arendelle, metroville])
  expected = True, 249
  assert actual == expected


def test_business_trip_sad():
  
  my_graph = Graph()
  pandora = my_graph.add_node('Pandora')
  metroville = my_graph.add_node('Metroville')
  narnia = my_graph.add_node('Narnia')
  naboo = my_graph.add_node('Naboo')
  arendelle = my_graph.add_node('Arendelle')
  monstropolis = my_graph.add_node('Monstropolis')
  my_graph.add_edge(pandora, arendelle, 150)
  my_graph.add_edge(arendelle, pandora, 150)
  my_graph.add_edge(pandora, metroville, 82)
  my_graph.add_edge(metroville, pandora, 82)
  my_graph.add_edge(metroville, arendelle, 99)
  my_graph.add_edge(arendelle, metroville, 99)
  my_graph.add_edge(metroville, narnia, 37)
  my_graph.add_edge(narnia, metroville, 37)
  my_graph.add_edge(metroville, monstropolis, 105)
  my_graph.add_edge(monstropolis, metroville,105)
  my_graph.add_edge(metroville, naboo, 26)
  my_graph.add_edge(naboo, metroville, 26)
  my_graph.add_edge(monstropolis, naboo, 73)
  my_graph.add_edge(naboo, monstropolis, 73)
  my_graph.add_edge(narnia, naboo, 250)
  my_graph.add_edge(naboo, narnia, 250)
  my_graph.add_edge(arendelle, monstropolis, 42)
  my_graph.add_edge(monstropolis,arendelle, 42)


  actual = business_trip(my_graph, [pandora, naboo])
  expected = False, 0
  assert actual == expected
