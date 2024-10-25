def binary_search(cards, query):
    l_pointer = 0
    r_pointer = len(cards) - 1

    while l_pointer <= r_pointer:
        mid = (l_pointer + r_pointer) // 2
        choice = cards[mid]

        if choice == query:
            print("card found")
            return choice
        elif choice > query:
            r_pointer = mid - 1
        else:
            l_pointer = mid + 1
    print("card not found")
    return None

test_data = [10, 20, 40, 45, 56, 67, 78, 99]
call = binary_search(test_data, 99)
print(call)