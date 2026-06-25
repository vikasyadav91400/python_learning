#reading a file in read mode


# f=open('myfile.txt', 'r')

# text=f.read()
# print(text)
# f.close()

#writing a file in writing mode
# f=open('myfile.txt', 'w' )
# f.write('Hello World')
# f.close()

#append mode
# f=open('myfile.txt', 'a' )
# f.write('Hello World')
# f.close()

# #with statment 
# with open('myfile.txt', 'a') as f:
#     f.write("Hey i am inside with")

#ewadline()method

f=open('myfile.txt', 'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
     break
    
    
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of students {i} in maths is: {m1}")
    print(f"marks of students {i} in Java is: {m2}")
    print(f"marks of students {i} in Python is: {m3}")
    
    i
        # print(line, type(line))
          
    print(line) 