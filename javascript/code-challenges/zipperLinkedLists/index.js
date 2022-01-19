// const LinkedList = require('../../linked-list');

const zipLists = (ll1, ll2) => {
  let list1Current = ll1.head;
  let list2Current = ll2.head;

  while ((list1Current) && (list2Current)){
    let list1Next = list1Current.next;
    let list2Next = list2Current.next;

    list2Current.next = list1Next;
    list1Current.next = list2Current;

    list1Current = list1Next;
    list2Current = list2Next;
  }
  ll2.head = list2Current;
};

module.exports = zipLists;


