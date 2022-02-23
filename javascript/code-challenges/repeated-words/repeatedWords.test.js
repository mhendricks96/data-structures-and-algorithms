const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

const reapeatedWord = require('./index');

describe('Reapeated Word', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Testing Reapeated Word functions', () => {
  it('Should return the first word that is repeated', () => {
    expect(reapeatedWord('some days are just the perfect weather days')).toEqual('days');
  });
});

describe('Testing output first only', () => {
  it('Should return the first word that is repeated', () => {
    expect(reapeatedWord('some days just have the perfect weather and some days dont')).toEqual('some');
  });
});

describe('Testing long input', () => {
  it('Should return the first word that is repeated', () => {
    expect(reapeatedWord('It was a queer, sultry summer the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')).toEqual('summer');
  });
});
