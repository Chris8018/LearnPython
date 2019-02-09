print('Check if a number can be divided by another number')

check = int(input('Number to check: '))
divideBy = int(input('Divide by: '))

if check % divideBy == 0:
    print('%d can be divided by %d' % (check, divideBy))
else:
    print('%d cannot be divided by %d' % (check, divideBy))