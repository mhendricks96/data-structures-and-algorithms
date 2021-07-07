from linked_list.linked_list import LinkedList, Node

def zipped_list(list1, list2):
    """
    function takes in 2 linked lists and returns a list with both link lists zippered together
    """
    list1_curr = list1.head
    list2_curr = list2.head
  
    while list1_curr != None and list2_curr != None:   
      list1_next = list1_curr.next
      list2_next = list2_curr.next
           
      list2_curr.next = list1_next 
      list1_curr.next = list2_curr 
      
      list1_curr = list1_next
      list2_curr = list2_next
    list2.head = list2_curr

def merge_sorted_list(list1, list2):
    
    """
    function takes in 2 ordered linked lists and returns an ordered link list containing all the nodes from both lists
    (recursive)
    """
    current1 = list1.head
    current2 = list2.head
    if current1 is None:
        return list2
    if current2 is None:
        return list1

    if (current1.value < current2.value):
        current1.next = merge_sorted_list(current1.next, list2)
        return list1
    else:
        current2.next = merge_sorted_list(current2.next, list1)
        return list2