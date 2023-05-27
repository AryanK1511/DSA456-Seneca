# Function to calculate the nth fibonacci number
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        prev, curr = 1, 1
        for i in range(3, n + 1):
            temp = prev + curr
            prev, curr = curr, temp
        return curr

# Checks for two numbers in the given nums list whose sum is equal to the specified goal
def sum_to_goal(nums, goal):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (nums[i] + nums[j] == goal):
                return nums[i] * nums[j]
    return 0

    