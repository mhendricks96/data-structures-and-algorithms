'use strict';

const Queue = require('../../stacks-and-queues/queue');


class Node {
  constructor(value){
    this.value = value;
    this.children = [];
  }
}

class kArrayTree {
  constructor(){
    this.root = null;
  }
}


const fizzBuzzTree = (tree) => {

  const changeValue = (value) => {
    if (value % 15 === 0) {
      return 'FizzBuzz';
    } else if (value % 5 === 0){
      return 'Buzz';
    } else if (value % 3 === 0){
      return 'Fizz';
    } else {
      return (value.toString());
    }
  };

  let queue = new Queue();
  queue.enqueue(tree.root);

  while (!queue.is_empty()){
    let front = queue.front;
    front.value = changeValue(front.value);
    for(let i = 0; i < front.children.length; i++){
      queue.enqueue(front.children[i]);
    }
    queue.dequeue();
  }
};

module.exports = {
  Node: Node,
  kArrayTree: kArrayTree,
  fizzBuzzTree: fizzBuzzTree,
};


