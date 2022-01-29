'use strict';
class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
    this.count = 0;
    //this.nodes = [];
  }

  preOrder(node) {
    let nodeArray = [];

    function recursivePart(node){
      //append root node to node_list
      nodeArray.push(node.value);
      //traverse left subtree
      if (node.left){
        recursivePart(node.left);
      }
      //traverse right subtree
      if (node.right){
        recursivePart(node.right);
      }
    }
    recursivePart(node);
    return nodeArray;
  }

  inOrder(node) {
    let nodeArray = [];

    function recursivePart(node){
      //traverse left subtree
      if (node.left){
        recursivePart(node.left);
      }
      //append root node to node_list
      nodeArray.push(node.value);
      //traverse right subtree
      if (node.right){
        recursivePart(node.right);
      }
    }
    recursivePart(node);
    return nodeArray;
  }

  postOrder(node) {
    let nodeArray = [];

    function recursivePart(node){
      //traverse left subtree
      if (node.left){
        recursivePart(node.left);
      }
      //traverse right subtree
      if (node.right){
        recursivePart(node.right);
      }
      //append root node to node_list
      nodeArray.push(node.value);
    }
    recursivePart(node);
    return nodeArray;
  }
}

class BinarySearchTree extends BinaryTree {
  constructor(){
    super();
  }

  add(value) {

    function recursivePart(node) {
      if (node.value === value){
        console.log(node.value, value);
        return 'tree already has this value';
      } else if (node.value > value){
        if (node.left){
          recursivePart(node.left);
        } else {
          node.left = new Node(value);
        }
      } else {
        if (node.right){
          recursivePart(node.right);
        } else {
          node.right = new Node(value);
        }
      }
    }

    if (!this.root) {
      this.root = new Node(value);
    } else {
      return recursivePart(this.root);
    }
  }

  contains(value) {
    let isHere = false;
    function recursivePart(node){
      if (node.value === value) {
        isHere = true;
      } else if (value < node.value) {
        if (node.left){
          recursivePart(node.left);
        } else {
          isHere = false;
        }
      } else {
        if (node.right){
          recursivePart(node.right);
        } else {
          isHere = false;
        }
      }
    }
    recursivePart(this.root);
    return isHere;
  }
}

module.exports = {
  BinaryTree: BinaryTree,
  BinarySearchTree: BinarySearchTree,
  Node: Node,
};


