'use strict';

class Node {
  constructor(value, next){
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor(){
    this.head = null;
    this.length = 0;
  }

  append(value){
    let node = new Node(value);
    if (this.head === null){
      this.head = node;
      this.length += 1;
      return;
    }

    let current = this.head;
    while (current.next){
      current = current.next;
    }
    current.next = node;
    this.length += 1;
  }

  insert(value){
    let node = new Node(value);
    if (this.head === null){
      this.head = node;
      this.length += 1;
      return;
    }
    node.next = this.head;
    this.head = node;
    this.length += 1;
  }

  includes(value){
    let current = this.head;
    while (current){
      if (current.value === value){
        return true;
      }
      current = current.next;
    }
    return false;
  }

  to_string (){
    let current = this.head;
    let values = [];
    let answer = '';

    while (current) {
      values.push(current.value);
      current = current.next;
    }

    for (let i = 0; i < values.length; i++){
      answer += `{ ${values[i]} } -> `;
    }
    return (`${answer}NULL`);
  }

}

module.exports = LinkedList;
