
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
          