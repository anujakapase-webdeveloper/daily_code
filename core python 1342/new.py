class Student():
    def __init__(self,name,age,class1):
        self.name=name
        self.age=age
        self.class1=class1
    def display(self):
        print("name-->",self.name)
        print("age-->",self.age)
        print("class-->",self.class1)

s1=Student("Ram",23,13)
s1.display()  

        
class Employee():
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def set_details(self):
        print("employee name-->",self.name)
        print("employee age-->",self.salary)
        print("employee department-->",self.department)
emp=Employee("shyam",50000,"python Developer")
emp.set_details()            
        