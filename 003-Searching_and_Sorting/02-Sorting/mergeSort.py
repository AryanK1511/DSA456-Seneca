# ========== NORMAL MERGE SORT ==========
def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    mid = int(len(arr) / 2)

    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])
    return merge(left, right)

def merge(first, second):
    mix = [0]*(len(first) + len(second))
    i, j, k = 0, 0, 0
    while (i < len(first) and j < len(second)):
        if (first[i] < second[j]):
            mix[k] = first[i]
            i += 1
        else:
            mix[k] = second[j]
            j += 1
        k += 1
    # It may be possible that one of the arrays in not complete
    # Only one of the following two loops will run
    while (i < len(first)):
        mix[k] = first[i]
        i += 1
        k += 1
    while (j < len(second)):
        mix[k] = second[j]
        j += 1
        k += 1

    return mix

# ========== PYTHON SPECIFIC MERGE SORT ==========

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
