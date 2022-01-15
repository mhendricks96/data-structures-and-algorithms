'use strict';

const { it } = require('eslint/lib/rule-tester/rule-tester');
// Require our linked list implementation
const LinkedList = require('../index');

describe('Linked List', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });  
});

describe('Testing Linked List creation', () => {
  it('should return that the array i created', () => {
    let my_list = new LinkedList();
    my_list.append(5);
    my_list.append(3);
    my_list.append(7);
    expect(my_list.length).toEqual(3);
    expect(my_list.head.value).toEqual(5);
    expect(my_list.includes(48)).toEqual(false);
    expect(my_list.includes(5)).toEqual(true);
    expect(my_list.to_string()).toEqual('{ 5 } -> { 3 } -> { 7 } -> NULL');
    my_list.insert(15);
    expect(my_list.head.value).toEqual(15);
    let my_list2 = new LinkedList();
    my_list2.insert(99);
    expect(my_list2.head.value).toEqual(99);
  });
});
