#/usr/bin/env python3
"""
Author:
Date:
Program: Calculate curtain price
"""
__version__ = 0.1
roll_width = 140
price_per_metre = 5

#prompt user for window ht and wt
window_height = input("Enter the height of the window (cm)")
window_width = input("Enter the width of the window (cm)")

# hems in consideration
curtain_width = float(window_height) * 0.75 + 20
curtain_height = float(window_height) + 15

width = curtain_width / roll_width
total_length = curtain_height * width

total_length = (total_length * 2) / 10
#total price
price = total_length * price_per_metre
print( "You need ", total_length, " meters of cloth for ", price)
print(curtain_height,curtain_width,total_length,price)
