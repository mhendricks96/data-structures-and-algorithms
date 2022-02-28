'use strict';

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const Graph = require('./index');

describe('Graph', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Graph creation', () => {
  it('should instantiate an empty graph', () => {
    let my_graph = new Graph();
    expect(my_graph).toBeTruthy();
  });
});

describe('Testing Graph length 0', () => {
  it('should return 0 for the length of an empty graph', () => {
    let my_graph = new Graph();
    expect(my_graph.size()).toBe(0);
  });
});

describe('Adding a node to a graph', () => {
  it('should return length of 1 after adding a node to graph', () => {
    let my_graph = new Graph();
    my_graph.addNode(8);
    expect(my_graph.size()).toBe(1);
  });
});

describe('Testing get nodes', () => {
  it('should values of all 3 nodes in the graph', () => {
    let my_graph = new Graph();
    my_graph.addNode(8);
    my_graph.addNode(7);
    my_graph.addNode(5);
    expect(my_graph.getNodes()).toEqual([8,7,5]);
  });
});

describe('Testing edge creation not present', () => {
  it('should let user know one of the nodes they asked for is missing', () => {
    let my_graph = new Graph();
    my_graph.addNode(8);
    my_graph.addNode(7);
    my_graph.addNode(5);
    expect(my_graph.addEdge(8,9)).toEqual('couldnt find one of your nodes');
  });
});


describe('Testing breadth first traversal', () => {
  it('should return a list of nodes in breadth first order', () => {
    let my_graph = new Graph();
    my_graph.addNode('hi');
    my_graph.addNode('bye');
    my_graph.addNode('ok');
    my_graph.addEdge('hi', 'bye', 50);
    my_graph.addEdge('hi', 'ok', 25);
    expect(my_graph.breathFirst()).toEqual([]);
  });
});


