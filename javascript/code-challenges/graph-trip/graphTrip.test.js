'use strict';
const Graph = require('../../graph');
const graphTrip = require('./graphTrip');
const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('breadth First', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});


describe('Testing business trip itinerary', () => {

  it('Should return False and the cost if a direct flight between two cities exists', () => {

    let my_graph = new Graph();
    let pandora = my_graph.addNode('Pandora');
    let metroville = my_graph.addNode('Metroville');
    let narnia = my_graph.addNode('Narnia');
    let naboo = my_graph.addNode('Naboo');
    let arendelle = my_graph.addNode('Arendelle');
    let monstropolis = my_graph.addNode('Monstropolis');
    my_graph.addEdge(pandora, arendelle, 150);
    my_graph.addEdge(arendelle, pandora, 150);
    my_graph.addEdge(pandora, metroville, 82);
    my_graph.addEdge(metroville, pandora, 82);
    my_graph.addEdge(metroville, arendelle, 99);
    my_graph.addEdge(arendelle, metroville, 99);
    my_graph.addEdge(metroville, narnia, 37);
    my_graph.addEdge(narnia, metroville, 37);
    my_graph.addEdge(metroville, monstropolis, 105);
    my_graph.addEdge(monstropolis, metroville,105);
    my_graph.addEdge(metroville, naboo, 26);
    my_graph.addEdge(naboo, metroville, 26);
    my_graph.addEdge(monstropolis, naboo, 73);
    my_graph.addEdge(naboo, monstropolis, 73);
    my_graph.addEdge(narnia, naboo, 250);
    my_graph.addEdge(naboo, narnia, 250);
    my_graph.addEdge(arendelle, monstropolis, 42);
    my_graph.addEdge(monstropolis,arendelle, 42);




    let [isDirect,] = graphTrip(my_graph, [pandora, arendelle]);
    expect(isDirect).toEqual(false);
  });

  // it('Should return FALSE and NULL cost if a direct flight between two cities doesn\'t exist', () => {
  //   let [isDirect, cost] = graphTrip(graph, ['Naboo', 'Pandora']);
  //   expect(isDirect).toBeFalsy();
  //   expect(cost).toEqual(null);
  // });

  // it('Should return TRUE and the total cost if a flight plan between three cities exist', () => {
  //   let [isDirect, cost] = graphTrip(graph, ['Arendelle', 'New Monstropolis', 'Naboo']);
  //   expect(isDirect).toBeTruthy();
  //   expect(cost).toEqual(115);
  // });

  // it('Should return TRUE and the total cost if a flight plan between three cities exist', () => {
  //   let [isDirect, cost] = graphTrip(graph, ['Narnia', 'Arendelle', 'Naboo']);
  //   expect(isDirect).toBeFalsy();
  //   expect(cost).toEqual(null);
  // });
});
