def sumOfDigits(num):
    if num <= 0:
        return 0
    last = num % 10
    num = int(num / 10)
    return last + sumOfDigits(num)

print(sumOfDigits(726))