# Create a program that asks the user for a number and 
# then prints out a list of all the divisors of that number.

user_num = int(input('Type in a number: '))

x = list(range(1, user_num+1)) 
divisorList = []
for num in x:
    if user_num % num == 0:
        divisorList.append(num)
        print(divisorList)