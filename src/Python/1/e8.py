import random

print('Rock Paper Scissor game')
print('r    : rock')
print('p    : paper')
print('s    : scissor')
print('stop : stop the game')

rule = {'r': {'s': 'win', 'p': 'lose', 'r': 'draw'},
        's': {'p': 'win', 'r': 'lose', 's': 'draw'},
        'p': {'r': 'win', 's': 'lose', 'p': 'draw'}}

moves = {'r': 'rock', 'p': 'paper', 's': 'scissor'}

while True:
    bot = random.choice(['r', 'p', 's'])
    print('Bot has chosen its move')
    player = input('Your move: ')
    if player == 'stop':
        print('Stop the game')
        break
    print('Bot move: ' + moves[bot])

    try:
        print('Player move: ' + moves[player])
        print(rule[player][bot])
    except KeyError:
        print('Invalid move')
        print('Restart the game')
        continue
