def split(the_list):
  """
  Divide the un-sorted list at midpoint into sublists
  Returns the left and right sub-lists
  Overall Time Complexity: O(log n)
  """
  
  midpoint = len(the_list)//2
  left = the_list[:midpoint]
  right = the_list[midpoint:]
  
  return left, right

def merge(left, right):
  """
  Merges two lists and sorts them
  Returns the merged list
  Overall Time Complexity: O(n)
  """
  
  merged = []
  i = 0
  j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
      
  for x in range(i, len(left)):
    merged.append(left[x])

  for x in range(j, len(right)):
    merged.append(right[x])
    
  return merged

def merge_sort(the_list):
  """
  Sorts a list in ascending order
  Returns a new sorted list
  1. Divide - Find the midpoint of the list and divide into sub-lists
  2. Conquer - Recursively sort the sub-lists created in step 1
  3. Combine - Merge the recursively sorted sub-listed from step 2
  
  Time Complexity: O(n log n)
  """
  
  if len(the_list) <= 1:
    return the_list
  
  left_half, right_half = split(the_list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  
  return merge(left, right)

def verify_sorted(the_list):
  if len(the_list) <= 1:
    return True
  
  return the_list[0] <= the_list[1] and verify_sorted(the_list[1:])

print(merge_sort([4,5,2,4,5,23,2,4]))
