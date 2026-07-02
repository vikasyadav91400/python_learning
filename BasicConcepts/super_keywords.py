class ParentClass:
    def parent_method(self):
        print("This is the parent method1.")
        
class ChildClass(ParentClass):
    def parent_method(self):
    
        print("Vaibhav")
        super().parent_method() 
    def child_method(self):    
        print("This is the child method2.")
        
    
        super().parent_method() 
        
child_object = ChildClass()
child_object.child_method() 
child_object.parent_method()               
        