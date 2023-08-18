'''
write a program that prints out all the elements of the list that are less than 5.
'''

import random

lst = []

for i in range(20):
    lst.append(random.randint(0,100))

print(lst)

for i in lst:
    if i < 5:
        print(i)
    else:
        continue
