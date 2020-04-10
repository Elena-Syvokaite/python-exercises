# Ask the user for a string and 
# print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

user_string = input('Type in any word: ')

x = []

for letter in user_string:
     x.append(letter)

y = []

for letter in reversed(user_string):
    y.append(letter)

if x == y:
    print('Palindrome!')
else:
    print('Not a palindrome.')