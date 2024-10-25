def gcd(x, y):
    x = abs(x)
    y = abs(y)
    assert isinstance(x, int) and isinstance(y, int), "x and y  must be integers"
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(gcd(10, 4))