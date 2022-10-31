def count_recursion(k):
  if(k>0):
    result = count_recursion(k-1)+1
    print(result)
  else:
    result = 0
  return result

print("Example of Recursion Count")
count_recursion(6)
