print('Check number ODD or EVEN')
num = int(input('Number: '))

if num % 4 == 0:
    print('%d can be divided by 4' % num)
elif num % 2 == 0:
    print('%d is an EVEN number' % num)
else:
    print('%d is an ODD number' % num)
