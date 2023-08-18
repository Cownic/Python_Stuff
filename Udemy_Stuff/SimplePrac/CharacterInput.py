'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

age = input("Enter your age as of this year: ")
print("You will turn 100 years old in the year {}.".format(2023+(100- int(age))))