#*args functions
#multiple argument
def num(*args):
    print(args)
num(23,65,46,98,12)  

def name(*args):
    print(args)
name("anuja","gayatri","shibhangi")   

#addition
def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum(23,65,8,43,19)

#find large number
def larger(*args):
    print("larger:",max(args))
larger(23,65,12) 

#find minimun number
def minimum(*args):
    print("smaller:",min(args))
minimum(1,2,3,4)    



#**kwargs
def info(**kwargs):
    return kwargs
print(info(name="anuja",age=22,city="pune",gender="female"))

#using both *args and **kwargs
def info(*args,**kwargs):
    print(args,kwargs)
info(23,65,84,12,name="anuja",age=23,city="pune")    


