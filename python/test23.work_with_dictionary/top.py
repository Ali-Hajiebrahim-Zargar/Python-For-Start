import collections  
print("please enter the number of country: ")
n = int(input())
country = dict()
for i in range(0,n):
    print("please enter the name of country")
    name = input()
    country[name]= country.get(name,0)+1
    
print(country)    
    