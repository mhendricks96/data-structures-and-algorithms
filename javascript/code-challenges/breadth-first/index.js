'use strict';

const Queue = require('../../stacks-and-queues/queue');

const breathFirst = (tree) => {
  let values = [];
  let queue = new Queue();

  queue.enqueue(tree.root);
  while (!queue.is_empty()) {
    let front = queue.dequeue();
    values.push(front.value);
    if (front.left){
      queue.enqueue(front.left);
    }
    if (front.right){
      queue.enqueue(front.right);
    }
  }
  return values;
};

module.exports = breathFirst;
