#functions
#types of function
#built in functions
def len():
    print("hello")
len()  

def min():
    print(24,54,67)
min()    

#user define function
def add(a,b):
    print(a+b)
add(2,3)   

def mul(a,b):
    print(a*b)
mul(5,8)  

def mul(a,b):
    return a*b
print(mul(5,4)) 

#args with return type
def sum(x,y):
    return x+y
print(sum(3,5))

#args without return type
def sub(a,b):
    print(a-b)
sub(5,4)  

#no args with return type
def sub():
    a=4
    b=2
    return a-b
print(sub())

#no args without return type
def sub():
    x=9
    y=5
    return x-y
print(sub())


#student information
def studinfo(name,age,city,gender):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo("anuja",22,"pune","Female")

def studinfo(name,age,city,gender):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo(age=23,name="gayatri",city="pune",gender="Female")

# insert default value 
def studinfo(name,age,city,gender="female"):
    print("name-->",name)
    print("age-->",age)
    print("city-->",city)
    print("gender-->",gender)
studinfo(age=23,name="gayatri",city="pune")