def binarySearch(arr, key):
    # Calculate the start and end index of the array
    start = 0
    end = len(arr) - 1

    # start should always be less than the end
    while (start <= end):
        # Calculate the middle index
        middle = start + ((int)((end - start) / 2))
        # Check whether the element in the middle is the kwy
        if arr[middle] == key:
            return middle
        # Check whether middle element is greater than key
        elif arr[middle] > key:
            # The element has to be towards the left
            end = middle - 1
        # Check whether the middle element is smaller than the key
        elif arr[middle] < key:
            # The element has to be on the right of the middle
            start = middle + 1
    return -1

print(binarySearch([100, 200, 300, 400, 500, 600, 700, 800], 700))