def binary_search(n, lst):
    lhs = 0
    rhs = len(lst) - 1
    while lhs < len(lst) - 1 and rhs > 0:
        mid = int((lhs + rhs) / 2)
        if n == lst[mid]:
            break
        elif n > lst[mid]:
            lhs = mid + 1
        else:
            rhs = mid - 1

    if lhs >= len(lst) - 1 or rhs <= 0:
        return "The number is not in the list"
    else:
        return mid


a = [1, 3, 5, 30, 42, 43, 500]
b = 50

print(binary_search(b, a))
print(a.index(b))
