#!/usr/bin/env python3
"""



"""
counter = 0
total = 0
number = 0
while number >= 0:
    number = int(input ("Enter a positve number\n or negative number to exit"))
    total += number
    print(total) 
    counter += 1
    print(counter)
average = total / counter
print(average)