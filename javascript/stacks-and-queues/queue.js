
class Node {
  constructor(value,next) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  constructor(){
    this.front = null;
    this.back = null;
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
      return 'Sorry, this Queue is empty';
    } else {
      return this.front.value;
    }
  }

  enqueue(value) {
    let node = new Node(value);
    if (this.is_empty()) {
      this.front = node;
      this.back = node;
    } else {
      let temp = this.back;
      this.back = node;
      temp.next = node;
    }
    this.length += 1;
    return;
  }

  dequeue() {
    if (this.is_empty()){
      return 'This Queue is already empty';
    } else {
      let result = this.peek();
      this.front = this.front.next;
      this.length -= 1;
      if (!this.fron){
        this.back = null;
      }
      return result;
    }
  }
}

module.exports = Queue;
