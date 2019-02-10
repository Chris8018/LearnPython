# Generate a list of Fibonacci number

print('Generate x number of Fibonacci number')


def gen_fibonacci(l, num):
    if len(l) == num:
        return l
    if len(l) < 2:
        return gen_fibonacci(l + [1], num)
    else:
        return gen_fibonacci(l + [l[len(l)-1] + l[len(l)-2]], num)


x = int(input('x: '))

fibonacci_nums = gen_fibonacci([], x)

print(fibonacci_nums)
