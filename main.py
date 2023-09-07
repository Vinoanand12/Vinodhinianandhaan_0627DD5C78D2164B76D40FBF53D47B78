def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


value = 5
res = fact_rec(value)

print("The factorial of", value, "is", res)