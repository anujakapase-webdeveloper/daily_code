#set
set1={24,37,47,58,"anuja"}
print(set1)

#creating set
num={23,65,78,4,6,93,57}
print(num)
print(type(num))

#creating empty set
a=set()
print(type(a))#set

a={}
print(type(a))#dict

#set methods
#add()
fruits={"apple","banana","pinapel"}
fruits.add("kiwi")
print(fruits)

#remove
fruits={"apple","banana","pinapel"}
fruits.remove("banana")
print(fruits)

#set operations
#Union
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)
print(a.union(b))#{1,2,3,4,5,6,7,8}

#intersection
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a&b)
print(a.intersection(b))#{4,5}

#defference
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

#symmetric difference
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a^b)
print(a.symmetric_difference(b))

#frozen set
fruits=frozenset(["apple","banana","pinapel"])
print(fruits)
print(type(fruits))

# union in frozen set
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8])
print(type(a))
print(a|b)

#intersection in frozenset
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8])
print(type(a))
print(a&b)

#difference in frozenset
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8])
print(type(a))
print(a-b)
print(b-a)

#symmentric difference in frozenset
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8])
print(type(a))
print(a^b)

 






