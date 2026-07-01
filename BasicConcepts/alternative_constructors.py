class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod  
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])     
        
e1=Employee("John Doe", 50000)
print(e1.name) 
print(e1.salary)         
        
string="Harry-12000"
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)

string="Varry-22000"
e3=Employee.fromstr(string)
print(e3.name)
print(e3.salary)