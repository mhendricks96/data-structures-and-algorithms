from graphs.graphs import Graph


def business_trip(my_graph, list_of_cities):
  '''function that takes in a list of cities and returns a boolean indicating whether the trip is possible with direct flights'''
  
  if my_graph.get_nodes() == None or list_of_cities == None:
    return False, 0
  
  total_price = 0
  
  for idx, city in enumerate(list_of_cities):
    possible_flights = my_graph.get_neighbors(city)

    if idx + 1 < len(list_of_cities):
      next_city = list_of_cities[idx + 1]
    else:
      next_city = None

    if next_city == None:
      break
    elif next_city not in possible_flights:
      return False, 0

    ticket_price = possible_flights[next_city]

    total_price = total_price + ticket_price
  
  return True, total_price
