#for loop
for i in range(100):
 print(i)

 #print 1 to 100 
 for i in range(1,101):
  print(i)

#print odd number with using if
for i in range(1,100):
  if(i%2==1):
   print("odd numbers",i) 

#print odd number without using is statement
for i in range(1,100,2):
 print(i) 

#print even number using if statement
for i in range(100):
  if(i%2==0) :
   print("even number",i) 

#print even number without using if statement
for i in range(0,100,2):
 print("even numbers",i) 

#print 3rd table
for i in range(1,11) :
   print(f"3 x {i} = {3*i} ")

#print 2 table 
for i in range(2,21,2):
 print(i)   

#print reverse numbers 200 to 1
for i in range(200,0,-1):
 print(i) 

#print numbers -100 to 100
for i in  range (-100,101):
 print(i)

#print 1 to 100 number with skipping 1 number
for i in range(1,101,2):
 print(i)  

#factorial
n=5
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)  

#sum of numbers
sum=4
total_sum=0
for i in range(1,n+1):
 total_sum+=i
print(total_sum)

#reverse the number
num=12345
for i in (str(num)[::-1]):
 print(i)

#print even number from 1 to 20
for i in range(0,21,2):
  print(i) 

#print odd number from 1 to 20
for i in range(1,21):
 print(i)  

#print 7 th table in reverse
for i in range(10,0,-1):
 print(i*7) 

#print square from 1 to 10
for i in range (1,11):
  print(i**2)

#print cubes from 1 to 5
for i in range(1,6):
 print(i**3)  

#print 5th table using range
for i in range(5,51,5):
 print(i)  

#print number which is divide by 5 from 1 to 100
for i in range(1,101):
  if(i%5==0):
   print(i) 

#print all element of a list
numbers=[21,22,23,24,25,26,27]
for num in numbers:
 print(num)   

#find sum and avg of a list
num=[10,20,30,40,50]
total=0
count=0
for x in num:
 total+=x
 count+=1
print(count) 
avg=total/count
print("sum of elements-->",total)
print("avarage of elements-->",avg)

#find maximum value in a list
nums=[12,43,76,4,7,56]
max_val=nums[0]
for x in nums:
 if x > max_val:
  max_val=x
print("maximum value",max_val)

#find minimum value in a list
nums=[12,43,76,4,7,56]
min_val=nums[0]
for x in nums:
  if x < min_val:
   min_val=x
print("minimum value",min_val)

#find positive number in a list
num=[-21,34,56,-3,84,-34,3,5,-8]
for x in num:
 if(x>0):
  print("positive numbers",x)

#find nagetive numbers in a list
num=[-21,34,56,-3,84,-34,3,5,-8]
for x in num:
 if x<0:
  print(x)

#reverse all number of a list
#num=[-21,34,56,-3,84,-34,3,5,-8]
#or i in num([::-1]):

#reverse all number in a list
nums = [10, 20, 30, 40, 50]
for i in range(len(nums) - 1, -1, -1):
  print(nums[i])

#find vowels
text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0
for char in text:
  if char in vowels:
    count += 1
print("Total Vowels:", count)  

#print *
for i in range(1,6):
 print("*"*i)

for i in range(4,0,-1):
 print("*"*i) 

