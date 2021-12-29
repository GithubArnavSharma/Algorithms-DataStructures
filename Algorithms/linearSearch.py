def linear_search(the_list, target):
  for i in range(0, len(the_list)-1):
    if the_list[i] == target:
      return i
  return None

def verify_search(index):
  if index is not None:
    print("Target found at index " + str(index))
  else:
    print("Target not found in list")
    
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

search_4 = linear_search(the_list, 4)
search_10 = linear_search(the_list, 10)

verify_search(search_4)
verify_search(search_10)
