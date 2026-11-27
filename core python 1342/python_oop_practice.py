#student management system
class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display_details(self):
        print(f"student name-->{self.name}")
        print(f"student roll number-->{self.roll}")
        print(f"student marks-->{self.marks}")
s=student("anuja",101,98)
s1=student("gayatri",102,99)
s2=student("shubhangu",103,96)

s.display_details()
s1.display_details()
s2.display_details()

#Bank Account
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposite balance {amount} total balance {self.__balance}")
        else:
            print("invalid amount")
    def withdraw (self,amount):
        if amount>0:
            self.__balance-=amount
            print(f"withdraw balance {amount} total balance {self.__balance}")
        else:
            print("amount is not available")
    def display_balance(self):
        print(f"account holder name {self.name}")
        print(f"total balance {self.__balance}")
b=BankAccount("anuja",50000)
b.display_balance()
b.deposite(25000)
b.withdraw(10000)
b.display_balance()

#employee salary
class Employee:
    def emp(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

    def dis_emp(self):
        print(f"emp name{self.name}")
        print(f"emp id {self.emp_id}")
        print(f"emp salary {self.salary}") 
class manager(Employee):
    def man(self,department):
        self.department=department

    def dis_manager(self):
        self.dis_emp()
        print(f"department {self.department}")  

m=manager()
m.emp("anuja",101,50000)
m.man("python")     


#payment system
class creditcard():
    def payment(self):
        print("payment through credit card")
class UPI():
    def payment(self):
        print("payment through UPI")
class netbanking ():
    def payment(self):
        print("payment through netbanking")
c=creditcard()
u=UPI()
n=netbanking()
c.payment()
u.payment()
n.payment()  

#vehicle management
class vehical():
    def start(self):
        print("satring")
class car(vehical):
    def start(self):
        print("car is starting")
class bike(vehical):
    def start(self):
        print("bike is starting")
class bus(vehical):
    def start(self):
        print("bus is starting")
c=car()
c.start()
b=bike()
b.start()
bu=bus()
bu.start()       

#shape
from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass
class rectangle(shape):
    def __init__(self,height,widht):
        self.heght=height
        self.widht=widht
    def cal_area(self):
        print(f"area of a rectangle {self.heght * self.widht} " )

class circle(shape):
    def __init__(self,redius):
        self.redius=redius 

    def cal_area(self):
        print(f"area of a circle {math.pi * self.redius**2}")

rect=rectangle(54,87)
rect.cal_area()
c=circle(7) 
c.cal_area()     

#library management
class book:
    def __init__(self,book_name,author,price):
        self.book_name=book_name
        self.author=author
        self.price=price
    def dis_book(self):
        print(f"book name{self.book_name}")
        print(f"book written by {self.author}")
        print(f"book price {self.price}")
    def dis(self,dis_per):
        discount=(self.price*dis_per)/100
        self.price-=discount
        print(f"discount {dis_per} total price {discount}")
b=book("python","gddhijs",765)
b2=book("hddhf","ksdsj",88)
b3=book("njd","gyee",768)

b.dis_book()
b2.dis_book()
b3.dis_book()

b.dis(10)
b2.dis(8)
b3.dis(6)

#hospital management
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def dis_person(self,):  
      print("person name-->",self.name)
      print("person age-->",self.age)  

class doctor(person):
    def __init__(self,name,age,specilaization):
        super().__init__(name,age)
        self.specilaization=specilaization
    
    def dis_doctor(self):
       self.dis_person()
       print("specilaization-->",self.specilaization)

class sergory(doctor):
    def __init__(self,name,age,specilaization,sergory):
        super().__init__(name,age,specilaization)
        self.sergory=sergory
    def dis_sergory(self):
        self.dis_doctor()
        print("sergory-->",self.sergory)
s=sergory("Ram",26,"cardiotheracic",14)
s.dis_sergory()           


#employee salary management
class employee:
    def __init__(self,name,age,department,salary):
        self.name=name
        self.age=age
        self.department=department
        self._salary=salary
    def dis_details(self):
        print(f"emplyee name {self.name}")
        print(f"employee age {self.age}")
        print(f"employee department {self.department}")
        print(f"employee salary {self._salary}")

    def get(self):
        return self._salary
    def set(self,salary_inc) :
        if salary_inc>0  :                      
         self._salary+=salary_inc
        else:
            print("invlaid salary")

    def dis_details(self):
             print(f"emplyee name {self.name}")
             print(f"employee age {self.age}")
             print(f"employee department {self.department}")
             print(f"employee salary {self._salary}")       
class developer(employee):
    def __init__(self, name, age, department, salary,programming_languages):
        super().__init__(name, age, department, salary) 
        self.programming=programming_languages
    def dis_developer(self):
        self.dis_details()
        print("programming languages-->",self.programming)

d=developer("anuaja",22,"python developer",25000,"python")
d.dis_developer()                     
d.set(20000)
d.dis_developer()

#food ordering system
from abc import ABC,abstractmethod
class food():
    def __init__(self,price,quantity):
      self.price=price
      self.__quantity=quantity

    def get(self):
        return self.__quantity  
    def set(self,quantity):
        if quantity>0:
            self.__quantity+=quantity
        else:
            print("quantity must be greater than zero")
    @abstractmethod
    def cal_bill(self):
        pass


class pizza_order(food):
    def __init__(self, price, quantity,crust_type):
        super().__init__(price, quantity)
        self.crust_type=crust_type
    def cal_bill(self):
        base_total=self.price*self.get() 
        delivery_fee=5.00
        return base_total+delivery_fee
    def dis_bill(self):
        print("crust type-->",self.crust_type)  
        print("quantity-->",self.get())
        print("price-->",self.price)
        print("total bill-->",self.cal_bill())

class  burger(food):
    def __init__(self, price, quantity,meal_cambo):
        super().__init__(price, quantity) 
        self.meal_cambo=meal_cambo
    def cal_bill(self):
        base_total=self.price*self.get()
        if self.meal_cambo:
            base_total*=1.20
        return base_total
    def dis_bill(self):
        print(f"is mael cambo-->{"yes" if self.meal_cambo else 'NO'}")   
        print(f"quantity-->{self.get()}")
        print(f"price {self.price}")
        print(f"total bill{self.cal_bill()}")
pizza=pizza_order(100,1,"stuffed  crust")
burger=burger(50,2,meal_cambo=True)

pizza.dis_bill()
burger.dis_bill()
        
        
        


        



                  


        
