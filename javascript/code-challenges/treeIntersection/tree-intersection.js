'use strict';
const HashTable = require('../../hashTable');
const breathFirst = require('../breadth-first');

const tree_intersection = (tree1, tree2) => {
  // eslint-disable-next-line no-unused-vars
  let my_hashTable = new HashTable();

  let tree1_array = breathFirst(tree1);
  let tree2_array = breathFirst(tree2);

  const commonValues = tree1_array.filter(value => tree2_array.indexOf(value) !== -1);

  return commonValues;
};

module.exports = tree_intersection;
