def sum_digits(num):
  if (num < 10):
    return num
  return num % 10 + sum_digits(num // 10)

# test cases
print(sum_digits(12))
print(sum_digits(552))
print(sum_digits(123456789) == 45)