def recursive_mult(num1,num2):
    if num2==1:
        return num1
    if number1 and number2 < 0:
        print("not valid")
    else:
        return num1+recursive_mult(num1,num2-1)
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
print("The product of two numbers is ",recursive_mult(number1,number2))