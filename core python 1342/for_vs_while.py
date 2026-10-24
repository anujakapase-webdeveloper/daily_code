#for loop
#print factorial of 5
fact=5
for i in range(1,5):
    fact=fact*i
print(fact)

#fibonacci
n=5
a=0
b=1
count=0
for _ in range(n):
   next_num=a+b
   a=b
   b=next_num
   print(next_num)






#while loop
#print factorial of 10
num = 10
factorial = 1
i = 1
while i <= num:
  factorial = factorial * i
  i += 1
print("Factorial of", num, "is:", factorial)   

#fibonacci
n=20
a=0
b=1
count=0
while n>=count:
   next_num=a+b
   a=b
   b=next_num
   count+=1
   print(next_num)

