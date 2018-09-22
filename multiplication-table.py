"""
multiplication-table.py
Author: Nick Lee
Credit: A little syntax adjustment from stack overflow
Assignment: Multiplication table

Write and submit a Python program that prints a multiplication table. The user 
must be prompted to give the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
width = int(input("Width of multiplication table: "))
height = int(input("Height of multiplication table: "))

multi = 1

for i in range(height): # repeats for number of rows
    row1 = "" # first number in the row
    num1 = 0 # resets starting number
    for i in range(width): # generates the rows
        num1 += multi # adds the mutiplier to the next number in the row
        num2 = ("{0:>4}".format(num1)) # formats the next number in the row
        row1 = ("{0}{1}".format(row1, num2)) # adds the next number to the row
    print(row1) # prints each horizontal row
    multi += 1 # increases the multiplier

# sorry for agressive commenting


