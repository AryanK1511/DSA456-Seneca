def find_min(arr, min = None):
  if (len(arr) == 0):
    return min
  if min is None or arr[0] < min:
    min = arr[0]
  return find_min(arr[1:], min)



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)