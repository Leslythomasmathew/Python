def gcd(num1,num2):
    if num1%num2==0:
        return num2

    else:
        return gcd(num2,num1%num2)

n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))
print("The GCD of the given numbers is ", gcd(n1, n2))


