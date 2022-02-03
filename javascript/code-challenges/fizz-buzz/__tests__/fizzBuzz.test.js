'use strict';

const { fizzBuzzTree, Node, kArrayTree } = require('../index');

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('fizzbuzz', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('testing fizbuzz functions', () => {
  it ('should return the root as the approprate result', () => {
    let myTree = new kArrayTree();
    myTree.root = new Node(15);
    expect(myTree.root).toBeTruthy();
    fizzBuzzTree(myTree);
    expect(myTree.root.value).toEqual('FizzBuzz');
  });
});
