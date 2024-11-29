def mobile_number_valid(number):
   if len(number)==10 and number[0] in "987":
      return True
   return False
phone_number=input("Enter the mobile number: ")
if mobile_number_valid(phone_number):
   print(f"The given number {phone_number} is valid")
else:
   print(f"The given number {phone_number}  is invalid")





