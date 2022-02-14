const insertionSort = require('./insertionSort');
const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('Insertion Sort', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe ('Testing Insertion Sort', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [4,7,3,8,1,17,11,5];
    insertionSort(my_array);
    expect(my_array).toEqual([1,3,4,5,7,8,11,17]);
  });
});

describe ('Testing Insertion Sort few uniques', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [5,12,7,5,5,7];
    insertionSort(my_array);
    expect(my_array).toEqual([5,5,5,7,7,12]);
  });
});

describe ('Testing Insertion Sort reversed', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [20,18,12,8,5,-2];
    insertionSort(my_array);
    expect(my_array).toEqual([-2,5,8,12,18,20]);
  });
});

describe ('Testing Insertion Sort nearly sorted', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [2,3,5,7,13,11];
    insertionSort(my_array);
    expect(my_array).toEqual([2,3,5,7,11,13]);
  });
});

