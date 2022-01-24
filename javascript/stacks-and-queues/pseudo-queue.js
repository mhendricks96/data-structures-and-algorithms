'use strict';

const Stack = require('../stacks-and-queues/stack');

class PsudoQueue {
  constructor(){
    this.inStack = new Stack();
    this.outStack = new Stack();
    this.length = 0;
  }

  enqueue(value) {
    this.inStack.push(value);
    this.length++;
  }

  dequeue() {
    if (this.outStack.is_empty()){
      while (!this.inStack.is_empty()){
        this.outStack.push(this.inStack.pop());
      }
    }
    this.length--;
    let popped = this.outStack.pop();
    return popped;
  }
}

module.exports = PsudoQueue;

