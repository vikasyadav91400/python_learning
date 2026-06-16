numbers=[1,2,3,4,5]

for index, num in enumerate(numbers):
    
    if(index > 0):
        numbers[index]=numbers[index-1]+ numbers[index]
   
    
 
    
    print(f"numbers = {numbers}")
    




