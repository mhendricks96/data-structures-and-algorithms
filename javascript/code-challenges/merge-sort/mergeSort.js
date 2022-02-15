'use strict';

const mergeSort = (startArray) => {
  // if statement to break every subarray down to 1
  if (startArray.length > 1) {
    // find middle point of array
    let middle = Math.ceil(startArray.length / 2);
    //create left subarray with everything before the middle
    let leftArray = startArray.slice(0, middle);
    //create left subarray with everything before the middle
    let rightArray = startArray.slice(middle, startArray.length);
    // recursively run function on right and leftsubarrays
    mergeSort(rightArray);
    // eslint-disable-next-line no-unused-vars
    mergeSort(leftArray);
    //create variables to hold indexes of left,right, and starting arrays respectively
    let i = 0;//left
    let j = 0;//right
    let k = 0;//startArray
    // while loop to that goes until array is merged
    while ((i < leftArray.length) && (j < rightArray.length)){
      // check if current index in left subarray is less than current index in right subarray
      if (leftArray[i] < rightArray[j]){
        // if true, move element to current index in starting array
        startArray[k] = leftArray[i];
        // move to next index in left subarray
        i += 1;
        // move to next index in starting subarray
        k += 1;
      } else {
        // if not, move element from right subarray to starting subarray
        startArray[k] = rightArray[j];
        // move to next index in left subarray
        j += 1;
        // move to next index in starting subarray
        k += 1;
      }
    }
    // add leftovers to end of array
    while (i < leftArray.length) {
      startArray[k] = leftArray[i];
      i += 1;
      k += 1;
    }
    while (j < rightArray.length) {
      startArray[k] = rightArray[j];
      j += 1;
      k += 1;
    }
  }
};

module.exports = mergeSort;
