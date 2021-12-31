import random

numbers = [5,3,8,9,2,4]

def is_sorted(the_list):
  for index in range(len(the_list)-1):
    if the_list[index] > the_list[index + 1]:
      return False
  return True

def bogo_sort(values):
  while not is_sorted(values):
    random.shuffle(values)
  return values

print(bogo_sort(numbers))
