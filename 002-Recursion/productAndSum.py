# Product of the first n natural numbers
def product(n):
    if (n == 0):
        return 0
    if (n <= 2):
        return n
    return n * product(n - 1)

# Sum of the first n natural numbers
def sum(n):
    if (n == 0):
        return 0
    if (n < 2):
        return n
    return n + sum(n - 1)

print(product(4))
print(sum(4))