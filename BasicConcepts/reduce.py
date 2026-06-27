from functools import reduce 
numbers=[1,2,4,5,6,8,2]
def mysum(x, y):
    return x+y
sum= reduce(mysum, numbers)
print(sum)