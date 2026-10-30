#1. Create a tuple containing five integers and print it.
tup=(3,5,2,7,5)
print(tup)

#2. Create a tuple containing a string, integer, float, and Boolean value.
tup=("ram",45,8.3,True)
print(tup)

#3. Create a single-element tuple and verify its datatype.
tup=(34,)
print(type(tup))
tup=(65)
print(type(tup))

#4. Print the first, middle, and last elements of a tuple.
tup=(23,54,76,12,72,48,69,2)
first,*middle,last=tup
print(first)
print(middle)
print(last)

#5. Reverse a tuple using slicing.
tup=(34,23,54,87,45)
print(tup[::-1])

#6. Print every second element using slicing.
tup=(34,7628,8471,79)
print(tup[::2])

#7. Count how many times 25 occurs in a tuple.
tup=(45,243,25,65,35,76,25,76,25)
tup1=tup.count(25)
print(tup1)

#8. Find the index of a given element.
tup=(34,65,12,87,5)
tup1=tup.index(65)
print(tup1)

#9. Calculate the sum and average of numeric tuple elements.
tup=(23,65,45,23)
tup1=sum(tup)
print(tup1)

tup2=sum(tup)/len(tup)
print(tup2)

#10. Count even and odd numbers in a tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
for i in tup:
    if(i%2==0):
        print(i)

#11. Find the maximum and minimum values.
tup=(23,55,23,77,54,1,77)
print(min(tup))
print(max(tup))

#12. Check whether a particular value exists in a tuple.
tup=(43,76,23,87,34,12)
value=76
if  value in tup:
    print("value is  find")

else:
    print("value is not find")

#13. Convert a list into a tuple.
lis=[34,65,23,87,54]
tup=tuple(lis)
print(tup) 

#14. Unpack a tuple into four variables.
tup=(1,"ram","pune","python")
id,name,city,skill=tup
print(id)
print(name)
print(skill)
print(city)

#15. Swap two variables using tuple unpacking.
tup=(20,10)
tup2=(30,40)
tup,tup2=tup2,tup
print(tup)
print(tup2)

#16. Access a specific value from a nested tuple.
tup=((56,28),(78,89))
print(tup[0])

#17. Remove duplicate values while preserving order.


#19. Sort a tuple in ascending order and convert the result back into a tuple.
tup=(23,4,23,65,54,87)
lis2=list(tup)
lis1=lis2.sort()
print(lis1)

#20. Create a tuple of student names and marks, then print each student's details.
tup=(("name",89),("ram",67),("syam",56))
print(tup[0])
print(tup[1])
print(tup[2])
