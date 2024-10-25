def maxNum(cards: list):
    curr_max = 0
    for num in  cards:
        if num > curr_max:
            curr_max = num
        else:
            pass
    return curr_max

ll = [2000000,6,8,99,100, 1000, 89000]
print(maxNum(ll))