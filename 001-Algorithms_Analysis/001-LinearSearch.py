def linear_search(my_list, key):
    for i in range(0, len(my_list)): # n + 1 + 1
        if my_list[i] == key: # n 
            return i 
    return -1 #1 -> Worst Case

print(linear_search([32, 454, 7, 21, 754, 1234], 454)) # Output: 1
print(linear_search([32, 454, 7, 21, 754, 1234], 1)) # Output: -1