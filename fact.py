def recursive_factorial(num):
    if num==1:
        return 1
    else:
     return num * recursive_factorial(num-1)
n=int(input("Enter a number: "))
print("The factorial of ",n,"is" ,recursive_factorial(n))


