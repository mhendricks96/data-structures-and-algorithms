
def insertion_sort(start_list):
  # loop through every item in the list starting with the second item
  for i in range(1, len(start_list)):
    # variable to mark the vaue of item in current outer loop
    current = start_list[i]
    # variable to mark the position of item in current outer loop
    position = i
    #checks if current item is less than the item before it and not at 0 index
    while current < start_list[position - 1] and position > 0:
      # if so, flip current item with item before it
      start_list[position] = start_list[position - 1]
      # decrement position variable to be accurate
      position = position - 1
    # if not, leave in current position
    start_list[position] = current