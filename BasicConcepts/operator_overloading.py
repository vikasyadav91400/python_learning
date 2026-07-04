class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x):
        return vector(self.i + x.i,  self.j + x.j, self.k + x.k)
       
v1 = vector(2, 3, 4)
print(v1)
v2 = vector(5, 6, 7)
print(v2)
print(v1 + v2)
# added_vector = vector(v1.i + v2.i, v1.j + v2.j, v1.k + v2.k)
# print(added_vector)
print(type(v1 + v2))  # Output: <class 'str'>
