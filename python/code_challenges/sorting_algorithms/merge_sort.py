
def merge_sort(start_list):
  # if statement to break every sublist down to 1
  if len(start_list) > 1: 
    # find middle point of lists
    middle = len(start_list) // 2
    # create left sublist with everything before the middle
    left_list = start_list[:middle]
    # create right sublist with everything middle and after
    right_list = start_list[middle:]
    # recursively run function on right sublist
    merge_sort(right_list)
    # recursively run function on left sublist
    merge_sort(left_list)
    # create variables to hold indexes of left,right, and starting lists respectively
    i = 0 # left
    j = 0 # right
    k = 0 # starting list
    # while loop to that goes until list is merged
    while i < len(left_list) and j < len(right_list):
      # check if current index in left sublist is less than current index in right sublist
      if left_list[i] < right_list[j]:
        # if true, move element to current index in starting list
        start_list[k] = left_list[i]
        # move to next index in left sublist
        i += 1
        # move to next index in starting sublist
        k += 1
      else:
        # if not, move element from right sublist to starting list
        start_list[k] = right_list[j]
        # move to next index in left sublist
        j += 1
        # move to next index in starting sublist
        k += 1
    # add leftovers to end of list
    while i < len(left_list):
      start_list[k] = left_list[i]
      i += 1
      k += 1
    while j < len(right_list):
      start_list[k] = right_list[j]
      j += 1
      k += 1

