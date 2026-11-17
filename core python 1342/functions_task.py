#1.even number
#with arg with return type
def is_even(n):
    if n%2==0:
        return True
print(is_even(4))  

#with arg without return type
def is_even(n):
    if n%2==0:
        print("true")
is_even(6)   

#no argument with return type
def is_even():
    n=8
    if n%2==0:
        return True
print(is_even())  

#no arg without return type
def is_even():
    n=4
    if n%2==0:
     print("true")
is_even()    




#2.addition of two number
#with arg with return type
def add(a,b):
    return a+b
print(add(3,5))

#with arg without return type
def add(a,b):
    print(a+b)
add(5,8)   

#no argument with return type
def add():
    a=47
    b=5
    return a+b
print(add())

#no arg without return type
def add():
    a=3
    b=8
    print(a+b)
add()   





#3.reverse number
#with arg with return type
def rev(a):
    return a[::-1]
print(rev("python"))

#with arg without return type
def rev(s):
    print(s[::-1])
rev("python")   

#no argument with return type
def rev():
    s="python"
    return s[::-1]
print(rev())

#no arg without return type
def rev():
    s="python"
    print(s[::-1])
rev()  




#4.palindrome
#with arg with return type
def palindrome(s):
    if s==s[::-1]:
        return "palindrome"
print(palindrome("madam")) 

#with arg without return type
def palindrome(s):
    if s==s[::-1]:
        print("palindrome")
palindrome("saras") 

#no argument with return type
def palindrome():
    s="madam"
    if s==s[::-1]:
        return "palindrome"
print(palindrome())    

#no arg without return type
def palindrome():
    s="madam"
    if s==s[::-1]:
        print("palindrome")
palindrome()        



#5.prime number
#with arg with return type
def prime(n):
    count=0
    for  i in range (1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime"
print(prime(7))   

#with arg without return type
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime")
prime(7)   

#no argument with return type
def prime():
    count=0
    n=7
    for  i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime"
print(prime())     

#no arg without return type
def prime():
    count=0
    n=7
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime")
prime()      


#square of a number
#no arg without return type
def square():
    n=5
    print("square:",n*n)
square()        

#with arg without return type
def square(n):
    print("square:",n*n)
square(4)    

#no argument with return type
def square():
    n=8
    return n*n
print("square:",square())

#with arg with return type
def square(s):
    return s*s
print("square:",square(7))

#table
#no arg without return type
def table():
    num=5
    for i in range(1,11):
        print(num*i)
table()

#with arg without return type
def table(num):
    for i in range(1,11):
        print(num*i)
table(4) 

#no argument with return type
def table():
    num=6
    for i in range(1,11):
        return num*i
print(table()) 

#with arg with return type
def table(n):
    result=" "
    for i in range(1,11):
        result=n*i
    return result
(table(3))    



    





