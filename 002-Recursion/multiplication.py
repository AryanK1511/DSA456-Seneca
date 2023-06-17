def multiplication(a, b):
    # Base case: if either input is 0, return 0
    if a == 0 or b == 0:
        return 0

    # Recursive step: return one input added to a recursive call with the other input decremented by 1
    return a + multiplication(a, b - 1)

# Test cases
print(multiplication(2, 3))  # Output: 6
print(multiplication(5, 4))  # Output: 20
print(multiplication(0, 7))  # Output: 0
print(multiplication(9, 0))  # Output: 0