print("please enter your string:")
a = input()
b= a.lower()
c= a.upper()
big_cnter = 0
low_cnter = 0
for i in range(0,len(a)):
    
    if a[i] < b[i]:
        big_cnter = big_cnter+1
        
    else:
        low_cnter =low_cnter+1    
        
if big_cnter > low_cnter :
    
    print(c)
    
else:
    print(b)
        