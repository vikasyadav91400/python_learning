a=int(input("Enter the first Number="))
b=int(input("Enter the second Number="))
for i in range(1,b+1):
    if (a%i==0)and(b%i==0):
        gcd=i
print("The gcd of given number is",gcd)
