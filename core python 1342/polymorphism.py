#polymorphism
#method over loading
def add(*args):
    total=0
    for i in args:
        total+=i
    print(total)
add(20,45,65) 

class claculator:
    def sum(self,a,b=0,c=0):
        print(a+b+c)
c=claculator()
c.sum(34,65,12)
c.sum(34,65)

#student details
class student:
    def details(self,name,age=None):
        if age is None:
            print("name-->",name)
        else:
            print("name-->",name)
            print("age-->",age)
s1=student()
s1.details("aniket")
s1.details("anuja",22)     

#employee salary
class employee:
    def salary(self,basic,bonus=0):
        print("total salary-->",basic+bonus)
emp=employee()
emp.salary(20000,10000)
emp.salary(3000)   

#multiplication
class cal:
    def multi(self,a,b=1,c=1):
        print(a*b*c)
c=cal()
c.multi(2,4)  
c.multi(3,6,5)     

#greeting
class greeting:
    def greet(self,name,msg="welcome"):
        print(name,msg)
        if name == "jay":
            print("hello jay")
g=greeting()
g.greet("anuja")
g.greet("aniket","good mornig")
g.greet("chotu","good mornig chotu")    
g.greet("jay")    

#bill calculation
class cal:
    def bill(self,price,quantity=1):
        print("total bill-->",price*quantity)
c=cal()
c.bill(500)
c.bill(1000,3)  

#power calculation
class cal:
    def power(self,num,power=2):
        print(f"power of {num} is-->",num**power)
c=cal()
c.power(2)
c.power(3,2)  
c.power(4,3)    

#discount calculation
class discount:
    def dis(self,price,discount=0):
        total_discount=price*discount/100
        print("price of product-->",price)
        print("total discount-->",total_discount)
        print("total bill-->",price-total_discount)
d=discount()
d.dis(300)
d.dis(2000,10)
d.dis(5000,20)

#sum using *args
class cal:
    def add(self,*args):
        print("sum of number-->",sum(args))
c=cal()
c.add(2,4)   
c.add(34,65,3,4,76)   

#multify using *args
class multifly:
    def mul(self,*args):
        result=1
        for i in args:
            result=result*i
        print(result)
m=multifly()
m.mul(2,4,6,7)    
m.mul(2,3)    

#display students marks using *args
class student:
    def marks(self,*args):
        print("student marks->",args)
        print("total marks of students-->",sum(args))
s=student()
s.marks(23,54,76,89)   
s.marks(23,5,98,12)    

#find the avarage of student marks using args
class student:
    def marks(self,*args):
        avg=sum(args)/len(args)
        print("total marks of student-->",sum(args))
        print("average marks of students-->",avg)
s=student()
s.marks(34,65,87)   
s.marks(23,65,85,34,76)  

#find total arguments
class counter:
    def count(self,*args):
        print("total bill-->",sum(args))
        print("total items-->",len(args))
c=counter()
c.count(34,564,234,76)    

#display details
class details:
    def display(self,*args):
        for i in args:
         print("details-->",i)
d=details()
d.display("anuja",22,"pune")
d.display("aniket",18,"haragapur")   
d.display("chotu",4,"Haragapur")
d.display("jay",5,"haragapur")     








#method overrriding
class father:
    def display(self):
        print("father method")
class child(father):
    def display(self):
        print("child method")  
c=child()
c.display()     

#animal
class Animal:
    def sound(self):
        print("animal makes sound")
class dog(Animal):
    def sound(self):
        print("barking")
class cat(Animal):
    def sound(self):
        print("meow")
d=dog()
c=cat() 
d.sound()
c.sound()

#vihicle
class vihicle:
    def start(self):
        print('vihicle is starting')
class car(vihicle):
    def start(self):
        print("car is starting")
c=car()
c.start()                


#salary
class employee:
    def salary(self):
        print("employee salary is 50000")
class manager(employee):
    def salary(self):
        print("manager salary is 100000") 
        super().salary()
m=manager()
m.salary()   

#bank intrest
class bank:
    def intrest(self):
        print("bank intrest rate is 5%")
class SBI(bank):
    def intrest(self):
        print("SBI intrest rate is 7% ")
s=SBI()
s.intrest()        
                        


            



