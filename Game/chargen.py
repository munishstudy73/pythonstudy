#!/usr/bin/env python3
"""
chargen.py
Author:
Date:
Program:- User give input for character

"""
__version__ = 0.1
Name = ""
Desc = ""
Gender = ""
Race = ""

#prompt user for information
Name = input("what is your name?")
Desc = input("Describe yourself:")
Gender = input("What gender are you? (male / female / unsure):")
Race = input ("what race are you? (Pixie / Vulcan / Gelfling / Troll) :"

# output of character sheet
fancy_line = "##################################"

print("\n",fancy_line)
print("\t", Name)
print("\t", Race, Gender)
print("\t", Desc)
print(fancy_line, "\n")

#END