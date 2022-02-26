'use strict';

const { it, describe } = require('eslint/lib/rule-tester/rule-tester');

const leftJoin = require('./index');

describe('Left Join', () => {
  it('works', () => {
    expect(true).toBeTruthy();
  });
});

describe('testing left join', () => {
  it('should return single data structure', () => {
    let map1 = new Map();
    let map2 = new Map();
    map1.set('diligent', 'employed');
    map1.set('fond', 'enamored');
    map1.set('guide', 'usher');
    map1.set('outfit', 'garb');
    map1.set('wrath', 'anger');
    map2.set('diligent', 'idle');
    map2.set('fond', 'averse');
    map2.set('guide', 'follow');
    map2.set('flow	', 'jam');
    map2.set('wrath', 'delight');

    expect(leftJoin(map1, map2)).toEqual([{'diligent':{'antonym':'idle','synonym':'employed'}}, {'fond':{'antonym':'averse','synonym':'enamored'}},{'guide':{'antonym':'follow','synonym':'usher'}},{'outfit':{'antonym':null,'synonym':'garb'}},{'wrath':{'antonym':'delight','synonym':'anger'}}]);
  });
});

describe('testing left join again', () => {
  it('should return single data structure', () => {
    let map1 = new Map();
    let map2 = new Map();

    map1.set('mike', 'great');
    map1.set('buster', 'cuddly');
    map2.set('mike', 'old');
    map2.set('buster', 'mean');

    expect(leftJoin(map1, map2)).toEqual([{'mike':{'antonym':'old','synonym':'great'}}, {'buster':{'antonym':'mean','synonym':'cuddly'}},]);
  });
});
