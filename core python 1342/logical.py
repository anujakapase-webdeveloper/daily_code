

#comparison operator
#Take two numbers from the user and check whether they are equal.
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

print(num1==num2)

#Take two numbers and check which comparison results are True.
a=23
b=23
print(a==b)

#Take a person's age and check whether the age is greater than 18.
age=24
if(age>18):
    print("age is greater than 18")
else:
    print("age is less than 18")    

#Take two numbers and check whether the first number is greater than or equal to the second.
number=99
Number=58
print(number>=Number)

 #Take two numbers and check whether they are different.
num_1=74
num_2=34
print(num_1!=num_2)   

#Take a student's marks and check whether marks are greater than or equal to 40.
stu_marks=45
if(stu_marks>=40):
    print("student is pass")
else:
    print("student is fail")

#Take two numbers and display the result of all six comparison operators.
first_num=67
second_num=45
print(first_num==second_num)
print(first_num!=second_num)
print(first_num>=second_num)
print(first_num<=second_num)
print(first_num<second_num)
print(first_num>second_num)




#Logical operators

a=10
b=20
print(a<b and b>30)
print(a>b or a<b)
print(not(a>b))

age=25
print(age>=18 and age<=60)

marks=35
print(marks>=40 or marks==35)

#Take age and salary from the user and check:age >= 18 AND salary >= 20000
ages=int(input("enter your age:"))
salary=int(input("enter your salary:"))
print(age>=18 and salary>=20000)

#Take two numbers from the user and check whether:first number is greater than 10 OR second number is greater than 10 
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
print(first>10 and second>10)

print(not(True) and 31>=34 or not(32>21 and (True))and not(True or 56!=0))
print(not(0==0)and 34>=34 or not(32>=21 and not(False)) and not(False or 0!=0))
print("ram"=="Ram")and (0>0) and 34!=34 or not(32>=21) and not(True) and not(True or 56!=0)
