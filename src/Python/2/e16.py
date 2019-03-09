# Cow and bull game
# = Exist and Match game
# Gen 4 digit non duplicate digit num
# Guess the number
# Tell player how many Match and exist

import random


def no_repeated_digits(num):
    """
    1st digit is not 0
    4 digits
    non duplicate digit

    :arg num
    :return: boolean
    """
    try:
        return True if num.isdigit() and num[0] != '0' and len(num) == 4 and len(set(num)) == 4 else False
    except:
        print('no_repeated_digits error')
        raise


def gen_no_repeated_digit_rnd():
    """
    :return: a 4-non-repeated-digit number
    """
    num_list = list(map(lambda x: str(x), random.sample(range(10), 4)))
    if num_list[0] == '0':
        num_list.append(num_list.pop(0))
    return "".join(num_list)


def count_exist_match(r, g):
    """
    :param r: result
    :param g: guess
    :return: (exist, match)
    """
    try:
        exist = 0
        match = 0
        for i in range(len(r)):
            exist += g.count(r[i])
            if i == g.find(r[i]):
                match += 1

        return [exist, match]
    except:
        print('count_exist_match error')
        raise


print('Cow and Bull game')
print('Type "exit" to stop the game')

guess_num = ''

while guess_num != 'exit':
    result = gen_no_repeated_digit_rnd()
    print('Generated rnd 4-non-repeated-digit number')
    # print(result)

    guess_count = 0

    while True:
        guess_num = input('Your guess (4-non-repeated-digit number): ')

        while not no_repeated_digits(guess_num) and guess_num != 'exit':
            guess_num = input('Invalid input! Try again: ')
        else:
            guess_count += 1

        if guess_num == 'exit':
            break

        if result != guess_num:
            check = count_exist_match(result, guess_num)
            print('Exist: {0}; Match: {1}'.format(check[0], check[1]))
        else:
            print('Correct!')
            print('Number of guess: %d' % guess_count)
            print('Restart the game')
            break
else:
    print('Stop the game')
