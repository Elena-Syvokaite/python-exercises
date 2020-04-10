# Write a program that prints out all 
# the elements of the list that are less than 5.

# Objectives:
# - Lists
# - More conditionals

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for num in a:
#    if num <= 5:
#        print(num)
#    else:
#        break

print([num for num in a if num <= 5])