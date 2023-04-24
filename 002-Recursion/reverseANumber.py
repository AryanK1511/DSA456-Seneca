# Using pythons inbuit str cast functionality
def reverseNumber(num):
    if (num < 10):
        return num
    return str((num % 10)) + str(reverseNumber(int(num / 10)))

# Using the len function
def reverse_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_number(n // 10)