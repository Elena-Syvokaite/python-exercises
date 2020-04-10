# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old.

# Objectives:
# - Getting user input
# - Manipulating strings (a few ways)

name = input('What is your name? ')
age = int(input('And what is your age? '))
age_calculation = (100 - age) + 2020 
print('You, ' + name + ',' + ' will turn 100 years old in ' + str(age_calculation) + '.')