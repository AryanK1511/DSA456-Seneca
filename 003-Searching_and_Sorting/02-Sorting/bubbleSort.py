def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, (len(arr) - i - 1)):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubbleSort([5, 2, 1, 4, 3, 7, 9, 5, 6, 9, 7, 8, 9, 4, 2, 3, 4, 5]))