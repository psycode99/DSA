def sum_of_digits(n):
    assert n >= 0  and isinstance(n, int), "n must be a valid positive integer"
    if n in (0,):
        return n 
    else:
        return n % 10 + sum_of_digits(n // 10)
  

def iterative_sum_of_digits(n):
    assert n >= 0 and isinstance(n, int), "n must be a valid positive integer"
    to_str = str(n)
    str_len = len(to_str) 
    sum = 0
    for x in range(str_len):
        sum += int(to_str[x])
    return sum


test_numbers = [5, 13, 246, 9876, 12345, 1001, 999, 50432, 10000, 123456789, 1.5, -90]

for num in test_numbers:
    recursive = sum_of_digits(num)
    print(recursive)
    
    iterative = iterative_sum_of_digits(num)
    print(iterative)



