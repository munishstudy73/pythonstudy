#/usr/bin/env python3
"""
Author:
Date:
Program: Calculate curtain price
"""
__version__ = 0.1
roll_width = 140
price_per_metre = 5
print()
print('\twidth\theight\twidths\ttotal\tprice')

#prompt user for window ht and wt
window_height = input("Enter the height of the window (cm)")
window_width = input("Enter the width of the window (cm)")

# hems in consideration
curtain_width = float(window_height) * 0.75 + 20
print('\t', curtain_width)
curtain_length = float(window_height) + 15
print('\t\t', curtain_length)

width = curtain_width / roll_width
print('\t\t\t', width)
total_length = curtain_length * width
print('\t\t\t\t', total_length)
total_length = (total_length * 2) / 100
print('\t\t\t\t', round(total_length,2))
#total price
price = total_length * price_per_metre

print('\t\t\t\t\t', round(price,2))
print( "You need ", round(total_length,2), " meters of cloth for ", round(price,2))