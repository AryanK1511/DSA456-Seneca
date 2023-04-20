def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(factorial(4)) # Output: 24