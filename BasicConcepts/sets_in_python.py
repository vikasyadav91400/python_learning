# info={"Kerla",19, False, 5.4, 19}
# print(info)
# vikas=set()
# print(type(vikas))
# for item in info:
#     print(info)

# vik={"up",65,"Mayank",4.3,"a"}
# for item in vik:
#     print(vik)
#     print(type(vik))
    
# union & update
city1={"Lucknow","Bengaluru","Noida","Delhi"}    
city2={"Mumbai","Jammu","Lucknow","Noida"}
print(city1.union(city2))
city1.update
print(city2, city1)
#intersection & intersection_update
print(city1.intersection(city2))
city1.intersection_update
print(city1,city2)
#symmetric_diffrence & symmetric_diffrence_update
print(city1.symmetric_difference(city2))
#diffrence & diffrence_update
print(city1.difference(city2))
#isdisjoint
print(city1.isdisjoint(city2))


# city1={"Lucknow","Bengaluru","Noida","Delhi"}    
# city2={"Mumbai","Jammu",}
# print(city1.isdisjoint(city2))

#issuperset
print(city1.issuperset(city2))
#issubset
print(city1.issubset(city2))
#add
city1.add("Bhopal")
print(city1)
city2.add("Patna")
print(city2)
#pop
item=city1.pop()
print(city1)
print(item)
#del
# del city1
# print(city1)
#clear
city1.clear()
print(city1)