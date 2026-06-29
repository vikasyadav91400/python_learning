class Employee:
    def __init__(self, name, id, rollno):
        self.name = name
        self.id = id
        self.rollno = rollno
        
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name} rollno is {self.rollno}")
        
e1 = Employee("Vaibhav Balla", 400, 10) 
e1.showDetails()      
e2 = Employee("Ravi Kapoor", 401, 11) 
e2.showDetails()     
            
        
        