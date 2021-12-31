def get_min(unsorted):
    current_min = unsorted[0]
    idx = 0
    for i in range(1, len(unsorted)):
        if unsorted[i] < current_min:
            current_min = unsorted[i]
            idx = i
    return current_min, idx

def selection_sort(arr):
    sorted_arr = []
    while len(arr) > 0:
        the_min, idx = get_min(arr)
        sorted_arr.append(the_min)
        arr.pop(idx)
    return sorted_arr

numbers = [4, 6, 5, 2, 7, 5, 3, 9, 2, 8]

print(selection_sort(numbers))
