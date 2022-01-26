const Stack = require('../../stacks-and-queues/stack');

const ValidateBrackets = (string) => {
  let stack = new Stack();
  let startBrackets = ['(', '{','['];
  let endBrackets = ['}', ']', ')'];
  for (let i = 0; i < string.length; i++){
    if (startBrackets.includes(string[i])){
      stack.push(string[i]);
    } else if (endBrackets.includes(string[i])){
      if (stack.is_empty()){
        return false;
      } else {
        let openingBracket = stack.pop();
        if (openingBracket === '('){
          if (string[i] !== ')'){
            return false;
          }
        } else if (openingBracket === '{'){
          if (string[i] !== '}'){
            return false;
          }
        } else if (openingBracket === '['){
          if (string[i] !== ']'){
            return false;
          }
        }
      }
    }
  }
  if (stack.is_empty()){
    return true;
  } else {
    return false;
  }
};

module.exports = ValidateBrackets;
