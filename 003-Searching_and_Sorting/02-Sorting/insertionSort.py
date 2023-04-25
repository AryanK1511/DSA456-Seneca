def insertionSort(arr):
    for i in range(0, (len(arr) - 1)):
        j = i + 1
        while j > 0:
            if (arr[j] < arr[j - 1]):
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                j -= 1
            else:
                break
    return arr

print(insertionSort([5, 2, 1, 4, 3, 7, 9, 5, 6, 9, 7, 8, 9, 4, 2, 3, 4, 5]))