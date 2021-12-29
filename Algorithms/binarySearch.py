def binary_search(the_list, target):
  start = 0
  end = len(the_list) - 1
  
  while start <= end:
    midpoint = (start + end)//2
    num_mid = the_list[midpoint]
    
    if num_mid == target:
      return midpoint
    elif num_mid < target:
      start = midpoint + 1
    else:
      end = midpoint - 1
 
  return None

def verify_search(index):
  if index is not None:
    print("Target found in index " + str(index))
  else:
    print("Target not found in list")
    
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

search_9 = binary_search(the_list, 9)
search_0 = binary_search(the_list, 0)

verify_search(search_9)
verify_search(search_0)
