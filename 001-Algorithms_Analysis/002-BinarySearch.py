def binary_search(arr, key):
    start = 0 # 1
    end = len(arr) - 1 # 3

		# loop runs (log_2 n + 1) times
    while (start <= end): # 1
        mid = start + int(((end - start) / 2)) # 1 + 1 + 1 + 1 + 1 = 5
        if arr[mid] == key: # 1
            return mid
        elif arr[mid] > key: # 1
            end = mid - 1
        elif arr[mid] < key: # 1
            start = mid + 1 # 1
    return -1 # 1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)) # Output: 9
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # Output: -1