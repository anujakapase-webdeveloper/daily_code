#student management
class student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course

    def display(self):
        print("name-->",self.name)
        print("rollno--",self.roll_no)
        print("course-->",self.course)
s1=student("anuja",10,"python")
s1.display()           

#employee salary details
class employee:
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

    def calculate_sal(self):
        annual_sal=self.salary*12
        print("annualsalary-->",annual_sal)

emp=employee("anuja",50000,101)
emp.calculate_sal()  

#mobile details
class mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("brand-->",self.brand)
        print("model-->",self.model)
        print("price-->",self.price)   

    def apply_discount(self,discount):
        self.price -= discount
        print("tota price-->",self.price)

mob=mobile("iphone","i18",10000)
mob.display()
mob.apply_discount(5000)        


#bank 
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("name-->",self.name)
        print("balance-->",self.balance)

    def deposite(self,deposite1):
        self.balance+=deposite1  

    def withdraw(self,withdraw):
        self.balance-=withdraw  

    def display(self):
        print("current balane-->",self.balance)

b1=bank("anuja",100000)
b1.deposite(50000)
b1.withdraw(25000)
b1.display()  

#car rentel system
class car:
    def __init__(self):
        self.name="swift"
        self.rent=800
        self.days=5
        print("name-->",self.name)
        print("rent-->",self.rent)
        print("days-->",self.days)

    def claculate_rent(self):
        total_rent=self.rent*self.days
        print("total rent-->",total_rent)
c1=car()
c1.claculate_rent()

#leptop
class leptop():
    def __init__(self):
      self.brand="dell"
      self.ram="16gb"
      self.price=50000

    def display(self):
        print("brand-->",self.brand)
        print("ram-->",self.ram)
        print("price-->",self.price)
l1=leptop()
l1.display()      

#book
class book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def display(self):   
        print("name-->",self.name)
        print("author-->",self.author)
        print("price-->",self.price)
b1=book("python","kiran",500)
b1.display()    

#rectangular area
class rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print("width-->",self.width)
        print("height-->",self.height)

    def cal_area(self):
        area=self.width*self.height
        print("area of rectangular-->",area)   
a1=rect(23,41)
a1.cal_area()     

#product inventory
class product():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):   
        print("name-->",self.name)
        print("price-->",self.price)
        print("quantity-->",self.quantity)

    def cal_price(self):
        total_price=self.price*self.quantity
        print("total price-->",total_price)

    def update_quantity(self,new_quantity):
        self.quantity=new_quantity
        print("quantity update-->",self.quantity)


p1=product("keyboard",1500,2)
p1.display()
p1.cal_price()  
print()
p1.update_quantity(4)    
p1.cal_price()    

#company information
class company:
    company_name="TCS"
    employee_count=500
    def __init__(self,emp_name,emp_id):
        self.emp_name=emp_name
        self.emp_id=emp_id
        company.employee_count+=1

    def display(self):
        print("company_name",company.company_name)
        print("employee_name",self.emp_name)
        print("employee_id",self.emp_id)  
        print("total employee",company.employee_count)
        

emp=company("anuja",101)
emp.display()

emp2=company("gayatri",102)
emp2.display()

#student
class student:
    school="KHPS haragapur"
    def __init__(self,student_name,roll_number):
       self.student_name=student_name
       self.roll_number=roll_number

    def display(self,percentage):
        print("school-->",student.school)
        print("sttudent name-->",self.student_name)
        print("roll number-->",self.roll_number)
        print("percentage-->",percentage)
s1=student("anuja",101)
s1.display(98)
print()
s2=student("swati",102)
s2.display(99)

#shopping cart
class shopping:
    dis_per=15
    def __init__(self,customer_name,total_amt):
        self.customer_name=customer_name
        self.total_amt=total_amt
    def display(self):
        discount=(self.total_amt*shopping.dis_per)/100
        final_amt=self.total_amt-discount
        print("customer name-->",self.customer_name)
        print("total_amt-->",self.total_amt)
        print("discount-->",discount)
        print("final amt-->",final_amt)   
s1=shopping("anuja",500)
s1.display()




