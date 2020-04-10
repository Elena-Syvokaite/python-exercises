value1 = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
value2 = ['d', 'g']
value3 = ['b', 'c', 'm', 'p' ]
value4 = ['f', 'h', 'v', 'w', 'y']
value5 = ['k']
value8 = ['j', 'x']
value10 = ['q', 'z']

user_word = input('What is your scrabble word?')

user_score = []

for letter in user_word:
    if letter in value1:
        user_score.append(1)
    elif letter in value2:
        user_score.append(2)
    elif letter in value3:
        user_score.append(3)
    elif letter in value4:
        user_score.append(4)
    elif letter in value5:
        user_score.append(5)
    elif letter in value8:
        user_score.append(8)
    elif letter in value10:
        user_score.append(10)
        
score = sum(user_score)
print('This word scores: ' + str(score))