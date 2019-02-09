# Tutorial 1
# EVERYTHING is an object (that include function,...)
# Var(s) are immutable


# print() func
print("Hello\n")

# Use """ """ for printing  multi lines
print("""This is a multi
lines text\n""")

# Multi lines w/o """ """
print("This should\n"
      "display in multi lines\n")

# Commment
# Is this a comment?
#
# input('Enter something here: ')

# Var
name = "Super Programmer"
age = 100

# Cannot CONCAT String and NUM together
print("I am " + name + " and I am " + str(age) + " years old")

print(age)

print("LOOK! I am turning my age from int to float: " + str(age) + " -> " + str(float(age)))

# "printf" in python
# Method 1 {instance:(flag)(width).(accurate)
print("Name: {n}, Age: {a}\n".format(n=name, a=age))

# Method 2 %(flag)(width).(accurate)(type)
print("Name: %s, Age: %d\n" % (name, age))

# len()
print('Length of my name %d' % len(name))

# String can be treated as char[]
# x[index]
# x[fromIndex:stopAtIndex] **not include element at the stop
# x[index:] or x[:index] **from i to the end or from the beginning to i
# x[-index] **start from the end

# Lists
# Can have dif type
# Lists are mutable
# Same subset operations as Strings
# x[i] = value -> reassign
# x.append(o) add to the end of the lists
# have push() and pop()

# Dictionaries
# Set of key-val pairs
# EG: d = {1:'hello', 'two':42, 'blah':[123]}

# If statement
# if expression:
#   statements
if 20 < 5:
    print("This should not be printed")
    print("This should not be reachable")
print('Some text')

