from graphs.graphs import Graph


def business_trip(my_graph, list_of_cities):
  '''function that takes in a list of cities and returns a boolean indicating whether the trip is possible with direct flights'''
  total_price = 0
  happy_path = False
  #city_list = []

  for city in (list_of_cities):
    city_list = my_graph._adjacency_list[city]
  return city_list