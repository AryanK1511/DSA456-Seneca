def recursiveBinarySearch(arr, target, start, end):
    if (start > end):
        return -1
    middle = start + int((end - start) / 2)
    if (arr[middle] == target):
        return middle
    if (target < arr[middle]):
        return recursiveBinarySearch(arr, target, start, middle - 1)
    elif (target > arr[middle]):
        return recursiveBinarySearch(arr, target, middle + 1, end)

print(recursiveBinarySearch([1, 2, 3, 4, 5], 2, 0, 4))