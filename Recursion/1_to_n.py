def one_to_n(n):
    if n < 1:
        return n
    else:
        one_to_n(n-1)
        print(n) 

one_to_n(10)


def n_to_one(n):
    if n < 1:
        return n
    else:
        print(n)
        n_to_one(n - 1)

n_to_one(10)