import random

def quick_sort(the_list):
  if len(the_list) <= 1:
    return the_list
  
  less_pivot = []
  more_pivot = []
  pivot = the_list[random.randint(0, len(the_list)-1)]
  
  for value in the_list[1:]:
    if value <= pivot:
      less_pivot.append(value)
    else:
      more_pivot.append(value)
      
  return quick_sort(less_pivot) + [pivot] + quick_sort(more_pivot)

numbers = [6,4,7,8,2,4,6,1,2,7,8,3]
print(quick_sort(numbers))
