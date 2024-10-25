'''
Author: LESLY MATHEW
Date: 25-10-2024
Description: Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.

Sample Input:

Enter first number: 45
Enter second number: 12
Enter third number: 78

Sample Output:

The largest number is: 78
'''



number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))
number_3=int(input("Enter third number:"))
if number_1>number_2 and number_1>number_3:
    print("The largest number is",number_1 )
elif  number_2>number_1 and number_2>number_3:
    print("The largest number is",number_2)
else:
   print("The largest number is",number_3)