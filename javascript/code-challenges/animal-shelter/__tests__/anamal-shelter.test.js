'use strict';
const AnimalShelter = require('../index');

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

describe('Animal Shelter', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('Test Creating Shelter', () => {
  it('shoul create an empty shelter', () => {
    let shelter = new AnimalShelter;
    expect(shelter).toBeTruthy;
  });
});

describe('Testing single animal ', () => {
  it('should enqueue and deque a cat', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('cat');
    expect(shelter.dequeue('cat')).toEqual('cat');
  });
  it('should enqueue and deque a dog', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('dog');
    expect(shelter.dequeue('dog')).toEqual('dog');
  });
});

describe('Testing Null return', () => {
  it('should return null when not finding a dog', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('cat');
    expect(shelter.dequeue('dog')).toEqual('Null');
  });
  it('should return null when not finding a cat', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('dog');
    expect(shelter.dequeue('cat')).toEqual('Null');
  });
});

describe('Testing Finding animal in Queue', () => {
  it('should return a dog even if if not first in list', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('cat');
    shelter.enqueue('cat');
    shelter.enqueue('dog');
    shelter.enqueue('cat');
    expect(shelter.dequeue('dog')).toEqual('dog');
    expect(shelter.length).toEqual(3);
  });
  it('should return a cat even if if not first in list', () => {
    let shelter = new AnimalShelter;
    shelter.enqueue('dog');
    shelter.enqueue('dog');
    shelter.enqueue('dog');
    shelter.enqueue('cat');
    expect(shelter.dequeue('cat')).toEqual('cat');
    expect(shelter.length).toEqual(3);
  });
});

