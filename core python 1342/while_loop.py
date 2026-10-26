#print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1

#print numbers from 10 to 1
i=10
while i>=1:
    print(i)
    i-=1  

#print number from -11 to 11
i=-11
while i<=11:
    print(i)
    i+=1  

#print numbers from 100 to -100
i=100
while i>=-100:
    print(i)
    i-=1

#reverse tha number
num=54321
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("reversed:",rev)

#print even numbers
i=0
while i<=20:
    print(i)
    i+=2

#print even number fom -10 to 20
i=-10
while i<=20:
    print(i)
    i+=2  

#print odd numbers from 1 to 20
i=1
while i<=20:
    print(i)
    i+=2   

#print negative number a list
numbers = [10, -5, 3, -2, 0, -8, 7]
i = 0
print("Negative numbers are:")
while i < len(numbers):
  if numbers[i] < 0:
    print(numbers[i])
  i += 1 

#print positive numbers from a list
numbers = [10, -5, 3, -2, 0, -8, 7]
i = 0
while i<len(numbers):
    if numbers[i]>0:
     print(numbers[i])
    i+=1   

#print 3 rd table
i=1
num=3
while i<=10:
   print(num*i)
   i+=1    

#print 4 th table
num=4
i=1
while i<=10:
   print(num*i)
   i+=1    

#sum  of digit

num = 123
sum_digits = 0
while num > 0:
  digit = num % 10  
  sum_digits += digit  
  num = num // 10  
print("Sum of digits:", sum_digits)

#print squares fro 1 to 10
i=1
while i<=10:
   square=i*i
   print("square of ",i,"is",square)
   i+=1   

#print cube from 2 to 20
i=2
while i<=20:
   cube=i*i*i
   print("cube of",i,"is",cube)
   i+=1  

#print numbers divided by 4 between 1 to 20
i=1
while i<=20:
   if(i%4==0):
      print(i)
   i+=1   

i=10
while i>=1:
   print("liftof",i)
   i-=1  

#44: Print multiples of 3 up to 30
i=3
while i<=30:
   print(i)   
   i+=3 

#print count of number 
i=8652653
count=0
while i>0:
   count+=1
   i=i//10
print(count)   

#print 5 tables in revers format
i=10
num=5
while i>=1:
   print(num*i)
   i-=1

#print prime number
num = int(input("enter a prime number: "))
i = 2
while i < num and num % i != 0:
    i += 1
if num > 1 and i == num:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

 #find prime numbers in a list
numbers = [10, 3, 5, 8, 11, 4, 13, 1, 17]
prime_numbers = []
for num in numbers:
    if num > 1:
        i = 2
        while i < num and num % i != 0:
            i += 1
        if i == num:
            prime_numbers.append(num)
print("Original List:", numbers)
print("Prime Numbers:", prime_numbers)   