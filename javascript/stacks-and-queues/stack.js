
class Node {
  constructor(value,next) {
    this.value = value;
    this.next = next;
  }
}

class Stack {
  constructor(){
    this.top = null;
    this.length = 0;
  }

  len(){
    return this.length;
  }

  is_empty() {
    if (this.length === 0){
      return true;
    } else {
      return false;
    }
  }

  peek() {
    if (this.is_empty()) {
      return 'Sorry, this stack is empty';
    } else {
      return this.top.value;
    }
  }

  push(value) {
    let node = new Node(value);
    if (this.top === null){
      this.top = node;
    } else {
      node.next = this.top;
      this.top = node;
    }
    this.length += 1;
    return;
  }

  pop() {
    if (this.is_empty()){
      return 'This stack is already empty';
    } else {
      let popped = this.top;
      this.top = popped.next;
      popped.next = null;
      this.length -= 1;
      return popped.value;
    }
  }
}

module.exports = Stack;
