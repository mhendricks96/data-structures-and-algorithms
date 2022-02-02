'use strict';

// const Queue = require('../../../stacks-and-queues/queue');
const breathFirst = require('../index');
const { BinaryTree } = require('../../../binary-trees');
const { Node } = require('../../../binary-trees');

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('breadth First', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Breadth first traversals', () => {
  it('should return nodes int correct order', () => {
    let my_searchTree = new BinaryTree();
    my_searchTree.root = new Node(100);
    my_searchTree.root.left = new Node(177);
    my_searchTree.root.right = new Node(10);
    my_searchTree.root.left.right = new Node(17);
    expect(breathFirst(my_searchTree)).toEqual([100, 177, 17]);
  });
});
