#Abstraction
#animals
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):    
    def sound(self):
        print("dog is barking")
d1=dog()
d1.sound()   

#ATM
from abc import ABC,abstractmethod
@abstractmethod
class ATM(ABC):
    def withdraw(self):
        pass
class SBI(ATM):
    def withdraw(self):
        print("withdraw from SBI bank")
class HDFC(ATM):
    def withdraw(self):
        print("withdraw from HDFC bank")

sbi=SBI()
sbi.withdraw()      
hdfc=HDFC()
hdfc.withdraw()    

#payment
from abc import ABC,abstractmethod
class payment(ABC):
    def pay(self,amount):
        pass
class UPI(payment):
    def pay(self,amount):
        print("pay through UPI-->",amount)
class card(UPI):
    def pay(self,amount):
        print("pay through card-->",amount)  

u=UPI()
c=card()
u.pay(500)
c.pay(100)    

#employees
from abc import ABC,abstractmethod
@abstractmethod
class employee:
    def cal_salary(self):
        pass
class manager(employee):
    def cal_salary(self):
        print ("manger salary-->",5000)
class developer(manager):
    def cal_salary(self):
        print("developers salary-->",60000)
m=manager()
d=developer()
m.cal_salary()
m.cal_salary()        

        