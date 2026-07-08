# import time
# print(time.time())
#time.time
import time
# def usingWhile():
#     i=0
#     while(i<50000):
        
#         i = i + 1
#         print(i)
        
# def usingFor():
#     for i in range(50000):
               
#         print(i)        
        
# init = time.time()
# usingFor()
# t1=time.time() - init
# init = time.time()
# usingWhile()
# print(t1)
# print(time.time() - init)

# #time.sleep()



# print("Hello")
# time.sleep(3)
# print("This is printed after 3 seconds")
           
#time.strftime()

t=time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S", t)   

# print("current date:,Current time, ", formatted_time)      
print(formatted_time)
