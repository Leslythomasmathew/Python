def recursive_add(num1,num2):

    if num2==0:
        return num1
    if (number1 and number2) < 0:
        print("not valid")
    else:
        return recursive_add(num1+1,num2-1)
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
print("The sum of numbers is",recursive_add(number1,number2))