const mergeSort = require('./mergeSort');
const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('merge Sort', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe ('Testing merge Sort', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [8,4,23,42,16,15];
    mergeSort(my_array);
    expect(my_array).toEqual([4,8,15,16,23,42]);
  });
});

describe ('Testing merge Sort few uniques', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [5,12,7,5,5,7];
    mergeSort(my_array);
    expect(my_array).toEqual([5,5,5,7,7,12]);
  });
});

describe ('Testing merge Sort reversed', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [20,18,12,8,5,-2];
    mergeSort(my_array);
    expect(my_array).toEqual([-2,5,8,12,18,20]);
  });
});

describe ('Testing merge Sort nearly sorted', () => {
  it('should return the array in a sorted order', () => {
    let my_array = [2,3,5,7,13,11];
    mergeSort(my_array);
    expect(my_array).toEqual([2,3,5,7,11,13]);
  });
});
