'use strict';

// const Stack = require('../../stacks-and-queues/stack');

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class AnimalShelter {
  constructor() {
    this.front = null;
    this.back = null;
    this.length = 0;
    // this.holding_stack = new Stack();
    this.nodes_rotated = 0;
  }

  is_empty(){
    return (this.length === 0);
  }

  enqueue(animal) {
    let new_animal = new Node(animal);

    if (this.is_empty()) {
      this.front = new_animal;
    } else {
      this.back.next = new_animal;
    }
    this.back = new_animal;
    this.length++;
  }

  dequeue(preference) {
    if (this.is_empty()) {
      return 'Sorry, No Animals Available';
    }
    let next_up = this.front;

    while (next_up){
      if (next_up.value === preference){
        let chosen_animal = next_up.value;
        next_up = next_up.next;
        this.length--;
        let times_to_rotate = this.length - this.nodes_rotated;

        for (let i = 0; i < times_to_rotate; i++) {
          let temp = next_up.value;
          next_up = next_up.next;
          let rotated_node = new Node(temp);
          this.back.next = rotated_node;
          this.back = rotated_node;
        }
        return chosen_animal;
      } else {
        let wrong_animal = next_up.value;
        if (!next_up.next){
          return 'Null';
        } else {
          next_up = next_up.next;
          let rotated_node = new Node(wrong_animal);
          this.back.next = rotated_node;
          this.back = rotated_node;
          this.nodes_rotated++;
        }
      }
    }
  }
}

module.exports = AnimalShelter;
