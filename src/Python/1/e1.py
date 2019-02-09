from datetime import datetime

today = datetime.now();

name = input('Name: ')
age = int(input('Age: '))

temp = int(today.year) + (100 - age)

print('%s will turn 100 years old in %d' % (name, temp))