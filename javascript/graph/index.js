'use strict';



class Graph {
  constructor(){
    this.adjacencyList = new Map();
  }

  addNode(value) {
    this.adjacencyList.set(value, []);
    return this.adjacencyList.get(value);
  }


  addEdge(startNode, endNode, weight=0) {
    if (!this.adjacencyList.get(startNode) || !this.adjacencyList.get(endNode)){
      return 'couldnt find one of your nodes';
    }

    let startEdges = this.adjacencyList.get(startNode);
    let endEdges = this.adjacencyList.get(endNode);

    this.adjacencyList.set(startEdges.push([endNode, weight]));
    this.adjacencyList.set(endEdges.push([startNode, weight]));

  }

  getNeighbors(node) {
    if (!this.adjacencyList.get(node)) return 'NOT IN GRAPH';
    return this.adjacencyList.get(node);
  }

  getNodes() {
    return Array.from(this.adjacencyList.keys());
  }

  size() {
    return this.adjacencyList.size;
  }
}

module.exports = Graph;
