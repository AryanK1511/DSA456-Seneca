def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = start + int(((end - start) / 2))
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)) # Output: 9
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # Output: -1