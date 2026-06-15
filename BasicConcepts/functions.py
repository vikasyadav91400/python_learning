# def calculategmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# a = 8
# b = 9
# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is greater") 
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# calculategmean(a,b)
# c = 5
# d = 10
# if(c>d):
#     print("first number is greater")
# else:
#     print("second number is greater") 
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)
# calculategmean(c,d)
# #calling function
# def name(fname, lname):
#     print("Hello,", lname, fname)

# name("John", "Doe")

#python arguments
#defaults arguments
# def name(fname,mname="kumar",lname="yadav"):
#     print("hello,",fname,mname,lname)
# name("vikas",)    

#keywords arguments
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name(mname="kumar",lname="yadav",fname="vikas")

#required arguments
#example1. when number of arguments passed does not match to the actual function definition.
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name("vikas","yadav","kumar")

