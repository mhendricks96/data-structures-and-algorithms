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
  }
}


let node = new Node('Michae');
let list = new LinkedList();
list.head = node;


module.exports = LinkedList;
