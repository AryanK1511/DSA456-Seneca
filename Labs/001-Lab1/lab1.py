# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Aryan Khurana
# Student Number: 145282216
#

def wins_rock_scissors_paper(player, opponent):
    player, opponent = player.lower(), opponent.lower()
    return ((player == "rock" and opponent == "scissors") or (player == "paper" and opponent == "rock") or (player == "scissors" and opponent == "paper"))

def factorial(num):
    if (num < 2):
        return 1
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact


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

def sum_to_goal(nums, goal):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (nums[i] + nums[j] == goal):
                return nums[i] * nums[j]
    return 0

class UpCounter:
    def __init__(self, step = 1):
        self.countVal = 0
        self.step = step

    def count(self):
        return self.countVal

    def update(self):
        self.countVal += self.step

class DownCounter(UpCounter):
    def update(self):
        self.countVal -= self.step