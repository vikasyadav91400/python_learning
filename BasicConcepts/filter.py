l=[1,5,6,7,4,8.8]
def filter_function(a):
    return a>2
newl=list(filter(filter_function, l))
print(newl)
