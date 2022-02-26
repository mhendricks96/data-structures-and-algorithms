'use strict';

const leftJoin = (map1, map2) => {
  let finalValues = [];



  map1.forEach((value, key) => {
    // let currentArray = [value, key];
    let currentDict = {};
    let valuesDict = {};

    valuesDict['synonym'] = value;


    if (map2.has(key)) {
      valuesDict['antonym'] = map2.get(key);
    } else {
      valuesDict['antonym'] = null;
    }
    currentDict[key] = valuesDict;
    finalValues.push(currentDict);
  });

  // map1.forEach((value, key) => {
  //   // let currentArray = [value, key];
  //   let currentDict = new Map();
  //   let valuesDict = new Map();

  //   valuesDict.set('synonym', value);


  //   if (map2.has(key)) {
  //     valuesDict.set('antonym', map2[key]);
  //   } else {
  //     valuesDict.set('antonym', null);
  //   }
  //   currentDict.set(key, valuesDict);
  //   finalValues.push(currentDict);
  // });

  return finalValues;
};

module.exports = leftJoin;
