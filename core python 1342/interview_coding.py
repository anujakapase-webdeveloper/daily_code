#reverse a list
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)

#remove duplicates

numbers = [10, 20, 10, 30, 20, 40]

result = list(set(numbers))

print(result)

#remove duplicates

numbers = [10, 20, 10, 30, 20, 40]

result = list(dict.fromkeys(numbers))

print(result)

#find second largest number
list1=[224,53,87,56,93,53,87]
unique=list(set(list1))
unique.sort()
print("second largest number:",unique[-2])

#find even and odd numbers from a list
list1=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in list1:
    if i%2==0:
        even+=1
    if i%2==1:
        odd+=1
print("even:",even)
print("odd:",odd)    

#find positive and negative numbers
list1=[1,3,5,-45,-6,7,-8,4,-5]
positive=[]
nagative=[]
for i in list1:
    if i>0:
        positive.append(i)
    if i<0:
        nagative.append(i)
print("positive:",positive)
print("negative:",nagative)            