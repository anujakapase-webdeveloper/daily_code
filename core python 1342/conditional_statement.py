#1. Write a program to check whether a number is greater than 10
number=20
if(number>10):
    print(f"{number} is greater than 10")

#2. Write a program to check whether a person is eligible to vote (age must be 18 or above)    
age=20
if(age>=18):
    print("A person is eligible to vote")

#3. Write a program to check whether a number is divisible by 5    
number=10
if(number%5==0):
    print("number is divisible by 5")

#4. Write a program to check whether a student has scored at least 35 marks    
marks=40
if("marks>=35"):
    print(f"The student scored {marks} and has passed (at least 35 marks)")

#5. Write a program to check whether a character is an uppercase letter.
name="ANUJA"
if(name.isupper()):
    print("name is upper case")

#6. Write a program to check whether a number is even or odd.    
number=8
if(number%2==0):
    print(f"{number} is even")
else:
    (f"{number} is odd")  

#7. Write a program to check whether a number is positive or non-positive.
num=-23
if(num>0):
    print("number is positive")
else:
    print("number is negative")  

#8. Write a program to check voting eligibility using if-else.
'''age=int(input("enter your age:"))
if(age>=18 and age<100):
    print("your eligible for voting")
else:
    print("your not eligible for voting")   ''' 

#9. Write a program to check whether a number is divisible by both 3 and 5.
num=15
if(num%3==0 and num%5==0):
    print(f"{num} is divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")  

 #10. Write a program to check whether two numbers are equal or different.
num1=23
num2=23   
if(num1==num2):
    print(f"{num1} and {num2} are equal")
else:
    print(f"{num1} and {num2} are  defferent")

#11. Write a program to display Pass if marks are 35 or above; otherwise display Fail.
marks=76
if(marks>35 and marks<=100):
    print("your are pass")
else:
    print("yuor fail")  

#12. Write a program to check whether a year is a leap year.
year=2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.") 

    # if-elif-else statements
#13. Write a program to identify whether a number is positive, negative, or zero.
num=-1
if(num==0):
    print(" number is zero")
elif(num>0):
    print("number is positive")
else:
    print("number is negative")            

#14. Write a program to find the greatest of three numbers.
# Program to find the greatest of three numbers
num1 = 65
num2 = 34
num3 = 76
if num1 >= num2 and num1 >= num3:
  print(f"{num1} is the greatest number.")
elif num2 >= num1 and num2 >= num3:
  print(f"{num2} is the greatest number.")
else:
  print(f"{num3} is the greatest number.")

#15. Write a program to display a grade using these ranges: A = 90–100, B = 75–89, C = 60–74, Pass = 35–59,
#Fail = below 35. Also handle marks outside 0–100 as invalid
marks=78
if(marks>=90 and marks<=100):
    print("grade is A")
elif(marks>=75 and marks<=89):
    print("grade is B")
elif(marks>=60 and marks<=74):
    print("grade is c")
elif(marks>=35 and marks<=59):
    print("pass")
else:
    print("fail")

#16. Write a program to classify a character as an uppercase letter, lowercase letter, digit, or special character.
# Program to classify a character
'''char = input("Enter a character: ")

if len(char) == 1:
  if char.isupper():
    print(f"'{char}' is an uppercase letter.")
  elif char.islower():
    print(f"'{char}' is a lowercase letter.")
  elif char.isdigit():
    print(f"'{char}' is a digit.")
  else:
    print(f"'{char}' is a special character.")
else:
  print("Please enter exactly one character.")'''

#17. Write a program to display the weekday for a number from 1 to 7; display Invalid for any other number.
num=6
if(num>1 and num<7):
  if(num==1):
    print("it is a monday")
  elif(num==2):
         print("it is tuesday") 
  elif(num==3):
   print("it is a wednesday")
  elif(num==4):
   print("it is a tuesday")
  elif(num==5):
   print("it is a friday")
  elif(num==6):
   print("it is a saturday") 
  elif(num==7):
   print("it is a saturday")
else:
   print("invalid")
       
#18. Write a program to display the number of days in a month, assuming February has 28 days.

'''month = int(input("Month number enter karein (1 se 12): "))
if month == 2:
    print("28 days (February)")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
else:
    print("Invalid month number") '''

#19.Write a program to calculate a discount: 20% for a purchase of n5,000 or more, 10% for n2,000 or more,
#otherwise no discount. 

'''amount = float(input("Purchase amount enter karein: "))
if amount >= 5000:
    discount_percent = 20
elif amount >= 2000:
    discount_percent = 10
else:
    discount_percent = 0


discount_amount = amount * (discount_percent / 100)
final_price = amount - discount_amount


print(f"Discount: {discount_percent}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Payable Amount: {final_price}")  '''  

#nested if statement
#21
username = "anuja"
password= "puna123"
if(username=="anuja"):
  if(password=="puna123"):
      print("login succesfullye")

#22.
age=19
registered ="no"
if(age>=18):
   if(registered =="yes"):
      print("you are aligible to voting")

#23.
result="pass"
marks=80
if(result=="pass"):
   if(marks>=75):
      print("distinct")  

#24
num=-6
if(num>0):
   if(num%2==0):
      print("number is even") 
   else:
      print("number is odd") 
else:
   print("plaese enter positive number")    

#25.
age=26
salary=50000
if(age>=25):
   if(salary>40000):
      print("eligible for loan")
#26.
username="anuja0606"
password="puna@0606"
if(username=="anuja0606"):
   if(password=="puna@0606"):
      print("your account is activate")

#Logical operator
27.
number= 45
if(number>10 and number<50):
   print(f"{number} is between 10 and 50")   

#28.
num=21
if(num%3==0 or num%7==0):
   print(f"{num} is divisible by 3 and 7") 

#29.
age=35
qualification="bca"
if(age>=21 and age<=35 and qualification=="bca"):
   print("eligible for job")

#30.
char="o" 
if(char=="a" or char=="o"or char=="u"or char=="i"or char=="e"):
   print(f"{char} character is vowel")

#31.
num=203
if(num<100 or num>200):
   print(f"{num} is not between 100 and 200") 

#32
thoery="pass"
practical="fail"
if(thoery=="pass" and practical=="pass"):
   print("pass") 
else:
   print("fail") 

#33
order_amt=600
premium="no"
if(order_amt>=500 or premium=="yes"):
   print("free delivery")     

#Advance conditional practice
#34
a=45
b=65
c=87
d=100
if(a>b and a>c and a>d):
   print(f"{a}is greatest number")
elif(b>a and b>c and b>d):
   print(f"{b} is greatest number")
elif(c>a and c>b and c>d):
   print(f"{c} is greatest number")
else:
   print(f"{d}is greatest number")

#35
service=9
if(service>=10 and service<=20):
   print("15% bonus")
elif(service>=5 and service<=10):
   print("10% bonus")  
elif(service<5):
   print("5% bonus")
else:
   print("enter under 20 year experience")


  



   