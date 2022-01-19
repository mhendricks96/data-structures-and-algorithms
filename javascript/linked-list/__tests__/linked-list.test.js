'use strict';

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
// Require our linked list implementation
const LinkedList = require('../index');

describe('Linked List', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Linked List creation', () => {
  it('should instantiate an empty linked list', () => {
    let my_list = new LinkedList();
    expect(my_list.length).toEqual(0);
  });
});

describe('Testing the Head Node', () => {
  it('should point to the first node in the linked list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    expect(my_list.head.value).toEqual(5);
  });
});

describe('Testing Insert function', () => {
  it('should insert multiple nodes', () => {
    let my_list = new LinkedList();
    my_list.insert(15);
    my_list.insert(78);
    my_list.insert(456);
    expect(my_list.to_string()).toEqual('{ 456 } -> { 78 } -> { 15 } -> NULL');
  });
});

describe('Testing includes function', () => {
  it('should return a value of true when finding the value', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.includes(5)).toEqual(true);
  });
  it('should return a value of false when not finding the value', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.includes(48)).toEqual(false);
  });
});


describe('Testing string function', () => {
  it('should return a string containing all of the nodes', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 7 } -> NULL');
  });
});

describe('Testing append method', () => {
  it('should append nodes to end of linked list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 7 } -> NULL');
  });
});

describe('Testing insertBefore method', () => {
  it('should insert node before a node in the middle of linked list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    my_list.insertBefore(3, 12);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 12 } -> { 3 } -> { 7 } -> NULL');
  });
  it('should insert node before the first node', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    my_list.insertBefore(5, 12);
    expect(my_list.to_string()).toEqual('{ 12 } -> { 5 } -> { 3 } -> { 7 } -> NULL');
  });
  it('should retrun a string if the value is not in the list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.insertBefore(17, 55)).toEqual('value is not in linked list');
  });
});


describe('Testing insertAfter', () => {
  it('should insert after a node in the middle of the list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    my_list.insertAfter(3, 'hello');
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { hello } -> { 7 } -> NULL');
  });

  it('should insert after the last node of the list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    my_list.insertAfter(7, 'hello');
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 7 } -> { hello } -> NULL');
  });
});

// stretch goal

describe('Testing delete method', () => {
  it('should remove node with given value from the list', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    my_list.deleteValue(3);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 7 } -> NULL');
  });
});

describe('Testing Where k is greater than the length of the linked list', () => {
  it('should return that it cannot be done', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.kth_from_end(8)).toEqual('this list is not that long. choose a smaller number');
  });
});

describe('Testing Where k is the same as the length of the list', () => {
  it('should return that it cannot be done', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.kth_from_end(3)).toEqual('this list is not that long. choose a smaller number');
  });
});

describe('Testing Where k is a negative integer', () => {
  it('should return that it cannot be done', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.kth_from_end(-1)).toEqual('what is this calculus??? choose a positive number!');
  });
});

describe('Testing Where the linked list only has 1 item', () => {
  it('should return that it cannot be done', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    expect(my_list.kth_from_end(1)).toEqual('omg this is embarassing but the list only has 1 item....awkward');
  });
});

describe('Testing Where kth method works', () => {
  it('should return k-th value from the end of a linked list', () => {
    let my_list = new LinkedList();
    my_list.append(1);
    my_list.append(3);
    my_list.append(8);
    my_list.append(2);
    expect(my_list.kth_from_end(2)).toEqual(3);
  });
});
