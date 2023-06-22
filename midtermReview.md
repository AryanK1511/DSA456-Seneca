## Q1:

What is the run time of the following function:

```python
def f1(number):
    rc = 1                  # 1
    for i in range(0, 5):   # 5 + 1
        rc += 1             # 1 + 1
    return rc               # 1
```
- Let n be the number that is passed as the parameter
- Let T(n) be the total number of operations involved in the completion of the functions
- T(n) = 1 + 5 + 1 + 1 + 1 + 1
- T(n) = 10
- Therefore, **Time Complexity = O(1)**

## Q2:

What is the run time of the following function:

```python
def f1(n):
    rc = 1          # 1
    i = 0           # 1
    while i < n:    # n / 2
        rc += 1     # 2(n / 2)
        i += 2      # 2 (n / 2)
    return rc       # 1
```
- Let n be the number passed as the parameter of funtion f1
- Let T(n) be the number of operations involved in the completion of the functions
- T(n) = 1 + 1 + (n / 2) + n + n + 1
- T(n) = 3 + 2n + (n / 2)
- T(n) = (6 + 4n + n ) / 2
- T(n) = (5n + 6) / 2
- Therefore, **Time COmplexity = O(n)**

## Q3:

Suppose that the function g1(n) has a run time of O(n) and g2(n) has a run time of O(n^2)  What is the run time of f1(n)?

```python
def f1(n):
    g1(n)
    g2(n)
```
- Final Run Time of f1 = O(n) + O(n^2)
- Therefore, **Time Complexity = O(n^2)**

## Q4:

Write the following function recursively:

```python
def is_palindrome(word)
```
word is a character string.  This function returns true if word is a palindrome.  A palindrome is a string that reads the same forwards and backwards.  Thus:   noon, mom, dad are all palindromes.   table, texture, glass are not palindromes.

the above function can be a wrapper to a function that actually does the work

Try to write the function to O(n) run time where n is the length of s.

``` python
def palindrome(word):
    rev = palindromeString(word)
    return word == rev

def palindromeString(s):
    if len(s) <= 1:
        return s
    return palindromeString(s[1:]) + s[0]
```

## Q5:

When using a singly linked list to implement a stack, is it better for insertions to occur at the front or back of the list (or does it matter)?  Why?
**A)** It is better to insert elements at the **front** when trying to implement a stack using a singly linked list. This is because of the following reasons:
1. The stack is a LIFO (Last in first out structure). Imagine a stack of plates. You always add a new plate to the front/top of the stack and you always remove it from the top of the stack as well.
2. The time complexity when inserting at the front is **O(1)**. If you try to insert at the back using a singly linked list, you would have to iterate through the entire linked list to get to the end of the list and the time complexity would increase to be **O(n)**.

## Q6:

Describe what you will need to implement a queue using an array such that you have O(1) runtimes for enqueue() and dequeue() operations.  Do this WITHOUT using code (ie what do you need, why do you need it, but don't just code dump)

## Q7:

A self adjusting linked list is a linked list where a successful search causes the list to adjust so that the found item is moved to the front (and thus allowing successive search for same item to be more readily found).
 
Given the following class declarations for a doubly linked self adjusting linked list:
 
```python
class SelfAdjustingList:
	class Node:
		def __init__(self, dat, nx, pr):
			self.data = dat
			self.next = nx
			self.prev = pr

	def __init__(self, id_list):
                self.front = ...
                self.back = ...
```

Write the following function:
```python 
def search(self, v)
```

* This function searches for v within the list and returns true if v is found.  If not found, function returns false
* The list will be adjusted so that the found node is moved so that it becomes the first data node in the list
* Function must have run time of O(n)
* Implement two versions of this, one using sentinels and one without.

## Q8: Recursive Analysis:

Perform an analysis on do_something() function with respect to the length of the string str
```python
def do_recursion(str, curr):
    if curr == len(str):
        return 0
    elif str[curr] == "a":
        return 1 + do_recursion(str, curr + 1)
    else:
        return do_recursion(str, curr + 1)

def do_something(str):
    return do_recursion(str, 0)
```
