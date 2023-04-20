def factorial(num):
    fact = 1 # 1
    for i in range(1, num + 1): # (n - 1) + 1 + 1
																# (n-1) loop iterations
                                # 1 more for + operator
                                # 1 more for call to range function
        fact *= i  # 2(n-1)
                    # 2 as there are two operators
                    # (n-1) as loop runs n-1 times
    return fact     # 1

print(factorial(4)) # Output: 24