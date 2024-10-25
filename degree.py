'''
Author:Lesly Mathew
Date:25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:

'''

temperature=int(input("Enter temperature:"))
degree=input("Is this in (C)elsius or (F)ahrenheit? ")
if degree=="C":
    new_temperature_1=(9/5*temperature)+32
    print(temperature,"Celsius is",new_temperature_1,"Fahrenheit")
else:
    new_temperature_2=5/9*(temperature-32)
    print(temperature,"Fahrenheit is",new_temperature_2,"Celsius")






