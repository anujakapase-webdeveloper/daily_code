#creating tuple
tuple=(2,3,4,5,6)
print(tuple)

# creating tuple using ,
tuple=23,54,67,12,43,56
print(tuple)

#we can store defferent data types in tuple
tuple=(23,"ram",False,45.4)
print(tuple)

#tuple is immutable(cannot be change)
'''tuple=(3,5,2,4,678,)
tuple[0]=6
print(tuple)'''

#tuple with built in functions
tuple=(34,65,78,23,67,53,6)
tuple=max(tuple)
print(tuple)

tuple=(34,65,78,23,67,53,6)
tuple=min(tuple)
print(tuple)

tuple=(34,65,78,23,67,53,6)
tuple=sum(tuple)
print(tuple)

#we can convert tuple into list
tuple=(34,65,78,23,67,53,6)
list=list(tuple)
print(list)

#converting list into tuple
'''list=[34,65,78,23,67,53,6]
tuple=tuple(list)
print(tuple)'''

#immutable and mutable
tuple=(34,65,[78,23,67],53,6)
tuple[2].append(84)
print(tuple)

#packing and unpacking
tuple=(1,"ram","pune")
id,name,city=tuple
print(id)
print(name)
print(city)

#tuple methods
#index()
tuple=(34,65,78,23,67,53,6)
tuple=tuple.index(34)
print(tuple)

#count()
tuple=(34,65,78,23,67,53,6,65)
tuple=tuple.count(65)
print(tuple)





