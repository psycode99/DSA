def recursiveCall(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveCall(n - 1)
        print(n)


recursiveCall(5)