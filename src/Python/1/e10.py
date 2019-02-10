#import random
import math

print('Check if a number is a prime number')


def is_prime(n, i=3):
    if n % 2 == 0 or n % i == 0:
        return False
    elif i*i < n:
        return is_prime(n, i + 2)
    else:
        return True


num = int(input('Number to check: '))

print(str(num) + ' is prime number: ' + str(is_prime(num)))

# Method 1
# listOfNum = [2] + list(range(3, int(math.sqrt(num)) + 1, 2))
#
# temp = list(filter(lambda x: x != 0, map(lambda x: num % x, listOfNum)))
# print('Is prime number ' + str(len(listOfNum) == len(temp)))

# Method 2

