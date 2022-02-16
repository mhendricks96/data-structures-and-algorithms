'use strict';

const findPivot = (array, first, last) => {
  //define pivot(using first element here)
  let pivot = array[first];
  //define 'left' as the element right after the pivot
  let left = first + 1;
  //define 'right' as the last element
  let right = last;

  // eslint-disable-next-line no-constant-condition
  while (true) {
    //see if 'left' element is less than 'right' element and pivot element. if so, make the next element 'left'
    while ((left < right) && array[left] <= pivot) {
      left = left + 1;
    }
    //see if 'left' element is less than 'right' element and 'right' element is greater than pivot element. if so, make the previous element 'right'
    while ((left < right) && (array[right] >= pivot)){
      right = right - 1;
    }
    // once right and left meet, break out of while loop
    if (right <= left){
      break;
    } else {
      //switch left and right items
      [array[left], array[right]] = [array[right], array[left]];
    }
  }
  // after while loop is done, switch first and right items
  [array[first],array[right]] = [array[right], array[first]];
};

const mainFunction = (array, first, last ) => {
  // run until first === last which means the list has only one item
  if (first < last) {
    //put pivot(first item) in proper place with all items less than it to the left, and all items greater than it to the right
    let pivot = findPivot(array, first, last);
    // run recursively on everythin to the left of the pivot and then everything on the right of the pivot.
    mainFunction(array, first, pivot - 1);
    mainFunction(array, pivot + 1, last);
  }
};

const quickSort = (array) => {
  // start function by finding the first and last elements and sending them to the main function.
  let last = array.length - 1;
  mainFunction(array, 0, last);
};

module.exports = quickSort;
