'use strict';

const reapeatedWord = (string) => {
  let my_hash = {};
  let splitString = string.split(' ');

  for (let i = 0; i < splitString.length; i++) {
    let count = 1;
    let word = splitString[i];

    if (word in my_hash) {
      my_hash[word] += 1;
      return word;
    } else {
      my_hash[word] = count;
    }

  }
};

module.exports = reapeatedWord;
