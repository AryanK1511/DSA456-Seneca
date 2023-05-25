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
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

```

#### Function 3 Analysis
- Let n represent the length of the list that is being passed as the parameter for function3.
- Let T(n) represent the number of operations needed to complete the function
- T(n) = 

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
	* ex. Samuel Vimes
	* ...

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Samuel Vimes |  0.123 | 0.456 |
| group member 2 | 0.0 | 0.0 |
| group member 3 | 0.0 | 0.0 |
| group member 4 | 0.0 | 0.0 |
| group member 5 | 0.0 | 0.0 |
| group member 6 | 0.0 | 0.0 |

### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number |  |  |  |
|fibonacci |  |  |  |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.


## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  
3. What sort of conclusions can you draw based on your observations?



