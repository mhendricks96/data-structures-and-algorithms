// const Graph = require('../../graph');

const graphTrip = (graph, cities) => {
  let available = false;
  let cost = 0;
  let answer = [available, cost];
  if (graph.size() === 0 || cities.length === 0){

    return answer;
  }
  let totalPrice = 0;

  for (let i = 0; i < cities.length; i++){
    let city = cities[i];
    let possible_flights = graph.getNeighbors(city);

    let next_city;

    if (i + 1 < cities.length){
      next_city = cities[i + 1];
    } else {
      next_city = null;
    }

    if (next_city === null){
      break;
    } else if (!(possible_flights.includes(next_city))){
      return answer;
    }

    let ticket_price = possible_flights[next_city];
    totalPrice = totalPrice + ticket_price;
  }

  available = true;
  cost = totalPrice;
  return answer;
};

module.exports = graphTrip;

