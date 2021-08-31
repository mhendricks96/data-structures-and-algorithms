
def find_pivot_place(list1, first, last):
  #define pivot(using first element here)
  pivot = list1[first]
  #define 'left' as the element right after the pivot
  left = first + 1
  # define 'right' as the last element
  right = last

  while True:
    #see if 'left' element is less than 'right' element and pivot element. if so, make the next element 'left'
    while left <= right and list1[left] <= pivot:
        left += 1
    #see if 'left' element is less than 'right' element and 'right' element is greater than pivot element. if so, make the previous element 'right'
    while left <= right and list1[right] >= pivot:
        right -= 1
    # once right and left meet, break out of while loop
    if right < left:
        break
    else:
      # switch left and right items
        list1[left], list1[right] = list1[right], list1[left]
  # after while loop is done, switch first and right items
  list1[first], list1[right] = list1[right], list1[first]
  return right


def main_function(list1, first, last):
  # run until first == last which means the list only has one item
  if first < last:
    # put pivot(first item) in proper place with all items less than it to the left, and all items greater than it to the right
    pivot = find_pivot_place(list1,first,last)
    # run recursevly on everything to the left of the pivot
    main_function(list1, first, pivot - 1)
    # run recursevly on everything to the right of the pivot
    main_function(list1, pivot + 1, last)

def quick_sort(list1):
  # start function off by finding the first and last elements and sending them to the main function
  last = len(list1) - 1
  main_function(list1, 0, last)

