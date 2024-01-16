b=0
while(1):
    
    print("please inter the age: ")
    a = int(input())
    
    if a == -1 :
        
        print("mission done")
        break
    elif (a<10) | (a>90):
    
        print("wrong value")
        
    elif a>b :
        b = a;
        
    else:
        
        continue
        
print(" the maximum age is ", b)        