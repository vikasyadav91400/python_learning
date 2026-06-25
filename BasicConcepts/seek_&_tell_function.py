# #seek() function
# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(9)
#     data=f.read(7)
#     print(data)
    
# tell() function
# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(9) 
#     print(f.tell())
#     data=f.read(7)
#     print(data)    

# truncate() function
with open('myfile.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(4)
with open('myfile.txt', 'r') as f:
    print(f.read())
    
