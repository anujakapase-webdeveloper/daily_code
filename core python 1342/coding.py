
#table
n=5
for i in range(1,11):
     print(n*i)

#fact
n=6
fact=1
for i in range(1,n+1):
     fact=fact*i
     print(fact) 

#prime
n=4
count=0
for i in range(1,n+1):
     if n%i==0:
          count+=1
if count==2:
     print("prime")
else:
     print("not a prime")

#even 
n=2
if n%2==0:
     print("even")  

#odd
n=5
if n%2!=0:
     print("odd")

#reverse
n=12345
rev=0
for i in range(len(str(n))):
     digit=n%10
     rev=rev*10+digit
     n=n//10
print("reverse:",rev)   

#sum
n=1234
total=0
for i in range(len(str(n))):
     digit=n%10
     total=total+digit
     n=n//10
print("total",total)   

#count
n=12345
count=0
for i in str(n):
     count+=1
print(count)   

#fibonacci
a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a + b


#   table
n=10
for i in range(1,11):
     print(n*i) 

#fact
n=5
fact=1
for i in range(1,n+1):
     fact=fact*i
print(f"factorial of {n}is {fact}")     

#even or add
n=5
if n%2==0:
     print("even")
else:
     print("odd")

#  prime
n=5
count=0
for i in range(1,n+1):
     if n%i==0:
          count+=1
if count==2:
     print("prime")
else:
     print("not a prime")   
     #prime
n=6
coun=0
for i in range(1,n+1):
     if n%i==0:
          count+=1
if count==2: 
 print("prime")
else:
     print("not a prime")  

#rev
num=12345
rev=0
for i in range(len(str(num))):
     digit=num%10
     rev=rev*10+digit
     num=num//10
print(rev)          

sum=12335
total=0
for i in range(len(str(sum))):
     digit=sum%10
     total=total+digit
     sum=sum//10
print(total) 

#fibonacci
a=0
b=1
for i in range(10):
     print(a)
     a,b=b,a+b

#palindrome
num=121
if str(num)==str(num)[::-1]:
     print("palindrome")
else:
     print("not a palindrome")  

     #sum of even numbers
total_sum=0
for i in range(0,51,2):
     sum=sum+i
print("sum of even number",sum)    




n=5
fact=1
for i in range(1,n+1):
     fact=fact*i
print(f"fact of {n}is{fact}")  

n=6
count=0
for i in range(1,n+1):
     if n%2==0:
          count+=1
if count==2:
     print("prime")
else:
     print("not a prime")

n=12345
total=0
for i in range(len(str(n))):
     digit=n%10
     total=total+digit
     num=n//10
print(f"sum of {n} is {total}")  

#rev
n=12345
rev=0
for i in range(len(str(n))):
     digit=n%10
     rev=rev*10+digit
     n=n//10
print(rev)  

#palindrome
n=141
if str(n)==str(n)[::-1]:
     print("palindrome")
else:
     print("is a palindrome")   

#sum of even number
sum=0
for i in range(0,51,2):
     sum+=i
print(sum)
            