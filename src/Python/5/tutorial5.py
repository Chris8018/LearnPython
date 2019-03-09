# 1.
# Write a function to return the length of an integer.E.g.
# >> > get_len_int(123456789071524124750)
# 21
# >> > get_len_int(100)
# 3
# >> > get_len_int(-100)
# 4
# >> > get_len_int(‘ci’)
# TypeError: provide only integer input


def get_len_int(a):
    if not a.isnumeric():
        raise TypeError('provide only integer input')
    return len(str(a))


# 2.
# Returns True / False - two strings are anagrams(assume input consists of alphabets only)
# >> > str_anagram('cat', 'Tac')
# True
# >> > str_anagram('beat', 'table')
# False
# >> > str_anagram('Tap', 'paT')
# True
# >> > str_anagram('beat', 'abet')
# True


def str_anagram(s1, s2):
    for c in s1:
        s2 = s2.replace(c, '', 1);
    return len(s2) == 0


# 3.
# Write a function that returns
# 'Good' for numbers divisible by 7
# 'Mood' for numbers divisible by 6
# 'Universe' for numbers divisible by 42
# 'Oops' for all other numbers


def aFunc(n):
    if n % 42 == 0:
        return 'Universe'
    if n % 7 == 0:
        return 'Good'
    if n % 6 == 0:
        return 'Mood'
    return 'Oops'


# 4.
# Write a function that returns product of all numbers of a list
# >> > product([5, 25])
# 125
# >> > product([-4, 2.3e12, 77.23, 982, 0b101])
# -3.48863356e+18
#
# bonus: works on any kind of iterable


def add(a, b):
    return a + b


def product(num_list):
    result = 1
    for n in num_list:
        result *= n
    return result
