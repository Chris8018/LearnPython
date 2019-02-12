# Password generator
# **Online Solution**

import string
import random


def gen_random_string(size=5, chars=string.ascii_letters + string.digits):
    """
    @:arg1 size = 5
    @:arg2 chars = letters + digits
    @:return a string
    """
    return ''.join(random.choice(chars) for _ in range(size))


def histogram_from_list(the_list):
    temp_set = set(the_list)
    for x in temp_set:
        print('{0} {1}'.format(x, '*'*the_list.count(x)))


list_string = [gen_random_string() for _ in range(5)]

my_list = [list_string[random.randint(0, len(list_string) - 1)] for _ in range(10)]
histogram_from_list(my_list)
