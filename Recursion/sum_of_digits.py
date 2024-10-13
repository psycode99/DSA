def sum_of_digits(n):
    assert n >= 0  and isinstance(n, int), "n must be a valid integer"
    if n in (0, 1):
        return n 
    else:
        return n % 10 + sum_of_digits(n // 10)
    
print(sum_of_digits(50))