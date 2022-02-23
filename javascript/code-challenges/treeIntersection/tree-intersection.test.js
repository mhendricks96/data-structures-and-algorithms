const {BinarySearchTree} = require('../../binary-trees');

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

const tree_intersection = require('./tree-intersection');

describe('tree intersection', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('testing tree intersection', () => {
  it('should return an array of the common values', () => {
    let thisTree = new BinarySearchTree();
    let thatTree = new BinarySearchTree();

    let values_list = [17,87,77,16,9,81738];
    for (let i = 0; i < values_list.length; i++){
      thisTree.add(values_list[i]);
    }

    let values_list2 = [17,80,52,16,6,1];
    for (let i = 0; i < values_list2.length; i++){
      thatTree.add(values_list2[i]);
    }
    expect(tree_intersection(thisTree, thatTree)).toEqual([17,16]);
  });
});

