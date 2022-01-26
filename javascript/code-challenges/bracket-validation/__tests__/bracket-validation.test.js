'use strict';
const validateBrackets = require('../index');
const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('Validate brackets', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing correct validations', () => {
  it('should return true to even brackets', () => {
    expect(validateBrackets('{}')).toEqual(true);
    expect(validateBrackets('{}(){}')).toEqual(true);
    expect(validateBrackets('()[[Extra Characters]]')).toEqual(true);
    expect(validateBrackets('{}{Code}[Fellows](())	')).toEqual(true);
    expect(validateBrackets('{}(){}')).toEqual(true);
  });
});

describe('Testing incorrect validations', () => {
  it('should return false to uneven brackets', () => {
    expect(validateBrackets('[({}]	')).toEqual(false);
    expect(validateBrackets('(](')).toEqual(false);
    expect(validateBrackets('{(})	')).toEqual(false);
  });
});
