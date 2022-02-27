'use strict';

class Node {
  constructor(value) {
    this.value = value;
  }
}

class Edge {
  constructor(nodeFrom, weight=0) {
    this.nodeFrom = nodeFrom;
    this.weight = weight;
  }
}

class Graph {
  constructor(){
    this._adjacencyList = {};
  }

  addNode(value) {
    let new_node = new Node(value);
    this._adjacencyList[value] = [];
    return new_node;
  }


  addEdge(startNode, endNode, weight=0) {
    if ((startNode in this._adjacencyList) && (endNode in this._adjacencyList)){
      let newEdge = new Edge(startNode, weight);
      let startNodeAdjacency = this._adjacencyList[startNode];
      startNodeAdjacency.push(newEdge);
    }else {
      return 'couldnt find one of your nodes';
    }
  }

  getNeighbors(node) {
    let neighbors = {};
    let edgeList = this._adjacencyList[node];
    console.log(this._adjacencyList);
    console.log(edgeList);

    for (let i = 0; i < edgeList.length; i++){
      let edge = edgeList[i];

      neighbors[edge.nodeFrom] = edge.weight;
    }
    return neighbors;
  }

  getNodes() {
    return Object.keys(this._adjacencyList);
  }

  size() {
    return Object.keys(this._adjacencyList).length;
  }
}

module.exports = {
  Graph: Graph,
  Node: Node,
  Edge: Edge
};
