const LinkedList = require('../linked-list');

class HashTable {
  constructor(size=1024){
    this.size = size;
    this.buckets = [null] * this.size;
  }

  set(key, value){
    let index = this.hash(key);

    if (this.contains(index)){
      return 'sorry, can only accept 1 value per key.';
    }

    if (this.buckets[index] !== null){
      this.buckets[index] = new LinkedList();
    }

    let bucket = this.buckets[index];
    bucket.append([key, value]);
  }

  get(key){
    if (this.contains(key) === false) {
      return 'sorry, key not found';
    }
    let index = this.hash(key);
    let bucket = this.buckets[index];

    let current = bucket.head;

    while (current !== null) {
      if (current.value[0] === key) {
        return current.value[1];
      }
      current = current.next;
    }
  }

  contains(key){
    let index = this.hash(key);
    let bucket = this.buckets[index];

    if (bucket) {
      let current = bucket.head;
      while (current !== null) {
        if (current.value[0] === key) {
          return true;
        }
        current = current.next;
      }
    }
    return false;
  }

  hash(key){
    let char_total = 0;

    for (let i=0; i < key.length; i++) {
      let char = String.fromCharCode(key[i]);
      char_total += char;
    }
    let product = char_total * 599;
    let index = product % this.size;
    return index;
  }
}

module.exports = HashTable;
