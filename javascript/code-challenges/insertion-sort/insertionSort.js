'use strict';


const insertionSort = (startArray) => {
  for (let i = 1; i <= startArray.length - 1; i++) {
    // variable to mark the vaue of item in current outer loop
    let current = startArray[i];
    // variable to mark the position of item in current outer loop
    let position = i;
    // checks if current item is less than the item before it and not at 0 index
    while ((current < startArray[position - 1]) && (position > 0)) {
      // if so, flip current item with item before it
      startArray[position] = startArray[position - 1];
      // decrement position variable to be accurate
      position = position - 1;
    }
    // if not, leave in current position
    startArray[position] = current;
  }
};

module.exports = insertionSort;
