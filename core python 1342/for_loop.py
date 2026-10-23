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

 