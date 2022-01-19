'use strict';
const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const zipLists = require('../index');

const LinkedList = require('../../../linked-list');

describe('LinkedList', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing linked list zipper function', () => {
  it('should take in 2 linked lists and return 1 linked list with the values zippered', () => {
    let my_list = new LinkedList();
    my_list.insert(1);
    my_list.insert(2);
    my_list.insert(3);
    let my_list2 = new LinkedList();
    my_list2.insert(5);
    my_list2.insert(10);
    my_list2.insert(15);
    zipLists(my_list,my_list2);
    expect(my_list.to_string()).toEqual('{ 3 } -> { 15 } -> { 2 } -> { 10 } -> { 1 } -> { 5 } -> NULL');
  });
});
