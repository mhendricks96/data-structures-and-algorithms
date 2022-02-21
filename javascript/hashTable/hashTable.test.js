'use strict';

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');
const HashTable = require('./index');

describe('Hash Tables', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Hash Table creation', () => {
  it('should instantiate an empty Hash Table', () => {
    let hashTable = new HashTable();
    expect(hashTable).toBeTruthy();
  });
});


