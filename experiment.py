# This is a program you can run that will test
# a bot of your choice against another.
#
# Feel free to change the given variables.
#
# The program takes half a minute to run with 50 trials.
import os


# The bot we want to experiment with.
OUR_BOT = 'SkrrtBot.py'

# The bot we want to run against.
ENEMY_BOT = 'reconchess.bots.random_bot'

# The number of trials we want to experiment over.
TRIALS = 50

total = 0
wins = 0
command = 'rc-bot-match ' + OUR_BOT + ' ' + ENEMY_BOT

i = 0
while i < TRIALS:
    output = os.popen(command).read()
    winner = output[19:24]
    if winner == 'white':
        wins += 1

    total += 1
    i += 1

print('Wins: ', wins, "/", total)