# Write a program that returns a list that contains 
# only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# ---------------
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c= []

#for num in a:
#    if num == num in b:
#        if num not in c:
#            c.append(num)

#print(c)

# ---------------

import random
a = random.sample(range(1,50), 10)
b = random.sample(range(1,50), 8)
c = []

for num in a:
    if num == num in b:
        if num not in c:
            c.append(num)

print(c)
