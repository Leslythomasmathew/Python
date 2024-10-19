'''
Author:Lesly Mathew
Date:19-10-24
Description:Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
        Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''

firstname=input("Enter your first name: ")
lastname=input("Enter your last name: ")
name=firstname+" "+lastname
print(name)
lentgh=len(firstname)
str_name=name[:lentgh]
print(str_name)