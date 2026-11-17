# 1. Integer 
age = 25

# 2. Floating-point number 
price=24.30

# 3. String 
name="anuja"

# 4. Boolean 
is_active = True

# 5. List 
subject=["pyhton","datastructure","java"]

# 6. Tuple 
student=("john","alice","bob")

# 7. Dictionary 
employees = {"id": 101, "name": "Alice","skill":"python"}

# 8. Set 
unique_tags = {"python", "coding", "beginner"}

# 9. Complex Number 
complex_num = 3 + 5j

# 10. NoneType 
middle_name = None

# Printing their types
variables = [
    age,
    price,
    name,
    is_active,
    subject,
    student,
    employees,
    unique_tags,
    complex_num,
    middle_name,
]

for var in variables:
    print(f"values:{var} {type(var)}")

    
#2.Initial assignment
student_data="Anuja"
print(f"{student_data} {type(student_data)}")

#reassignning value
student_data=45
print(f"{student_data} {type(student_data)}")

#3.Create variables to store employee ID, name, salary, department, and employment status.
employees_id=101
name="john"
salary=50000
department="data science"
employees_status=True
print(f"id={employees_id} {type(employees_id)}")
print(f"name{name} {type(name)}")
print(f"salary={salary}{type(salary)}")
print(f"department={department}{type(department)}")
print(f"employeees_status={employees_status}{type(employees_status)}")

#4.Accept the length and width of a rectangle and calculate its area. Identify the data types used.
length=45.56
width=39
area=length*width
print(f"area of the rectangular is={area}|{type(area)}")

#5.Write a program to swap two variables without using a third variable.
a=10
b=40
print(f"original value of a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"swapping value of a={a} and b={b}")

#6.Predict the output:
a = 10
b = 20.5
c = "30"

print(type(a + b))#float
print(type(str(a)))#str
print(type(float(c)))#float

#7.Convert "250" into an integer and calculate its square.
number="250"#str
number=int(number)#type casting
print(type(number))#int

#8.Convert 45 into a float, string, and boolean.
number=45
num1=float(number)
num2=str(number)
num3=bool(number)
print(type(num1))
print(type(num2))
print(type(num3))

#9.Convert 99.99 into an integer. Explain the output.
number=99.99
num1=int(number)
print(num1,type(num1))

#10.Accept a number as a string and convert it into an integer.
'''name="anuja"
name=int(name)
print(f"name:{name}{type(name)}")'''

#11.Accept a student's marks in string format and calculate the percentage after conversion.
'''python=87
sql=78
total=python+sql
print(total)
percentage=total*2/100
print(percentage)'''

#12.Predict the output:
a = 100
b = 20.5
print(str(a) + str(b))#10020.5
print(int(b))#20
print(float(a))#100.0
print(bool(0))#False
print(bool(""))#False

#String Data Type
#13.Accept a person's full name and display it in uppercase and lowercase.
name="anuja kapase"
name=name.upper()
print(name)

#14.Count the number of characters in a string.
name="anujakapase"
name=len(name)
print(name)

#15.Reverse a given string without using built-in reverse methods.
name="anujakapase"
print(name[::-1])

#16.Count how many times the letter "a" appears in a string.
name="anuja kapase"
print(name.count(a))
