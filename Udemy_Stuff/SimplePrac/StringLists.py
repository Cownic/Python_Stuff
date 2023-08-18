'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

user_string = input("Enter a word: ")

reversed_string = user_string[::-1]

print(reversed_string)

if user_string == reversed_string:
    print("True")
else:
    print("False")