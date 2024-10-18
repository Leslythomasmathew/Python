'''
Author:Lesly Mathew
Date:18-10-2024
Description: Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.

Expected Output:

Enter a number: 5

Square root of 5: 2.23606797749979

Factorial of 5: 120

5 raised to power 2: 25.0
'''



import math
from math import factorial

number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("square root of",number,":",square_root)
factorial=math.factorial(number)
print("factorial of",number,":",factorial )
power=math.pow(number,2)
print(number,"raised to power 2:",power)
