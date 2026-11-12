i=23
if i%2==0:
    print("even")
else:
    print("odd")

num=-1
if num==0:
    print("number is zero")
elif num>0:
    print("positive number")
elif num<0:
    print("negative number")  

#revers number
num=12345
for i in (str(num)[::-1]):
 print(i)    


 


'''num=4
if num%num==0:
    print("prime number" )
else:
    print("not prime number")

for i in range(1,101,1):
    print(i)'''

n=5
fact=1
for i in range(1,n+1) :
    fact*=i
print(fact)

#square
for i in range(1,11):
    print(i**2)

#cube
for i in range(1,11):
    print(i**3)  

 #list   

#even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

#odd numbers
for num in numbers:
    if num % 2 != 0:
        print(num)

#even and odd count
my_list=[34,65,12,76,87,45,23,76,2,34,56]
even=0
odd=0
for num in my_list:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("even number count:",even)
print("even nymber count:",odd)

#reverse
my_list=[34,65,12,76,87,45,23,76,2,34,56]
for i in range(len(my_list) -1,-1,-1):
    print(my_list[i])

#my_list=[34,65,12,76,87,45,23,76,2,34,56] 

#find string
my_list=[10,"ram","python",56]
print("string in list:")
for items in my_list:
    if type(items)==str: 
        print(items)

#find integer
my_list=[10,"ram","python",56]
print("int number")
for i in my_list:
    if type(i)==int:
        print(i)

#tuple 

#maximun number
my_tuple=(23,65,23,87,56,9,6,24)
print(max(my_tuple))

#minmum number
my_tuple=(23,65,23,87,56,9,6,24)
print(min(my_tuple))

#sum of tuples
my_tuple=(23,65,23,87,56,9,6,24)
print(sum(my_tuple))

#find lenght of tuple
my_tuple=(23,65,23,87,56,9,6,24)
print(len(my_tuple))

#even numbers from a tuple
my_tuple=(23,65,23,87,56,9,6,24)
for num in my_tuple:
    if num%2==0:
        print(num)

#dictionary
#display keys and values
my_dict={"id":1,"name":"anuja"}
print(my_dict)  

my_dic=my_dict.items()
print(my_dic)

#total marks
student_marks={"rahul":65,"rani":89,"ram":97,"amit":32}
total_marks=0
for marks in student_marks.values():
    total_marks+=marks
print(total_marks)

#marks above 60
for name,marks in student_marks.items():
    if marks>60:
        print(marks)

# count number who is passed
passing_marks=40
passed_count=0
for marks in student_marks.values():
    if marks>=passing_marks:
     passed_count+=1
print(passed_count)  

#find highest number
highest_marks=max(student_marks.values())
print("highest marks:",highest_marks)


str="python"
rev=""
for i in str:
    rev=i+rev
print(rev)






    


