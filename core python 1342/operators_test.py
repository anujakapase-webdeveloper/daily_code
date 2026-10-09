#operatores Test
a=15//4
b=15%4
print(a,b)

x=-15//4
y=-15%4
print(x,y)

res=2**3**2
print(res)

val=10.0%3
print(type(val),val)

x=5.5+4.5*2//3
print(x)

p=10+3*2**2-4/2
print(p)

a=7
b=2.0
print(a//b)

print(10==10.0)

print([1,2]<[1,2,0])

a=5
print(1<a<10)

print("apple"> "Apple")

print(True==1,False==0)

print(10!=10.0)

x=0 and 10
y=5 and 20
print(x,y)

print(not[] and not"0")

x=[] or [0] or False
print(x)

a=True
b=False
print(a and not b or b)

a="Hello" or ""
b="" or "world"
print(a,b)

res=10 or 1 / 0
print(res)

print(not(5>2 and 3<21))

a=10
a+=5*2
print(a)

lst=[1,2]
lst+=[3,4]
print(lst)

if(n:=len("python"))>5:
  print(n)

x=8
x//=3
print(x)

a=5
a**=2
print(a)

x=12
x%=5
print(x)

a=5
b=3
print(a&b,a|b)

x=10
print(~x)

x=3
print(x<<2)

a=1
print((a<<3)-1)

a=5
b=3
print(a^b)

print(~(-5))

x=16
print(x>>3)

s="py" in "python"
print(s)

print(1 not in [1,2,3])

print("th" not in "python")

d={"a":1,"b":2}
print(1 in d,"a" in d)

t=(1,[2,3])
print(2 in t)

st={1,2,3}
print(3 in st)

a=[1,2]
b=[1,2]
print(a is b,a==b)

a="hello"
n="hello"
print(a is n)

p=[10]
q=p
print(p is not q)

x=256
y=256
print(x is y)

a=None
print(a is None)

x=True
y=1
print(x is y)

a=[1,2]
b=a
b+=[3]
print(a is b,a)

x=10
y=5
z=x>y and x&y or x^y
print(z)

x=5
print(x&1==9)

a=[1,2]
b=a
b=b+[3]
print(a is b,a)

x=10
y=5
z=x>y and x&y or x^y
print(z)