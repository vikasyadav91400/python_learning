class Person:
    def __init__(self, name, occ):
        print("Hey I am a Person")
        self.name=name
        self.occ=occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")  
        
a=Person("Vikas", "DEveloper")
b=Person("Harry", "HR")
a.info()
b.info()          