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

  insertBefore(value, newValue){
    let newNode = new Node(newValue);
    let current = this.head;

    if (current.value === value){
      newNode.next = current;
      this.head = newNode;
    }

    while (current.next){
      if (current.next.value === value){
        newNode.next = current.next;
        current.next = newNode;
        return;
      }
      current = current.next;
    }
    return 'value is not in linked list';
  }

  insertAfter(value, newValue) {
    let newNode = new Node(newValue);
    let current = this.head;

    while (current){
      if (current.value === value){
        newNode.next = current.next;
        current.next = newNode;
        return;
      }
      current = current.next;
    }
    return 'value is not in linked list';
  }

  // Stretch goal
  deleteValue(value){
    let current = this.head;
    while (current.next){
      if (current.next.value === value){
        current.next = current.next.next;
      }
      current = current.next;
    }
    return 'value is not in linked list';
  }

  kth_from_end(k){
    if (this.length < 2){
      return 'omg this is embarassing but the list only has 1 item....awkward';
    } else if (k < 0){
      return 'what is this calculus??? choose a positive number!';
    } else if (k >= this.length){
      return 'this list is not that long. choose a smaller number';
    } else {
      let current = this.head;
      let target = this.length - k;
      for (let i = 0; i < target-1; i++){
        current = current.next;
      }
      return current.value;
    }
  }

}

module.exports = LinkedList;
