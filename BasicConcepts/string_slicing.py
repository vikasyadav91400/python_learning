name = "Vikas,Harish"
print(name[0:5])  
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word") 
print(len1)
print(fruit[0:5]) # including 0 but not 5
print(fruit[1:5]) # including 1 but not 5
print(fruit[:9])
print(fruit[0:-3])
print(fruit[-3:-1])
nm  = "Vikas"
print(nm[-4:-2])
#String methods
#String are immutable
a = "!!Vikas, vikas, vikas!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print (a.replace("Vikas", "Harish"))
b = "intruduction to python ProgRamming"
print(b.capitalize()) 
print(a.count("vikas"))
c = "Python is a great programming language ,,,,"
print(c.endswith(",,,"))
str1="He's name is Don. he is an honest men."
print(str1.find("is"))
print(str1.index("an"))
str2="Pythonisagreatprogramminglanguage"
print(str2.isalpha())
str3="my name is vikas"
print(str3.islower())
str4="my name is vikas"
print(str4.isprintable())
str5="  2  "
print(str5.isspace())
str6="My Name Is Vikas"
print(str6.istitle())
str7="My NamE Is Vikas"
print(str7.swapcase())
str8="Python is a great programming language"
print(str8.title())

