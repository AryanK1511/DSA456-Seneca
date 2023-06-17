def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while call_stack:
    return_value = call_stack[-1]
    call_stack.pop(-1)
    print(call_stack)
    print("You're adding", return_value["n_value"], "to", result)
    result += return_value["n_value"]
  print(result)
  return result, call_stack

sum_to_one(4)