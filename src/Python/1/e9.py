import random

print('Guessing value of generated number (1-9)')
print('Type \'exit\' to stop the game')
try:
    while True:
        num = random.randint(1, 10)
        print('Generated number')
        guess = 0;
        while True:
            player = int(input('Your guess: '))
            guess += 1
            if int(player) == num:
                print('Correct')
                print('You guessed %d time(s)' % guess)
                print('Restart the game')
                break
            else:
                print('Wrong')
                print('Try again')

except ValueError:
    print('Exit game')
