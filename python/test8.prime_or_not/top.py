print("inter your desired value: ")
a = int(input())

for i in range(2,a):
    
    b = a%i
    print("i is ",i)
    print("b is:",b)
    if b == 0 :
        
        print("not prime")
        break
    elif (i==a-1):
        
        print("prime")
        break
        
    else:
        
        continue    