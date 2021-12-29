def recursive_binary_search(the_list, target):
  if len(the_list) == 0:
    return False
  
  midpoint = len(the_list)//2
  num_mid = the_list[midpoint]
  
  if num_mid == target:
    return True
  elif num_mid < target:
    return recursive_binary_search(the_list[midpoint+1:], target)
  else:
    return recursive_binary_search(the_list[:midpoint], target)

def verify_recursive_search(result):
  if result == True:
    print("Target is in the list")
  else:
    print("Target is not in the list")
    
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

search_7 = recursive_binary_search(the_list, 7)
search_11 = recursive_binary_search(the_list, 11)

verify_recursive_search(search_7)
verify_recursive_search(search_11)
