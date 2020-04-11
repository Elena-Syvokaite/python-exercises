play = True

while play:
    Player1 = input('Player 1, choose one: rock, paper or scissors?')
    Player2 = input('Player 2, choose one: rock, paper or scissors?')
        
    if Player1 == Player2:
        print('Tie!')
    elif Player1 == 'rock' and Player2 == 'scissors':
        print('Player 1 wins!')
    elif Player1 == 'scissors' and Player2 == 'paper':
        print('Player 1 wins!')
    elif Player1 == 'paper' and Player2 == 'rock':
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')
    
    restart = input('Play again? y/n')
    if restart == 'n':
        play = False