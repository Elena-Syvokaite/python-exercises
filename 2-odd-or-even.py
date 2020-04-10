# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2? 

# Objectives:
# - Modular arithmetic (the modulus operator)
# (For example, when I divide 5 by 3, the remainder is 2, 
#  and the sentence reads like this: “5 modulo 3 is 2",
# "7 modulo 3 is 1", "6 modulo 3 is 0".

# - Conditionals (if statements)

# - Checking equality
# == (equals to), != (not equal to)

num = int(input('Type in a number: '))
if num % 2 == 0:
    print('Even number')
else:
    print('Odd number')