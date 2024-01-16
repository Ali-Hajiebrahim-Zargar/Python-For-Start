max_com_multiple = 0
value = 0
for i in range (1,20):
    
    print("enter the ",i,"value:")
    a= int(input())
    num_com_multiple = 0
   
    for j in range(1,a):
        if a%j == 0:
            
            num_com_multiple = num_com_multiple +1 
            
    if num_com_multiple > max_com_multiple :
                
        max_com_multiple = num_com_multiple
        value = a
        
    elif  num_com_multiple == max_com_multiple :   
        
        if a > value :
            value = a
            
    else:
        
        continue
    
print("the maximum value is ", value)
print("the number of common multiplier is ", max_com_multiple )            