#dir()method is used to find out all the attributes and methods of a specified object, without the values. This function will return all the properties and methods, even built-in properties which are default for all object.
# x=[1,2,3]
# print(dir(x))
# print(x.__add__)

#dict() method is used to create a dictionary in Python. A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. The dict() method can be used to create an empty dictionary or to convert other data types (like lists or tuples) into a dictionary.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "USA"
        
p=Person("John", 30)
print(p.__dict__)     
print(help(p))    
