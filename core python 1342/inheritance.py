#inheritance
class animal():
    def eating(self):
        print("animal is eating")
class dog(animal):
    def sound(self):
        print("dog is barking")
d=dog()  
d.eating()
d.sound()  

#types of inheritance
#single inheritance
class father():
    def property(self):
        print("fathers's property")
class son(father):
    def study(self):
        print("python")
s=son()
s.property()
s.study()     

#meltilevel inheritance
class GF():
    def form(self):
        print("gf-->form")
class father(GF):
    def home(self):
        print("father's home")
class son(father):
    def cycle(self):
        print("my cycle")
s=son()
s.form()
s.home()
s.cycle()   

#multipe inheritance
class  father():
    def leadership(self):
        print("fathers property")
class mother():
    def cooking(self):
        print("mothers property")
class child(father,mother):
    def study(self):
        print("i am studing")
c=child()
c.leadership()
c.cooking()
c.study()

#heirarchical inhetitance
class father():
    def riding(self):
        print("riding a bike")
class child1(father):
    def driving(self):
        print("driving a car")
class child2(father):
    def sport(self):
        print("running") 
c=child1()
c1=child2()
c.riding()
c.driving()
c1.riding()
c1.sport()  

#hybrid inheritance
class GF():
    def form(self):
        print("GF's form")
class father(GF):
    def home(self):
        print("father's home")
class mother():
    def cooking(self):
        print("cooking")
class child1(father,mother):
    def sport(self):
        print("kabbadi")
class child2(father,mother):
    def study(self):
        print("python") 
c=child1()
c2=child2()
c.form()
c.home()
c.cooking()
c.sport()

c2.form()
c2.home()
c2.cooking()
c2.study()

#super () function
class father():
    def display(self):
        print("parent class")
class child(father):
    def display(self):
        super().display()
        print("child class")
c=child()                
c.display()

#practice questions
#single
class father():
    def property(self):
        print("father's property")
class child(father):
    def knowledge(self):
        print("knowledge")
c=child()
c.property()
c.knowledge()   

#heirarcical
class vihicle():
    def shape(self):
        print("round shape")
class car(vihicle):
    def size(self):
        print("small size")
class truck(vihicle):
    def size(self):
        print("big size")
c=car()
t=truck()
c.shape()
c.size()
t.shape()
t.size()

#inheritance with cunstructor
class father:
   def __init__(self):
      print("parent  class")
class child(father):
   def __init__(self):
       super().__init__()
       print("child class")
c=child()

#inheritance with parameter
class father:
   def __init__(self,name):
      self.name=name
      print("name",name)
class child(father):
   def __init__(self, name,age):
      super().__init__(name)
      self.age=age
      print("name-->",name,"age-->",age)
c=child("ram",22)        
      
 #inheritance without parameter
class father:
   def __init__(self):
      self.name="shyam"
class child(father):
   def __init__(self):
      super().__init__()  
      self.age=22
      print("name-->",self.name,"age-->",self.age)  
c=child()        


               







