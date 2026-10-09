#identify operator
# is operator : it check memory address of both value if it same same it return true ,otherwise false
name="anuja"
Name="anuja"
print(name is name) #True because both values store in same memory address
print(id(name))
print(id(Name))

a=23
b=45
print(a is b) #False because both values store defferent memory address
print(id(a))
print(id(b))

#is not operator:it check  both memoy address if both memory addres same it return false otherwise True
x="aniket"
y="aniket"
print(x is not y) #False
print(id(x))
print(id(y))

X=56
Y=98
print(x is not y)#True
print(id(X))
print(id(Y))

# is operator and == opearator
# is operator: it is a identify operator it used to check memory address o two values if both values are same it return true otherwise fale
# == operator: it is the comparison operator it is used to compare two value if both values are same it return true otherwise false 
n="anuja"
m="aniket"
print(n is m) #Flase:because both values are store in deffernt memory address
print(n == m) #False:beacuse both values are defferent

num1=65
num2=65
print(num1 is num2) #True
print(num1 == num2)#True


stu_name=["anuja","gayatri","shubhangi"]
stu_n=["anuja","gayatri","shubhangi"]
print(stu_name is stu_n)#False:because both values store in defferent memory address
print(stu_name == stu_n)#True

age=[27,25,18]
Age=age
print(age is Age)#True :because both age value assign in Age varialbe it return True
print(age == Age)#False