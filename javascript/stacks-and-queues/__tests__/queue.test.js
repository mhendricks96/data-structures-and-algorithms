const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const Queue = require('../queue');

describe('Queue', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Queue creation', () => {
  it('should instantiate an empty Queue', () => {
    let myQueue = new Queue();
    expect(myQueue).toBeTruthy;
    expect(myQueue.front).toBe(null);
    expect(myQueue.back).toBe(null);
  });
});

describe('Testing enqueing into Queue', () => {
  it('should add a node to the back of Queue', () => {
    let myQueue = new Queue();
    myQueue.enqueue(15);
    expect(myQueue.front.value).toEqual(15);
    expect(myQueue.back.value).toEqual(15);
  });

  it('should enqueue 3 nodes onto a Queue', () => {
    let myQueue = new Queue();
    myQueue.enqueue(15);
    myQueue.enqueue(35);
    myQueue.enqueue(84);
    expect(myQueue.length).toEqual(3);
  });
});

describe('Testing dequeueing off of Queue', () => {
  it('Should remove a node from the front the Queue', () => {
    let myQueue = new Queue();
    myQueue.enqueue(15);
    myQueue.enqueue(35);
    expect(myQueue.dequeue()).toEqual(15);
  });
  it('Should empty the Queue after multiple dequeues', () => {
    let myQueue = new Queue();
    myQueue.enqueue(15);
    myQueue.enqueue(35);
    myQueue.dequeue();
    myQueue.dequeue();
    expect(myQueue.length).toEqual(0);
  });
  it('Should raise an exception if the Queue is empty',() => {
    let myQueue = new Queue();
    expect(myQueue.dequeue()).toEqual('This Queue is already empty');
  });
});

describe('Testing Peek method', () => {
  it('should return the value of the top node of the Queue', () => {
    let myQueue = new Queue();
    myQueue.enqueue(15);
    myQueue.enqueue(35);
    expect(myQueue.peek()).toEqual(15);
  });
  it('Should raise an exception if the Queue is empty',() => {
    let myQueue = new Queue();
    expect(myQueue.peek()).toEqual('Sorry, this Queue is empty');
  });
});
