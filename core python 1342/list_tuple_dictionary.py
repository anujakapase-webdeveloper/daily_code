#aria of a circle
r = 5
area = 3.14 * r * r
print("Area:", area)

c = 25
f = (c * 9/5) + 32
print("Fahrenheit:", f)

#simple interest
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Simple Interest:", si)

#check a number divided into 5 and 11
num = 55
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible")

#avg of the three student
a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("Average:", avg)   

#group of every element of a list
lst = [2, 3, 4]
prod = 1
for x in lst:
    prod *= x
print("Product:", prod)

lst = [1, 2, 3, 2, 4, 2, 5]
target = 2
print("Count:", lst.count(target))

#check itme is present in a list
lst = [10, 20, 30, 40]
item = 20
print("Exists" if item in lst else "Not exists")

#concatenate
l1 = [1, 2]
l2 = [3, 4]
print("Merged:", l1 + l2)

s = "python is very easy"
print("Words count:", len(s.split()))   

s = "hello world python"
print(s.replace(" ", "-"))

s = "apple"
print(s.startswith('a'))

s = "coding"
print("Index:", s.find('d'))

d = {'name': 'Rahul', 'age': 21}
print(d['name'], d['age'])      

d = {'a': 1}
d['b'] = 2
print(d)

#find product of all dictionary
d = {'a': 1}
d['b'] = 2
print(d)

d = {'name': 'Rahul', 'age': 21}
print(d['name'], d['age'])

print(type(2/4))