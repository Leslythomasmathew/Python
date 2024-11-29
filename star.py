
#Increased Triangle
print("Increased triangle")
no_of_rows=int(input("Enter the number of rows: "))
for i in range(0,no_of_rows):
 for j in range(0,i):
    print("*",end="")
 print('*')


#Decreasing Triangle
print('Reversed triangle')
rows1=int(input("Enter the number of rows: "))
for k in range(rows1,0,-1):
  for l in range(k,0,-1):
   print("*", end="")
  print('')

#hill pattern
print("Hill pattern")
rows2=int(input("Enter the number of rows"))
for m in range(1,rows2+1):
    for n in range(rows2-m):
        print(" ",end=" ")
    for o in range(2*m-1):
        print("*",end=" ")
    print(" ")


#reverse hill pattern
print('Reversed Hill Pattern Triangle')
rows3=int(input("Enter the number of rows: "))
for m in range(rows3,0,-1):
   for n in range(rows3 - m, 0, -1):
     print(" ", end=" ")
   for o in range(2*m-1,0,-1):
     print("*", end=" ")
   print("")