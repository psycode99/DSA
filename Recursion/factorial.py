def factorial(n):
    assert n >= 0 and isinstance(n, int), "The input must be a valid integer"
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)
        

print(factorial(100))

