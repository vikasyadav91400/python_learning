def cube(x):
    return x*x*x
print(cube(2))

#method1
l=[1,2,5,7,4]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)    

# #method2
l=[1,2,5,7,4]
newl=list(map(cube,l))
print(newl)



