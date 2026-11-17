#even number
#with arg with return type
def is_even(n):
    if n%2==0:
        return True
print(is_even(4))  

#with arg without return type
def is_even(n):
    if n%2==0:
        print("true")
is_even(6)   

#no argument with return type
def is_even():
    n=[]
    if n%2==0:
        return True
print(is_even(8))    
