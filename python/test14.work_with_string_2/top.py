print("please inter your equation:")
a = input()
count1 = 0
count2 = 0
count3 = 0
count_plus = 0

for i in range (0,len(a)) :
    
    if a[i] == '3' :
        
        count3= count3+1        
        
    elif a[i] == '2':
        
        count2= count2 +1
        
    elif a[i] == '1' :
        
        count1= count1+1
        
    else:
        
        count_plus = count_plus + 1;
        
a= count1*"1+"+count2*"2+"+count3*"3+"
print(a[:len(a)-1])                    
            
            