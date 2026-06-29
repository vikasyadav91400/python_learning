# try:
#     num = int(input("Enter an integer:"))
# except ValueError:
#     print("number entered is not a interger.")    
    
#finally clause
# try:
#  l=[1, 2 ,4, 7, 8]
#  i=int(input("enter the index:"))
#  print(l[i])
# except:
#     print("some error occurred")    
    
# finally:
#     print("I am always executed")    
#raising custom error
a=int(input('Enter any value between 5 & 9'))    
if(a<5 or a>9):
    raise ValueError("Value should be between 5 & 9") 
 

    
            