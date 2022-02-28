'use strict';
const Queue = require('../stacks-and-queues/queue');


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

  breathFirst(){

    let nodes = [];
    let visited_nodes = [];
    let queue = new Queue();
    let [firstNode] = this.adjacencyList.keys();

    queue.enqueue(firstNode);
    visited_nodes.push(firstNode);

    while(!queue.is_empty()){
      let current = queue.dequeue();
      let currentNeighbors = Array.from(this.getNeighbors(current));
      nodes.push(current);

      // console.log(currentNeighbors);
      for (let i = 0; i < currentNeighbors.length; i++) {
        let neighbor = currentNeighbors[i];
        if (!visited_nodes.includes(neighbor)){
          visited_nodes.push(neighbor);
          queue.enqueue(neighbor);
        }
      }
    }
    return nodes.slice(0,-1);
  }

}

module.exports = Graph;
