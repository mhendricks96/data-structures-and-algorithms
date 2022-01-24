const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const PsudoQueue = require('../pseudo-queue');

describe('PsudoQueue', () => {
  it ('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testint psudoque creation', () => {
  it('should instantiate an empty PsudoQueue', () => {
    let myPsudoQueue = new PsudoQueue();
    expect(myPsudoQueue).toBeTruthy;
  });
});

describe('Testing enqueing into psudoQueue', () => {
  it('should add a node to the back of Queue', () => {
    let myPsudoQueue = new PsudoQueue();
    myPsudoQueue.enqueue(15);
    expect(myPsudoQueue.length).toEqual(1);
  });

  it('should enqueue 3 nodes onto a Queue', () => {
    let myPsudoQueue = new PsudoQueue();
    myPsudoQueue.enqueue(15);
    myPsudoQueue.enqueue(35);
    myPsudoQueue.enqueue(84);
    expect(myPsudoQueue.length).toEqual(3);
  });
});

describe('Testing dequeueing off of PsudoQueue', () => {
  it('Should remove a node from the front the Queue', () => {
    let myPsudoQueue = new PsudoQueue();
    myPsudoQueue.enqueue(15);
    myPsudoQueue.enqueue(35);
    expect(myPsudoQueue.dequeue()).toEqual(15);
  });
  it('Should empty the Queue after multiple dequeues', () => {
    let myPsudoQueue = new PsudoQueue();
    myPsudoQueue.enqueue(15);
    myPsudoQueue.enqueue(35);
    myPsudoQueue.dequeue();
    myPsudoQueue.dequeue();
    expect(myPsudoQueue.length).toEqual(0);
  });
});
