print('List of divisors of a number')

num = int(input('Number: '))

listOfNum = range(2, num + 1)
listOfDivisor = list(filter(lambda n: num % n == 0, listOfNum))

for n in listOfDivisor:
    print(n)
