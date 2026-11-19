#local variable
def add():
    a=10
    b=15
    print(a+b)
add()  

def name():
    name="anuja"
    print(name)
name()

#global variable
age=22
def info():
    print("age:",age)
info() 
print(age)  

marks=99
def studinfo():
    marks=78
    print("marks:",marks)
studinfo()
print(marks)  

city="pune"
print(city)
def info():
    city="mumbai"
    print("city:",city)
city="bengaluru"    
info()
print(city)

#global keyword
skill="python"
print("skill:",skill)#python
def skill():
    global skill
    skill="java"
    print(skill)#java
def skills():
    skill=".net"
    print(skill)#.net
skill() 
skills()   
print(skill)#java

#nested function
def outer():
    a=10
    b=20
    print(a+b)
    def inner():
        x=10
        y=5
        print(x-y)
    inner()
outer()   

def outer():
    name="anuja"
    print(name)
    def inner():
        print("name:",name)
    inner()
outer()



    
    
    

    
