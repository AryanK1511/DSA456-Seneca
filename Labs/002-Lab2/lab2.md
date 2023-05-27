# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;                        # 1

	for i in range(0,number):       # n
		x = (i+1)                   # 2 * n
		total+=(x*x)                # 3 * n

	return total                    # 1
```

#### Function 1 Analysis
- Let n represent the number that is being passed as the parameter for function1.
- Let T(n) represent the number of operations needed to complete the function
- T(n) = 1 + n + 2n + 3n + 1
- T(n) = 6n + 2
- **T(N) is O(n)**

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6 # 6

```

#### Function 2 Analysis
- Let n represent the number that is being passed as the parameter for function2.
- Let T(n) represent the number of operations needed to complete the function
- T(n) = 6
- **T(n) is O(1)**

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.

```python

def function3(list):
	for i in range(0,len(list)-1):			# n + 1 + 1 + 1
		for j in range(0,len(list)-1-i): 	# 1 + 1 + 1 + 1 + (n - 1) + (n - 2) + ...... 1
			if(list[j]>list[j+1]):          # 1 + 1 + 1 + 1 = 4
				tmp=list[j]                 # 1 + 1 = 2
				list[j]=list[j+1]           # 1 + 1 + 1 + 1 = 4
				list[j+1]=tmp               # 1 + 1 + 1 = 3

```

#### Function 3 Analysis
- Let n represent the length of the list that is being passed as the parameter for function3.
- Let T(n) represent the number of operations needed to complete the function
- T(n) = n + 3 + 4 + 4 + 2 + 4 + 3 + [(n - 1) + (n - 2) + ....... 1]
- T(n) = n + n/2[(n - 1) + 1] + 20
- T(n) = n + ${n^2}$/2 + 20
- **T(n) is O(${n^2}$)**

### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1						# 1
	for i in range(1, number):  # (n - 1)
		total=total*(i+1)		# 3 * (n - 1)
	return total				# 1
```

#### Function 4 Analysis
- Let n represent the number passed as the parameter in function4
- Let T(n) represent the number of operations needed to complete the function
- T(n) = 1 + (n - 1) + 3(n - 1) + 1
- T(n) = 4n - 2
- **T(n) is O(n)**

## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Aryan Khurana
	* Arina Kolodeznikova
	* Nabeeha Siddiqui

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Aryan Khurana | 6.600000006073969e-06 | 2.930390794000459 |
| Arina Kolodeznikova | 5.500000042957254e-06 | 0.2319036220000612 |
| Nabeeha Siddiqui | 1.1200000017197453e-05 | 1.2416703189996952 |

### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 0.2319036220000612 | 2.930390794000459 | 2.698487172 |
|fibonacci | 5.500000042957254e-06 | 1.1200000017197453e-05 | 0.00000569999 |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

##### My (Aryan's) Code
###### Fibonacci
```python
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
```

- Utilizes two variables, prev and curr, to keep track of the Fibonacci sequence.
- Iterates using a for loop from 3 to n.
- Returns the final Fibonacci number.

###### Sum to Goal
```python
def sum_to_goal(nums, goal):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (nums[i] + nums[j] == goal):
                return nums[i] * nums[j]
    return 0
```

- Uses nested for loops to iterate over all pairs of numbers from the nums list.
- Checks if the sum of the pair is equal to the goal.
- Returns the product of the two numbers if found, otherwise returns 0.

##### Arina's Code
###### Fibonacci
```python
def fibonacci(num):
    n1, n2 = 0, 1
    if num < 0:
        print("Enter a positive value")
    elif num == 0:
        return 0
    elif num == 1:
        return n2
    else:
        for i in range(1, num):
            nth =n1 + n2
            n1, n2 = n2, nth
        return nth
```

- Utilizes two variables, n1 and n2, to keep track of the Fibonacci sequence.
- Iterates using a for loop from 1 to num - 1.
- Returns the final Fibonacci number.

###### Sum to Goal
```python
def sum_to_goal(num_list, goal):
    product = 0
    for i in range(len(num_list)):
        complimentary = goal - num_list[i]
        if complimentary in num_list[i + 1:]:
            product = complimentary * num_list[i]
    return product
```

- Uses a single for loop to iterate over the num_list and considers each number as the first number of the pair.
- Calculates the complementary value needed to reach the goal.
- Checks if the complementary value exists in the rest of the num_list.
- Returns the product of the pair if found, otherwise returns 0.

##### Nabeeha's Code
###### Fibonacci
```python
def fibonacci(n):
    arr = [0, 1]
    for elem in range(0, n):
        arr.append(arr[elem] + arr[elem+1])
    return arr[n]
```

- Uses a list, arr, to store the Fibonacci sequence.
- Iterates using a for loop from 0 to n - 1 and calculates the Fibonacci number by summing the last two elements of the list.
- Returns the final Fibonacci number.

###### Sum to Goal
```python
def sum_to_goal(arr, goal):
    _prod = 0
    for _ind in range(len(arr)):
        for _elem in range(_ind+1, len(arr)):
            if (arr[_ind] + arr[_elem] == goal):
                _prod = arr[_ind]*arr[_elem]
	return _prod
```

- Uses nested for loops to iterate over all pairs of numbers from the arr list.
- Checks if the sum of the pair is equal to the goal.
- Stores the product of the pair in _prod if found and return it.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
- **Fibonacci:**
	- The fastest code uses variables and does not use extra space like the slowest code does. In the case of Nabeeha's code, the use of an array and the subsequent appending of elements to the array can introduce additional overhead and potentially slow down the execution, even if the time complexity remains the same. Hence, even if the time complexity is the same, the choice of data structures and the approach to memory management can still have a noticeable impact on the actual performance of the code.

- **Sum to Goal:**
	- Aryan's code uses nested loops to check all possible pairs in num_list for the sum condition which makes it slower compared to Arina's code which is the fastest in this case. Arina's code uses a single loop to solve the problem which is in turn a faster and a better approach as far as the execution time is concerned.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  
- Aryan and Arina use a few variables to store intermediate results so the space complexity is similar in their algorithms. They have a constant space complexity O(1). Nabeeha's implementation has higher space complexity because it maintains a list to store the Fibonacci sequence. Her algorithm has a space complexity of O(n) where n is the size of the array.

3. What sort of conclusions can you draw based on your observations?
- All students have the same time complexity for the algorithms that they wrote. The only difference is minor details that impact the run time of the program. Also, the algorithmic approach, memory management in code and the handling of edge cases impact the time and space complexity of an algorithm. While time complexity provides a theoretical measure of algorithmic efficiency by considering the growth rate of an algorithm as the input size increases, it does not account for the constant factors and overhead that can affect the actual execution time.


