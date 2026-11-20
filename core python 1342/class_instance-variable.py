#class variable and instance variable
bonus=100#golbal variable
class teacher:
    school="english_medium"#class variable or static
    def __init__(self,name,id,subject):
        self.name=name#instance variable
        self.id=id
        self.subject=subject

    def display(self):
        print("name-->",self.name)
        print("id-->",self.id)
        print("subject-->",self.subject)
        print("school-->",teacher.school)
        print("bonus-->",bonus)

t1=teacher("swati",101,"CS")
t2=teacher("sakshi",102,"science")
t1.display()
t2.display()

#employee
class employee:
    company="TCS"#class variable
    def __init__(self,name,salary):
        self.name=name #instance variable
        self.salary=salary

    def display(self):
        print("name-->",self.name)   
        print("salary-->",self.salary)
        print("bonus-->",bonus)

emp=employee("anuja",100000)
emp1=employee("gayatri",100000)
emp.display()
emp1.display()

#hospital
class hospital:
    name="annapurna hispital"
    def __init__(self,p_name,age):
        self.p_name=p_name 
        self.age=age
    def display(self):
        print("patient name-->",self.p_name)
        print("age-->",self.age)

h1=hospital("ram",50)
h2=hospital("shyam",30)
h1.display()  
h2.display()
