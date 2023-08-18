'''
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.
'''

number = input("Enter any valid number: ")

if (int(number)%2 == 0):
    result = "even"
else:
    result = "odd"

print("The number {} is {}".format(number, result))