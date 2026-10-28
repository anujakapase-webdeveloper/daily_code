#list
list=[23,54,67,43]
print(list)

#types of ways to iterating a list
list=[23,54,67,8,32,5,67,12,92,38]
for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])    

#using while loop
i=0
while i<len(list):
    print(list[i])
    i+=1   

#methods of list
list=[34,65,8,76,45,3,4,65,98,23,14,56,7,1]
list.append(34)
print(list)

#append()
list.append([32,45])
print(list)

#extend()
list.extend([32,45])
print(list)

#copy()
list.copy
print(list)

#count()
list.count(40)
print(list)

#index(0)
list.index(34,0,4)
print(list)

#insert()
list.insert(1,9)
print(list)

#pop()
list.pop(0)
print(list)

#remove()
list.remove(9)
print(list)

#sort
my_list=[23,52,1,34,9,1]
my_list.sort()
print(my_list)

#index
b=list.index(8)
print(b)

#count
C=list.count(23)
print(C)

#clear
c=list.clear()
print(c)

#addition of two list
m1=[23,65,78,64,83,23,94]
m2=[43,65,23,87,34,27,83]
list1=m1+m2
print(m1+m2)

#check values is present in a list
print(23 in m1)
print(100 in m2)
print(27 in list1)

#find max values in a list
list=[23,5,4,67,2]
print(max(list))

#find min value in a list
print(min(list))

#print sum of a list
print(sum(list))

#print length of a list
print(len(list))

