#student info
class student():
    def details(self, name, id, gender, marks, phoneno):
        self.name = name
        self.id = id
        self.gender = gender
        self.marks = marks
        self.phoneno = phoneno

    def display(self):
        print("name-->", self.name)
        print("id-->", self.id)
        print("gender-->", self.gender)
        print("marks-->", self.marks)
        print("phoneno-->", self.phoneno)


girl = student()
girl.details("Anuja", 1, "female", 99, 65623483749)
girl.display()

#employee details
class employee():
    def details(self,name,department,salary,id,city):
        self.name=name
        self.department=department
        self.salary=salary
        self.id=id
        self.city=city

    def display(self):
            print("name-->",self.name)
            print("department-->",self.department)
            print("salary-->",self.salary)
            print("id-->",self.id)
            print("city-->",self.city)
it=employee()
it.details("anuja","data analyst",100000,12,"pune")
it.display()

#mobile details
class mobile():
     def details(self,brand,model,color,price):
          self.brand=brand
          self.model=model
          self.color=color
          self.price=price

     def display(self):
          print("brand-->",self.brand) 
          print("model-->",self.model)
          print("color-->",self.color)
          print("price-->",self.price)
iphone=mobile()
iphone.details("iphone","i16","silver",100000)
iphone.display()      

#car details
class car():
     def details(self,brand,model,color,price):
          self.brand=brand
          self.model=model
          self.color=color
          self.price=price

     def display(self):
          print("brand-->",self.brand) 
          print("model-->",self.model)
          print("color-->",self.color)
          print("price-->",self.price)
swift=mobile()
swift.details("swift","2025","black",500000)
swift.display()   

#book details
class book():
     def details(self,title,author,price,pages):
          self.titla=title
          self.author=author
          self.price=price
          self.pages=pages

     def dispaly(self):
          print("titla-->",self.titla)
          print("author-->",self.author)
          print("price-->",self.price)
          print("pages-->",self.pages)

b1=book()
b1.details("python","james",500,500)
b1.dispaly() 

#leptop details
class leptop():
     def details(self,brand,ram,storage,price,operating_system):
          self.brand=brand
          self.ram=ram
          self.storage=storage
          self.price=price
          self.operating_system=operating_system
     
     def display(self):   
          print("brand-->",self.brand)
          print("ram-->",self.ram)
          print("storage-->",self.storage)
          print("price-->",self.price)   
          print("operating system-->",self.operating_system)

l1=leptop()
l1.details("Dell","8GB","238GB",18000,"windows11")
l1.display()

#bank account details
class bank():
     def details(self,bank_name,account_no,balance):
          self.bank_name=bank_name
          self.account_no=account_no
          self.balance=balance

     def display(self):
          print("bank name-->",self.bank_name)
          print("account_no-->",self.account_no)
          print("balance-->",self.balance)

b1=bank()
b1.details("union bank of india",64348387293802,500000)
b1.display()     

#teachers details
class teacher():
     def details(self,name,exp,salary,subject):
          self.name=name
          self.exp=exp
          self.salary=salary
          self.subject=subject
     def display(self):
          print("name-->",self.name)
          print("exp-->",self.exp)
          print("salary-->",self.salary)
          print("subject-->",self.subject)

t1=teacher()
t1.details("swati",1,25000,"computer science")
t1.display()   

#product details
class product():
     def details(self,name,price,quality,product_id):
          self.name=name
          self.price=price
          self.quality=quality
          self.product_id=product_id
     def display(self):
          print("name-->",self.name)
          print("price-->",self.price)
          print("quality-->",self.quality)
          print("product id-->",self.product_id)

t1=teacher()
t1.details("leptop",18000,1,101)
t1.display()   

#movies details
class movie():
     def details(self,name,hero,directer,rating):
          self.name=name
          self.hero=hero
          self.director=directer
          self.rating=rating
     def display(self):
          print("name-->",self.name)
          print("hero-->",self.hero)
          print("director-->",self.director)
          print("rating-->",self.rating)

t1=teacher()
t1.details("phir hera peri","akshay kumar","xyz",10)
t1.display()   

#hospital details
class hospital():
     def details(self,name,doctor,beds,location):
          self.name=name
          self.doctor=doctor
          self.beds=beds
          self.location=location
     def display(self):
          print("name-->",self.name)
          print("doctor-->",self.doctor)
          print("beds-->",self.beds)
          print("location-->",self.location)

t1=hospital()
t1.details("Annapurna hospital","Dr.vikas patil",100,"sankeshwar")
t1.display()   



          


               
          
           
          











