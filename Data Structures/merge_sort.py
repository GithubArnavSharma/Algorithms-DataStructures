def split(the_list):
  """
  Divide the un-sorted list at midpoint into sublists
  Returns the left and right sub-lists
  """
  
  midpoint = len(the_list)//2
  left = the_list[:midpoint]
  right = the_list[midpoint:]
  
  return left, right

def merge(left, right):
  """
  Merges two lists and sorts them
  Returns the merged list
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
  """
  
  if len(the_list) <= 1:
    return the_list
  
  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  
  return merge(left, right)

