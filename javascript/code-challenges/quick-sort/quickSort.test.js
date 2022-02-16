const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

const quickSort = require('./quickSort');

describe('quick Sort', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('testing quick Sort', () => {
  it ('should return return the array in a sorted order', () => {
    let myArray = [8,4,23,42,16,15];
    quickSort(myArray);
    expect(myArray).toEqual([]);
  });
});
