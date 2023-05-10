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

# ========== IN PLACE MERGE SORT ==========

print(mergeSort([5, 2, 1, 4, 3, 7, 9, 5, 6, 9, 7, 8, 9, 4, 2, 3, 4, 5]))