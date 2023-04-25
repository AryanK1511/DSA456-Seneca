def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[minIndex]):
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    return arr

print(selectionSort([5, 2, 1, 4, 3, 7, 9, 5, 6, 9, 7, 8, 9, 4, 2, 3, 4, 5]))