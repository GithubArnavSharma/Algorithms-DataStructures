the_list = [1, 2, 3]
first_value = the_list[0]

if 1 in the_list:
  print(True)

if 4 in the_list:
  print(True)
  
for n in the_list:
  if n == 2:
    print(True)
    break
    
the_list.append(4)
the_list.pop(3)
print(the_list)
