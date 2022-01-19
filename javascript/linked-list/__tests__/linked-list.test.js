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

describe('Testing Linked List insertion', () => {
  it('should be able to add to array with insertions', () => {
    let my_list = new LinkedList();
    my_list.append(5); // append method works
    my_list.append(3);
    my_list.append(7);
    expect(my_list.length).toEqual(3);
    expect(my_list.head.value).toEqual(5);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 7 } -> NULL');
    my_list.insertBefore(7, 12);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 12 } -> { 7 } -> NULL');
    expect(my_list.insertBefore(17, 55)).toEqual('value is not in linked list');
    my_list.insertAfter(5, 'hello');
    expect(my_list.to_string()).toEqual('{ 5 } -> { hello } -> { 3 } -> { 12 } -> { 7 } -> NULL');
    expect(my_list.insertBefore(17, 55)).toEqual('value is not in linked list');
    my_list.deleteValue(3);
    expect(my_list.to_string()).toEqual('{ 5 } -> { hello } -> { 12 } -> { 7 } -> NULL');
  });
});
