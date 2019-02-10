#import random
import math

print('Check if a number is a prime number')

num = int(input('Number to check: '))

listOfNum = [2] + list(range(3, int(math.sqrt(num)) + 1, 2))

temp = list(filter(lambda x: x != 0, map(lambda x: num % x, listOfNum)))
print('Is prime number ' + str(len(listOfNum) == len(temp)))
