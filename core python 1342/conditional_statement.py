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

# Take character input from the user
char = input("Enter a character: ")

# Check if the input is a single character
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
  print("Please enter exactly one character.")
       
            