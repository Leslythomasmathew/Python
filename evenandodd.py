list_1=[1,2,3,4]
list_2=[6,7,8]
list_3=list_1+list_2
list_4=[]
list_5=[]
print("The values of list 1 is",list_1)
print("The values of liSt 2 is",list_2)
print(f"The values of the list before sorting {list_3}")
for number in list_3:
  if number%2== 0:
         list_4.append(number)


  else:
       list_5.append(number)
print(f"The values of the list after sorting{list_4+list_5}")


