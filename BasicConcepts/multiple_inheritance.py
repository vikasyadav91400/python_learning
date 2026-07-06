class Employee:
    def __init__(self, name):
        self.name = name
        
        
class Dancer:
    def __init__(self, dance):
        self.style = dance     
        
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
       self.dance = dance
       self.name = name
       
o = DancerEmployee("John", "Hip Hop") 
print(o.name)  # Output: John
print(o.dance)
print(DancerEmployee.__mro__)  
     
   