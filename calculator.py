'''
Author:Lesly Mathew
Date:19-10-2024
Description:AIM: Write a Python program that performs the following tasks:

    User Input:
        Ask the user to enter two numbers, num1 and num2.
        Ask the user to enter a third number, num3.

    Addition:
        Add the first two numbers (num1 and num2).
        Print the sum in the format: "The sum of num1 and num2 is: result"

    Subtraction:
        Subtract num2 from num1.
        Print the difference in the format: "The difference when num2 is subtracted from num1 is: result"

    Multiplication:
        Multiply num1 by num2.
        Print the product in the format: "The product of num1 and num2 is: result"

    Division:
        Divide num1 by num2.
        Print the quotient in the format: "The quotient when num1 is divided by num2 is: result"

    Modulus:
        Find the remainder when num1 is divided by num2.
        Print the remainder in the format: "The remainder when num1 is divided by num2 is: result"

    Combined Arithmetic Operation:
        Perform the following combined operation:
        result = (num1 + num2) * num3 / 2
        Print the result in the format: "The result of (num1 + num2) * num3 / 2 is: result"
        '''
number1=int(input("Enter a number: "))
number2=int(input("Enter a number: "))
number3=int(input("Enter a number: "))
print("The sum of number1 and number 2 is:",number1+number2)
print("The difference when number2 is subtracted from number1 is:",number2-number1)
print("The product of number1 and number2 is:",number1*number2)
print("The quotient when number1 is divided by  number2 is: ",number1/number2)
print("The remainder when number1 is divided by number2 is: ",number1%number2)
print("The result of (number1 + number2) * number3 / 2 is:",(number1+number2)*number3/2)