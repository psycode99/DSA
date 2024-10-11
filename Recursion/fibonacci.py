def fibonacci(n):
    assert n >= 0 and isinstance(n, int), "n must be a valid integer"
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for x in range(4):
    fib = fibonacci(x)
    print(fib)