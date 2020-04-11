# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# Objectives:
# While loops
# infinite loops
# break statements

import random

play = True

while play:
    user_choice = input('Choose one: rock, paper or scissors?')
    choices = ['rock', 'paper', 'scissors']
    random_choice = random.choice(choices)
    
    if random_choice == user_choice:
        print('Computer chose: {}. Tie!'.format(random_choice))
    elif random_choice == 'rock' and user_choice == 'scissors':
        print('Computer chose: {}. You loose...'.format(random_choice))
    elif random_choice == 'scissors' and user_choice == 'paper':
        print('Computer chose: {}. You loose...'.format(random_choice))
    elif random_choice == 'paper' and user_choice == 'rock':
        print('Computer chose: {}. You loose...'.format(random_choice))
    else:
        print('Computer chose: {}. You win!'.format(random_choice))
    
    restart = input('Play again? y/n')
    if restart == 'n':
        play = False

    



