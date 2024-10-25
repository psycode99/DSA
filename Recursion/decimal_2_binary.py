def dec_2_bin(x):
    assert isinstance(x, int), " x must be  an integer"
    x = abs(x)
    if x == 0:
        return x
    else:
        return dec_2_bin(x // 2)  * 10 + (x % 2)
        # print(x % 2)

print(dec_2_bin(-13))