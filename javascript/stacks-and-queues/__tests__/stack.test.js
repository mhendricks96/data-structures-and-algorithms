const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

const Stack = require('../stack');

describe('Stacks', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Stack creation', () => {
  it('should instantiate an empty stack', () => {
    let myStack = new Stack();
    expect(myStack).toBeTruthy;
    expect(myStack.top).toBe(null);
  });
});

describe('Testing pushing onto Stack', () => {
  it('should push a node onto a stack', () => {
    let myStack = new Stack();
    myStack.push(15);
    expect(myStack.top.value).toEqual(15);
  });

  it('should push 3 nodes onto a stack', () => {
    let myStack = new Stack();
    myStack.push(15);
    myStack.push(35);
    myStack.push(84);
    expect(myStack.length).toEqual(3);
  });
});

describe('Testing popping off of Stack', () => {
  it('Should pop a node off the stack', () => {
    let myStack = new Stack();
    myStack.push(15);
    myStack.push(35);
    expect(myStack.pop()).toEqual(35);
  });
  it('Should empty the stack after multiple pops', () => {
    let myStack = new Stack();
    myStack.push(15);
    myStack.push(35);
    myStack.pop();
    myStack.pop();
    expect(myStack.length).toEqual(0);
  });
  it('Should raise an exception if the stack is empty',() => {
    let myStack = new Stack();
    expect(myStack.pop()).toEqual('This stack is already empty');
  });
});

describe('Testing Peek method', () => {
  it('should return the value of the top node of the stack', () => {
    let myStack = new Stack();
    myStack.push(15);
    myStack.push(35);
    expect(myStack.peek()).toEqual(35);
  });
  it('Should raise an exception if the stack is empty',() => {
    let myStack = new Stack();
    expect(myStack.peek()).toEqual('Sorry, this stack is empty');
  });
});
