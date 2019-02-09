print('Filter number less than 10\n')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

temp = list(filter(lambda x: x < 10, a))

for n in temp:
    print('%d' % n)