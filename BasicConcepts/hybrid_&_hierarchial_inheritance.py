# Example of Hybrid Inheritance
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1, Derived2):
    pass

# Example of Hierarchical Inheritance
class baseClass:
    pass
class D1(baseClass):
    pass
class D2(baseClass):
    pass
class D3(D1):
    pass


