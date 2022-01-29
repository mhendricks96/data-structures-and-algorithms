'use strict';

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const { Node, BinaryTree, BinarySearchTree } = require('../index');
// const BinaryTree = require('../index.js');
// const BinarySearchTree = require('../index.js');

describe('Binary Tree', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Tree creation', () => {
  it('should instantiate an empty tree', () => {
    let my_tree = new BinaryTree();
    let my_searchTree = new BinarySearchTree();
    expect(my_tree).toBeTruthy();
    expect(my_searchTree).toBeTruthy();
  });
});

describe('Testing preOrder', () => {
  it('should return correct node order', () => {
    let my_tree = new BinaryTree();
    my_tree.root = new Node(15);
    my_tree.root.left = new Node(78);
    my_tree.root.right = new Node(63);
    expect(my_tree.preOrder(my_tree.root)).toEqual([15,78,63]);
  });
});

describe('Testing inOrder', () => {
  it('should return correct node order', () => {
    let my_tree = new BinaryTree();
    my_tree.root = new Node(15);
    my_tree.root.left = new Node(78);
    my_tree.root.right = new Node(63);
    expect(my_tree.inOrder(my_tree.root)).toEqual([78,15,63]);
  });
});

describe('Testing postOrder', () => {
  it('should return correct node order', () => {
    let my_tree = new BinaryTree();
    my_tree.root = new Node(15);
    my_tree.root.left = new Node(78);
    my_tree.root.right = new Node(63);
    expect(my_tree.postOrder(my_tree.root)).toEqual([78,63,15]);
  });
});

describe('Testing adding root node', () =>{
  it('should add a root node to the tree', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.add(12);
    expect(my_searchTree.root.value).toEqual(12);
  });
});

describe('testing duplicate attemt', () =>{
  it('should return a string when trying to add a value that already exists', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    expect(my_searchTree.add(77)).toEqual('tree already has this value');
  });
});

describe('Testing Binary Search Tree Ordering', () =>{
  it('should put a node lower than the root to the left', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    my_searchTree.add(5);
    expect(my_searchTree.inOrder(my_searchTree.root)).toEqual([5,77]);
  });
  it('should put a node greater than the root to the right', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    my_searchTree.add(100);
    expect(my_searchTree.inOrder(my_searchTree.root)).toEqual([77,100]);
  });
  it('should be able to add many nodes in correct order', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    my_searchTree.add(100);
    my_searchTree.add(10);
    my_searchTree.add(17);
    my_searchTree.add(200);
    expect(my_searchTree.inOrder(my_searchTree.root)).toEqual([10,17,77,100,200]);
  });
});

describe('Testing contains method', () => {
  it('should return true when the value is in the tree', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    my_searchTree.add(100);
    my_searchTree.add(10);
    my_searchTree.add(17);
    expect(my_searchTree.contains(17)).toEqual(true);
  });
  it('should return false when the value is in the tree', () => {
    let my_searchTree = new BinarySearchTree();
    my_searchTree.root = new Node(77);
    my_searchTree.add(100);
    my_searchTree.add(10);
    my_searchTree.add(17);
    expect(my_searchTree.contains(1)).toEqual(false);
  });
});
