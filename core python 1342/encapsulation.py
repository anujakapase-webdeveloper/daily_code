class bank:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def getbalance(self):
        return self.__balance 
    @getbalance.setter
    def set__balance(self,amount):
        if amount>0: 
         self.__balance  +=amount
        else:
           print("invalid amount")


b1=bank(3400)
print(b1.getbalance)
set__balance=100
print(b1.getbalance)

#public variable
class classname:
   def __init__(self):
      self.name="anuja"
      self.age=22

   def display(self):
      print("name-->",self.name)
      print("age-->",self.age) 

c1=classname()
c1.display()
print(c1.name)
print(c1.age)

#protected variable
class className:
   def __init__(self):
      self._name="anuja"
      self._age=22

   def display(self):
      print("anuja-->",self._name)
      print("age-->",self._age)

c1=className()
c1.display()
print(c1._name)  

#private variable
class className:
   def __init__(self):
      self.__name="anuja"
      self.__age="21"
   def display(self):
      print("name-->",self.__name)
      print("age-->",self.__age)
        
c1=className()
c1.display()

     
