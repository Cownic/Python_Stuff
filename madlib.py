# Learning how to use f' to do string concentenation in python
from sample_madlibs import zombie
name = input("Please enter your name: ")

print(f"Hello, Welcome to Madlib, {name}")

exclaimation=input("Please enter an exclaimation below: ")
adverb=input("Please enter a adverb: ")
noun=input("Please enter a noun below: ")
adjective=input("Please enter a adjective below: ")

zombie.note(exclaimation,adverb,noun,adjective)
