class Employee:
    def __init__(self, name):
        self.name=name
        self.raise_amount=0.05
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount}")
        
emp1=Employee("Vaibhav") 
emp1.raise_amount=0.2
emp1.showDetails() 
# Employee.showDetails(emp1)   
emp2=Employee("Ramu") 
emp2.showDetails() 
            
        