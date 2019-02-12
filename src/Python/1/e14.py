# Password generator
# **Online Solution**

import string
import random


def pw_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    """
    :arg1 size = 8
    :arg2 chars = letters + digits + punctuations
    :return password
    """
    return ''.join(random.choice(chars) for _ in range(size))


print(pw_gen(int(input('How many characters in your password?'))))
